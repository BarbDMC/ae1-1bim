from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from SQLAlchemy.db import Base

class Servicios(Base):
    __tablename__ = 'servicios'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String, nullable=False)
    costo = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id'))

    vehiculo = relationship("Vehiculos", back_populates="servicios")

    def __repr__(self):
        return f"Servicios(descripcion={self.descripcion}, costo={self.costo}, fecha={self.fecha})"
