from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class EventosLink(Base):
    __tablename__ = "Eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey("Eventos.id", ondelete=True, onupdate=True), nullable=False,)
    inscrito_id = Column(Integer, ForeignKey("Inscritos.id", ondelete=True, onupdate=True), nullable=False)
    link = Column(String, nullable=False)