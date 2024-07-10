from flask import jsonify, Blueprint, request

trips_route_bp = Blueprint('trip_routes', __name__)

# Importação de controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinCreator

# Importação de repositorios
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository



# Importação do gerente de conexões
from src.models.settings.db_connection_handler import db_connection_handler

# Cria uma rota com o endereço /trips
@trips_route_bp.route('/trips', methods=['POST'])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)


    return jsonify(response['body']), response['status_code']

@trips_route_bp.route('/trips/<tripId>', methods=['GET'])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.fin_trip_details(tripId)
    
    return jsonify(response['body']), response['status_code']

@trips_route_bp.route('/trips/<tripId>/confirm', methods=['GET'])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)

    response = controller.confirm(tripId)

    return jsonify(response['body']), response['status_code']

@trips_route_bp.route('/trips/<tripId>/confirm', methods=['POST'])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinCreator(links_repository)

    response = controller.create(request.json, tripId)

    return jsonify(response['body']), response['status_code']
