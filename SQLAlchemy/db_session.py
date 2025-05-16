from sqlalchemy.orm import sessionmaker
from SQLAlchemy import engine

# Fábrica de sesiones
Session = sessionmaker(bind=engine)

# Instancia única reutilizable
session = Session()