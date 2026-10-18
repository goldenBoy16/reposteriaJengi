from reposteria.database import PkModel, Column
from reposteria.reposteria.user import models
from reposteria.tests.conftest import db

class Categoria(PkModel):
    __tablename__ = 'categorias'
    nombre = Column(db.String(100), nullable=False, unique=True)
    descripcion = Column(db.String(100), nullable=False, unique=True)

    def __str__(self) -> str:
        return f"Categoria(nombre={self.nombre}, descripcion={self.descripcion})"