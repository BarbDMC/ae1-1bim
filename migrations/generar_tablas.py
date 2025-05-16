import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SQLAlchemy.db import engine, Base
import models  # importante: importa __init__.py que carga los modelos

Base.metadata.create_all(engine)