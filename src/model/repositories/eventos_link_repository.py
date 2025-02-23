from src.model.configs.connection import DbConnectionHandler
from src.model.entities.eventos_link import EventosLink
from .interfaces.eventos_link_repository_interface import EventosLinkRepositoryInterface
import random

class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, evento_id: int, inscrito_id: int) -> str:
        with DbConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices('0123456789', k=7))
                formatted_link= f'evento-{evento_id}-{inscrito_id}-{link_final}'

                new_event_link = EventosLink(
                    link=formatted_link,
                    evento_id = evento_id,
                    inscrito_id= inscrito_id
                    )
                db.session.add(new_event_link)
                db.session.commit()

                return formatted_link
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_event_link(self, evento_id: int, inscrito_id: int) -> EventosLink:
        with DbConnectionHandler() as db:
            data = (
                db.session
                .query(EventosLink)
                .filter(
                    EventosLink.inscrito_id == inscrito_id,
                    EventosLink.evento_id == evento_id
                    )
                    .limit(1)
                    .one_or_none()
            )
            return data

    def delete(self, event_link_id: int) -> int:
        with DbConnectionHandler() as db:
            try:
                delete_event_link = db.session.get_one(
                    EventosLink, 
                    event_link_id
                    )
                db.session.delete(delete_event_link)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
