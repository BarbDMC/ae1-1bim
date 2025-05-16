import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from sqlalchemy.orm import sessionmaker
from SQLAlchemy import engine
from models import TalleresMecanicos, Vehiculos, Servicios

from datetime import date

# Se crea la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear objetos de tipo TalleresMecanicos
taller1 = TalleresMecanicos(nombre="AutoFix", direccion="Av. Siempre Viva 123", telefono="0999999999")
taller2 = TalleresMecanicos(nombre="Motores Pro", direccion="Calle Central 456", telefono="0888888888")

# Crear objetos de tipo Vehiculos
vehiculo1 = Vehiculos(placa="ABC123", marca="Toyota", modelo="Corolla", anio_fabricacion=2015, taller=taller1)
vehiculo2 = Vehiculos(placa="XYZ789", marca="Chevrolet", modelo="Aveo", anio_fabricacion=2012, taller=taller1)
vehiculo3 = Vehiculos(placa="LMN456", marca="Kia", modelo="Sportage", anio_fabricacion=2020, taller=taller2)

# Crear objetos de tipo Servicios
servicio1 = Servicios(descripcion="Cambio de aceite", costo=35.0, fecha=date(2024, 5, 10), vehiculo=vehiculo1)
servicio2 = Servicios(descripcion="Revisión de frenos", costo=80.0, fecha=date(2024, 5, 12), vehiculo=vehiculo1)
servicio3 = Servicios(descripcion="Cambio de disco de embrague", costo=150.0, fecha=date(2024, 5, 14), vehiculo=vehiculo2)
servicio4 = Servicios(descripcion="Alineación y balanceo", costo=50.0, fecha=date(2024, 5, 15), vehiculo=vehiculo3)

# Agregar los objetos a la sesión
session.add_all([
    taller1, taller2,
    vehiculo1, vehiculo2, vehiculo3,
    servicio1, servicio2, servicio3, servicio4
])

# Confirmar la transacción
session.commit()
