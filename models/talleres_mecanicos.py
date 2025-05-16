from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from SQLAlchemy.db import Base

class TalleresMecanicos(Base):
    __tablename__ = 'talleres_mecanicos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String, nullable=False)

    vehiculos = relationship("Vehiculos", back_populates="taller")

    def __repr__(self):
        return f"TalleresMecanicos(nombre={self.nombre}, direccion={self.direccion})"
