from src.model.entities.eventos_link import EventosLink
from abc import ABC, abstractmethod

class EventosLinkRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, event_link: str, evento_id: int, inscrito_id: int) -> None: pass
    
    @abstractmethod
    def select_event_link(self, event_link: str, evento_id: int, inscrito_id: int) -> EventosLink: pass

    @abstractmethod
    def delete(self, event_link_id: int) -> int: pass
