import re
import logging

from pyrogram import filters
from pyrogram.types import InlineQuery, CallbackQuery, Message
from pyrogram.enums import ParseMode
from pyrogram.enums import MessageEntityType

from test_tele.features.pyrogram.pixiv import inline_pixiv, get_px_file
from test_tele.features.pyrogram.gelbooru import inline_gelbooru, get_gb_file
from test_tele.features.pyrogram.manga import inline_mangapark, check_inline_query_type
from test_tele.features.pyrogram.realperson import inline_realperson, get_nude_file
from test_tele.features.pyrogram.furry import inline_furry, get_fur_file
from test_tele.datas import db_helper as dbh


query = dbh.Query()


async def find_links(text):
    link_pattern = r'((?:t.me/|@)[_0-9a-zA-Z/]+)'

    links = []
    for link in re.findall(link_pattern, text):
        link_type = 'sticker' if 'addstickers' in link else 'addlist' if 'addlist' in link else 'channel'
        links.append((link, link_type))
    return links


async def save_links(links):
    for link, link_type in links:
        link = link.replace("@", "t.me/")
        if link_type == 'channel':
            tme, url, *id = link.split("/")
            link = f"{tme}/{url}"
        link = "https://" + link
        if not query.read_datas('links', None, 'url = ?', [link]):
            query.create_data('links', ['url', 'type'], [link, link_type])


async def get_links(event):
    links = await find_links(event.text)
    if links:
        await save_links(links)

    try:
        for entity in event.entities:
            if entity.type == MessageEntityType.TEXT_LINK:
                links = await find_links(entity.url)
                await save_links(links)
    except:
        pass


async def run_pyrogram():
    from test_tele.live_pyrogram import APP
    app = APP

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    @app.on_message(filters.text | filters.photo | filters.sticker)
    async def incoming_message_handler(app, message: Message):
        """Handle spesific incoming message"""
        try:
            if message.text:
                # grab links
                await get_links(message)
            elif message.photo:
                logging.warning("ya ini photo")
                # logging.warning(message.photo)
            elif message.sticker:
                logging.warning("ya ini sticker")
                link = await find_links(f"t.me/addstickers/{message.sticker.set_name}")
                await save_links(link)
                
        except Exception as err:
            logging.error(err, exc_info=True)
    

    @app.on_inline_query()
    async def inline_handler(app, inline_query: InlineQuery):
        """Handle inline query search"""
        query_handlers = {
            '/': check_inline_query_type,
            '.md': inline_mangapark,
            '.px': inline_pixiv,
            '.rp': inline_realperson,
            '.fur': inline_furry
            # '.2d': inline_vanillarock
        }

        for query_prefix, handler in query_handlers.items():
            if inline_query.query.lower().startswith(query_prefix):
                await handler(app, inline_query)
                break
        else:
            await inline_gelbooru(app, inline_query)


    @app.on_callback_query(filters.regex(r"(?:md|gb|px|rp|fur|2d)"))
    async def callback_query_handler(app, callback_query: CallbackQuery):
        """Get callback query from inline keyboard"""
        handlers = {
            "md": None,
            "gb": get_gb_file,
            "px": get_px_file,
            "rp": get_nude_file,
            "fur": get_fur_file
            # "2d": get_vr_file
        }

        for prefix, handler in handlers.items():
            if callback_query.data.startswith(prefix):
                image_file = await handler(callback_query.data.replace(f"{prefix} ", ''))
                if callback_query.data.startswith("md"):
                    await app.send_photo(callback_query.from_user.id, image_file)
                else:
                    await app.send_document(callback_query.from_user.id, image_file)
                break
        else:
            pass


    await app.start()