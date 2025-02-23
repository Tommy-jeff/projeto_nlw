from src.model.entities.inscritos import Inscritos
from abc import ABC, abstractmethod

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_info: dict) -> None: pass

    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos: pass

    @abstractmethod
    def select_subscribers_by_link(self, link: str, evento_id: int) -> list: pass

    @abstractmethod 
    def get_ranking(self, evento_id: int) -> list: pass

    @abstractmethod
    def delete_subscriber(self, id: int) -> int: pass
