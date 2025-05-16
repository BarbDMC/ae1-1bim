# ae1-1bim
## Actividad: Use los conceptos de ORM a través de la librería SqlAlchemy en lenguaje Python - AE1

Este proyecto utiliza **Python**, **SQLite** y **SQLAlchemy** para modelar y consultar un sistema de talleres mecánicos, vehículos y servicios realizados.

---

## ✅ Instalaciones previas

Antes de ejecutar el proyecto, asegúrate de tener lo siguiente instalado:

1. **Python 3.8+**
2. **Ejecutar:** `pip install sqlalchemy`

## 📁 Estructura del proyecto

ae1-1bim/
├── SQLAlchemy/
│   ├── db.py                     # Define engine, Base y SessionLocal
│   ├── db_session.py             # Instancia única de sesión
│   ├── configuracion.py             # Define la cadena de conexión a la base de datos
├── models/
│   ├── __init__.py               # Importa todos los modelos
│   ├── talleres_mecanicos.py     # Modelo de TalleresMecanicos
│   ├── vehiculos.py              # Modelo de Vehiculos
│   └── servicios.py              # Modelo de Servicios
├── migrations/
│   ├── generar_tablas.py        # Crea las tablas en la base de datos
│   ├── insertar_datos.py        # Inserta datos de prueba
├── queries/
│   ├── config.py                     # Configura el path global del proyecto
│   ├── consultar_all.py         # Consulta con `.all()`
│   ├── consultar_filter.py      # Consulta con `.filter()`
│   ├── consultar_order_by.py    # Consulta con `.order_by()`
│   ├── consultar_or.py          # Consulta con `or_()`
│   └── consultar_and.py         # Consulta con `and_()`

## 🧱 Cómo ejecutar las migraciones

1. Asegúrate de estar en la raíz del proyecto.

2. Ejecuta la creación de las tablas:
`python migrations/generar_tablas.py`

3. Inserta los datos de prueba:
`python migrations/insertar_datos.py`

## 🔍 Cómo ejecutar las consultas

Cada archivo en la carpeta queries/ ejecuta una consulta distinta. Puedes probarlos así:
Asegúrate de tener las tablas y datos creados previamente usando los scripts de migrations/.

`python queries/consultar_all.py`
`python queries/consultar_filter.py`
`python queries/consultar_order_by.py`
`python queries/consultar_or.py`
`python queries/consultar_and.py`