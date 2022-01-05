from sqlalchemy import create_engine, MetaData
import config.env

engine = create_engine(config.env.DB_DSN)

conn = engine.connect()

meta = MetaData()
