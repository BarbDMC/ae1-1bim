import config

from sqlalchemy.orm import sessionmaker
from SQLAlchemy import engine
from models import Servicios
from sqlalchemy import and_
from datetime import date

Session = sessionmaker(bind=engine)
session = Session()

servicios = session.query(Servicios).filter(
    and_(
        Servicios.costo > 100,
        Servicios.fecha > date(2024, 5, 12)
    )
).all()

print("Servicios con costo > 100 realizados después del 12/05/2024:")
for servicio in servicios:
    print(f"ID: {servicio.id}, Descripción: {servicio.descripcion}, Costo: {servicio.costo}, Fecha de Servicio: {servicio.fecha}, Vehículo ID: {servicio.vehiculo_id}")