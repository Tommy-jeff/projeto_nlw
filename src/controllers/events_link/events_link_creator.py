from src.model.repositories.interfaces.eventos_link_repository_interface import EventosLinkRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventsLinkCreator:
    def __init__(self, events_link_repo: EventosLinkRepositoryInterface):
        self.__events_link_repo = events_link_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
       events_link_info = http_request.body["data"]
       event_id = events_link_info["evento_id"]
       subs_id = events_link_info["inscrito_id"]

       self.__check_event(event_id, subs_id)
       event_link = self.__insert_event(event_id, subs_id)
       return self.__format_response(event_link)

    def __check_event(self, event_id: int, subs_id: int) -> None:
        response = self.__events_link_repo.select_event_link(event_id, subs_id)
        if response: raise Exception("Event link Already exists!")

    def __insert_event(self, event_id: int, subs_id: int) -> int:
        event_link = self.__events_link_repo.insert(event_id, subs_id)
        return event_link
    def __format_response(self, event_link: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Event_link",
                    "count": 1,
                    "attibutes": {
                        "event_link": event_link
                    }
                }
            },
            status_code=201
        )