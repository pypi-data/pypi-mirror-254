"""The module responsible for operating tgcf in live mode"""
# untuk live pryogram ada di --> user_bot/pyrogram

from test_tele.user_bot.telethon import *

ALL_EVENTS = USER_BOT_HANDLER


async def start_sync() -> None:
    """Start tgcf live sync."""
    # clear past session files
    clean_session_files()

    USER_SESSION = StringSession(CONFIG.login.SESSION_STRING) # tambahan ku
    # SESSION = get_SESSION()
    client = TelegramClient( 
        USER_SESSION,
        CONFIG.login.API_ID,
        CONFIG.login.API_HASH,
        sequential_updates=CONFIG.live.sequential_updates,
    )
    bot_client = TelegramClient( # tambahan ku
        'tgcf_bot',
        CONFIG.login.API_ID,
        CONFIG.login.API_HASH,
        sequential_updates=CONFIG.live.sequential_updates,
    )
    
    if CONFIG.login.user_type == 0: # bot
        if CONFIG.login.BOT_TOKEN == "":
            logging.warning("Bot token not found, but login type is set to bot.")
            sys.exit()
        await bot_client.start(bot_token=CONFIG.login.BOT_TOKEN) # edit variable
    else:
        await client.start()
        await bot_client.start(bot_token=CONFIG.login.BOT_TOKEN) # tambahan ku

    config.is_bot = await bot_client.is_bot()
    logging.info(f"config.is_bot={config.is_bot}")

    await config.load_admins(bot_client)

    if CONFIG.login.user_type == 1: # user
        command_events = get_events(1)
        ALL_EVENTS.update(command_events)
        for key, val in ALL_EVENTS.items():
            if config.CONFIG.live.delete_sync is False and key == "deleted":
                continue
            client.add_event_handler(*val)

    # tambahan ku
    command_events = get_events(0)
    ALL_EVENTS.update(command_events)
    for key, val in ALL_EVENTS.items():
        if config.CONFIG.live.delete_sync is False and key == "deleted":
            continue
        bot_client.add_event_handler(*val)
        logging.info(f"Added event handler for {key}")

    if const.REGISTER_COMMANDS: # config.is_bot and
        await bot_client( # edit variable
            functions.bots.SetBotCommandsRequest(
                scope=types.BotCommandScopeDefault(),
                lang_code="en",
                commands=[
                    types.BotCommand(command=key, description=value)
                    for key, value in const.COMMANDS.items()
                ],
            )
        )
    config.from_to, config.reply_to = await config.load_from_to(client, config.CONFIG.forwards)

    if CONFIG.login.user_type == 1: # user
        await client.run_until_disconnected()
    await bot_client.run_until_disconnected()
