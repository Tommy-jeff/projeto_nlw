from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.controllers.subcribers.subscribers_creator import SubscriberCreator
from src.model.repositories.subscribers_repository import SubscribersRepository
from src.controllers.subcribers.subscriber_manager import SubscriberManager

subscriber_route_bp = Blueprint("subscriber_route", __name__)

@subscriber_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subcriber_repo = SubscribersRepository
    subscriber_creator = SubscriberCreator(subcriber_repo)

    http_response = subscriber_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code


@subscriber_route_bp.route("/subscriber/bylink/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(link, event_id):
    subcriber_repo = SubscribersRepository
    Subscriber_manager = SubscriberManager(subcriber_repo)

    http_request = HttpRequest(param={"link" : link, "event_id": event_id})

    http_response = Subscriber_manager.get_subscribers_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code

@subscriber_route_bp.route("/subscriber/ranking/<event_id>", methods=["GET"])
def subscribers_ranking(event_id):
    subcriber_repo = SubscribersRepository
    Subscriber_manager = SubscriberManager(subcriber_repo)

    http_request = HttpRequest(param={"event_id": event_id})

    http_response = Subscriber_manager.get_events_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code