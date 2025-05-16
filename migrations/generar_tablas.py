from SQLAlchemy.db import engine, Base
import models  # importante: importa __init__.py que carga los modelos

Base.metadata.create_all(engine)