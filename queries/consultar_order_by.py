import config

from SQLAlchemy.db_session import session
from models import Servicios
from sqlalchemy import desc

servicios = session.query(Servicios).order_by(desc(Servicios.fecha)).all()

print("Servicios ordenados por fecha:")
for servicio in servicios:
    print(f"ID: {servicio.id}, Descripción: {servicio.descripcion}, Costo: {servicio.costo}, Fecha de Servicio: {servicio.fecha}, Vehículo ID: {servicio.vehiculo_id}")
