from src.model.configs.connection import DbConnectionHandler
from src.model.entities.eventos import Eventos

class EventosRepository:
    def insert(self, event_name: str) -> None:
        with DbConnectionHandler() as db:
            try:
                new_event = Eventos(nome=event_name)
                db.session.add(new_event)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_event(self, event_name: str) -> Eventos:
        with DbConnectionHandler() as db:
            data = (
                db.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .limit(1)
                .one_or_none()
            )
            return data

    # def delete(self, event_id: int) -> int:
    #     with DbConnectionHandler() as db:
    #         try:
    #             delete_event = Eventos(id=event_id)
    #             db.session.delete(Eventos)
    #             db.session.commit()
    #         except Exception as exception:
    #             db.session.rollback()
    #             raise exception
