from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.controllers.subcribers.subscribers_creator import SubscriberCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

subscriber_route_bp = Blueprint("subscriber_route", __name__)

@subscriber_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subcriber_repo = SubscribersRepository
    subscriber_creator = SubscriberCreator(subcriber_repo)

    http_response = subscriber_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code
