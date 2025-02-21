from src.model.configs.connection import DbConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribes_repository_inteface import SubscribersRepository

class SubscribersRepository():
    def insert(self, subscriber_info: dict) -> None:
        with DbConnectionHandler() as db:
            try:
                new_subscriber = Inscritos(
                    nome=subscriber_info.get("name"),
                    email=subscriber_info.get("email"),
                    link=subscriber_info.get("link"),
                    evento_id=subscriber_info.get("evento_id"),
                    )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DbConnectionHandler() as db:
            data = (
                db.session.query(Inscritos)
                .filter(
                    Inscritos.email == email,
                    Inscritos.evento_id == evento_id)
                .limit(1)
                .one_or_none()
            )

            return data
        
    def delete_subscriber(self, id: int) -> int:
        with DbConnectionHandler() as db:
            try:
                delete_subcriber = db.session.get_one(
                    Inscritos, 
                    id
                    )

                db.session.delete(delete_subcriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
