from flask import jsonify, Blueprint

trips_route_bp = Blueprint('trip_routes', __name__)

# Cria uma rota com o endereço /trips
@trips_route_bp.route('/trips', methods=['POST'])
def create_trip():
    return jsonify({'Ola':'mundo'}), 200