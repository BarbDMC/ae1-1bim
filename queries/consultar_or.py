import config

from sqlalchemy.orm import sessionmaker
from SQLAlchemy import engine
from models import Vehiculos
from sqlalchemy import or_

Session = sessionmaker(bind=engine)
session = Session()

vehiculos = session.query(Vehiculos).filter(
    or_(Vehiculos.marca == "Toyota", Vehiculos.marca == "Chevrolet")
).all()

print("Vehículos Toyota o Chevrolet:")
for vehiculo in vehiculos:
    print(f"ID: {vehiculo.id}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio_fabricacion}, Placa: {vehiculo.placa}, Taller ID: {vehiculo.taller_id}")
