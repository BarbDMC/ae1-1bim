import config

from sqlalchemy.orm import sessionmaker
from SQLAlchemy import engine
from models import Vehiculos

Session = sessionmaker(bind=engine)
session = Session()

vehiculos_kia = session.query(Vehiculos).filter(Vehiculos.marca == "Kia").all()

print("Vehículos marca Kia:")
for vehiculo in vehiculos_kia:
    print(f"ID: {vehiculo.id}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio_fabricacion}, Placa: {vehiculo.placa}, Taller ID: {vehiculo.taller_id}")
