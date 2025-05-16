import config

from SQLAlchemy.db_session import session
from models import TalleresMecanicos, Vehiculos, Servicios

talleres = session.query(TalleresMecanicos).all()
vehiculosRegistrados = session.query(Vehiculos).all()
servicios = session.query(Servicios).all()

print("Talleres Mecánicos:")
print("===================================")
print("Id | Nombre | Dirección | Teléfono")
for taller in talleres:
    print(f"{taller.id} | {taller.nombre} | {taller.direccion} | {taller.telefono}")

print("\nVehículos Registrados:")
print("===================================")
print("Id | Marca | Modelo | Año | Placa | Año de fabricación | Taller ID")
for vehiculo in vehiculosRegistrados:
    print(f"{vehiculo.id} | {vehiculo.marca} | {vehiculo.modelo} | {vehiculo.anio_fabricacion} | {vehiculo.placa} | {vehiculo.taller_id}")


print("\nServicios:")
print("===================================")
print("Id | Descripción | Costo | Fecha de Servicio | Vehículo ID")
for servicio in servicios:
    print(f"{servicio.id} | {servicio.descripcion} | {servicio.costo} | {servicio.fecha} | {servicio.vehiculo_id}")