from src.model.repositories.interfaces.subscribes_repository_inteface import SubscribersRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscriberCreator:
    def __init__(self, subscriber_repo: SubscribersRepositoryInterface):
        self.__subscriber_repo = subscriber_repo

    def create(self, httpRequest: HttpRequest) -> HttpResponse:
        subscriber_info = httpRequest.body["data"]

        self.__check_subscriber(subscriber_info["email"], subscriber_info["evento_id"])
        self.__insert_subscriber(subscriber_info)

        return self.__format_response(subscriber_info)

    def __check_subscriber(self, subscriber_email: str, subscriber_evento_id: int) -> None:
        response = self.__subscriber_repo.select_subscriber(self= self, email=subscriber_email, evento_id=subscriber_evento_id)
        if response: raise Exception("They Already Subcribed!")

    def __insert_subscriber(self, subcriber_info: dict) -> None:
        response = self.__subscriber_repo.insert(self= self, subscriber_info=subcriber_info)
    
    def __format_response(self, subcriber_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subcriber",
                    "count": 1,
                    "attibutes": subcriber_info
                }
            },
            status_code=201
        )
    