import sys

from flask import jsonify
from app.models import Address
from app import bp

# API route to query addresses on /api/addresses/x
@bp.route('/addresses/<int:id>', methods=['GET'])
def get_address(id):
    return jsonify(Address.query.get_or_404(id).to_dict())

# API route to query all addresses
@bp.route('/addresses', methods=['GET'])
def get_addresses():
    addresses = []
    for a in Address.query.all():
        try:
            print(a.to_dict(), sys.stderr)
            addresses.append(a.to_dict())
        except Exception as e:
            print(e, sys.stderr)
    return jsonify(addresses)