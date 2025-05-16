from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()