import sqlite3
import datetime


def create_new_db_file():
    new_db_name = "data/database_%s.db" %(datetime.datetime.now().isoformat())

    f = open("data/LATEST_DB.txt", "w")
    f.write(new_db_name)
    f.close()
    return new_db_name


def create_schema(filename):
    con = sqlite3.connect(filename)

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
                    CREATE TABLE assets
                   (
                   collection_id integer,
                   asset_url text,
                   marketplace_url text,
                   name text,
                   contract_name text,
                   contract_address text,
                   erc text,
                   filename text,
                   kind text,
                   hash blob,
                   FOREIGN KEY(collection_id) REFERENCES collections(rowid))
                   ''')


def setup_db():
    filename = create_new_db_file()
    print(f"New database file created {filename}")
    create_schema(filename)
    print("Schema has been loaded")


if __name__ == "__main__":
    setup_db()
