import sqlite3
import os

class Database:
    def __init__(self):
        self.SQLPATH = 'ttele.db'
        self.conn = sqlite3.connect(self.SQLPATH, uri=True)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # subscriber != donator : 0 False 1 True
        # full_subscriber : 0 False 1 True (will join group)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            user_id integer primary key autoincrement,
                            chat_id integer null,
                            username text null,
                            firstname text null,
                            is_subscriber integer null,
                            is_full_subscriber integer null,
                            is_block integer null
                        )''')
        

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS admins(
                            admin_id integer primary key,
                            chat_id integer null,
                            username text null,
                            role text null
                        )''')
        
        # caption : 0 False 1 True
        # keyboard : 0 False 1 True
        # def_inline : gelbooru | konachan | realbooru | aibooru
        # lang : id | en | ru | zh
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS settings(
                            sett_id integer primary key autoincrement,
                            lang text null,
                            def_inline text null,
                            caption integer null,
                            keyboard integer null,
                            excluded_tags text null,
                            chat_id integer null
                        )''')
        
        # safe username of public channel
        # will grab any username inserted, became my own database
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS links(
                            link_id integer primary key autoincrement,
                            url text null,
                            type text null,
                            notes text null
                        )''')
        
        # safe messages
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages(
                            msg_id integer primary key autoincrement,
                            id integer null,
                            entity text null,
                            link text null,
                            type text null
                        )''')
        
        self.conn.commit()
        self.dumpSQL()
        self.conn.close()
        

    # Hapus table
    def drop_table(self, table_name):
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()
        self.dumpSQL()
    
    
    # Dumping sql database as txt
    def dumpSQL(self):
        with open('base_sqlite_values.txt', 'w', encoding='utf-8') as f:
            for line in self.conn.iterdump():
                f.write('%s\n' % line)


