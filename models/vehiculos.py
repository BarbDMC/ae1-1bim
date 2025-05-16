from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from SQLAlchemy.db import Base

class Vehiculos(Base):
    __tablename__ = 'vehiculos'

    id = Column(Integer, primary_key=True)
    placa = Column(String, nullable=False, unique=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    anio_fabricacion = Column(Integer, nullable=False)
    taller_id = Column(Integer, ForeignKey('talleres_mecanicos.id'))

    taller = relationship("TalleresMecanicos", back_populates="vehiculos")
    servicios = relationship("Servicios", back_populates="vehiculo")

    def __repr__(self):
        return f"Vehiculos(placa={self.placa}, marca={self.marca}, modelo={self.modelo})"
