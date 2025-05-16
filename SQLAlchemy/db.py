from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from configuracion import string_connection_database

engine = create_engine(string_connection_database)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()