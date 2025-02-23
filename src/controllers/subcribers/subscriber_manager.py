from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.subscribes_repository_inteface import SubscribersRepositoryInterface

class SubscriberManager:
    def __init__(self, subscriber_repo: SubscribersRepositoryInterface):
        self.__subscriber_repo = subscriber_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.param["link"]
        event_id = http_request.param["event_id"]
        subs = self.__subscriber_repo.select_subscribers_by_link(self=self, link=link, evento_id=event_id)

        return self.__format_subs_by_link(subs)
    
    def get_events_ranking(self, http_request: HttpRequest) -> HttpResponse:
       event_id = http_request.param["event_id"]
       subs_ranking = self.__subscriber_repo.get_ranking(self=self, evento_id=event_id)
       return self.__format_subs_ranking(subs_ranking)

    def __format_subs_ranking(self, subs_ranking: list) -> HttpResponse:
        formatted_subscriber_link = []
        for position in subs_ranking:
            formatted_subscriber_link.append(
                {
                    "link": position.link,
                    "total_inscritos": position.total
                }
            )
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(formatted_subscriber_link),
                    "ranking": formatted_subscriber_link
                }
            },
            status_code=202
        )

    def __format_subs_by_link(self, subs: list) -> HttpResponse:
        formatted_subscriber = []
        for sub in subs:
            formatted_subscriber.append(
                {
                    "nome": sub.nome,
                    "email": sub.email
                }
            )
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(formatted_subscriber),
                    "subscribers": formatted_subscriber
                }
            },
            status_code=202
        )