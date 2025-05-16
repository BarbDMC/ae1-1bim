import config

from SQLAlchemy.db_session import session
from models import Vehiculos

vehiculos_kia = session.query(Vehiculos).filter(Vehiculos.marca == "Kia").all()

print("Vehículos marca Kia:")
for vehiculo in vehiculos_kia:
    print(f"ID: {vehiculo.id}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio_fabricacion}, Placa: {vehiculo.placa}, Taller ID: {vehiculo.taller_id}")
