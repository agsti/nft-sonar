import sqlite3
import datetime

new_db_name = "data/database_%s.db" %(datetime.datetime.now().isoformat())

f = open("data/LATEST_DB.txt", "w")
f.write(new_db_name)
f.close()

con = sqlite3.connect(new_db_name)

con.execute('''CREATE TABLE collections
               (
               created_at text,
               slug text NOT NULL,
               name text,
               telegram_url text,
               twitter_username text,
               latest_fetch datetime
               )''')

con.execute('''
                CREATE TABLE new_assets
               (
               collection_id integer,
               asset_url text,
               marketplace_url text,
               name text,
               contract_name text,
               contract_address text,
               erc text,
               filename text,
               hash blob,
               FOREIGN KEY(collection_id) REFERENCES collections(rowid))
               ''')
