from flask import Blueprint
from controllers.cartController import add_item_to_cart, remove_item_from_cart, update_item_quantity, get_cart, empty_cart, create_cart

cart_blueprint = Blueprint('cart_bp', __name__)
cart_blueprint.route('/create', methods=['POST'])(create_cart)
cart_blueprint.route('/add-item', methods=['POST'])(add_item_to_cart)
cart_blueprint.route('/remove-item', methods=['DELETE'])(remove_item_from_cart)
cart_blueprint.route('/update-quantity', methods=['PUT'])(update_item_quantity)
cart_blueprint.route('/', methods=['GET'])(get_cart)
cart_blueprint.route('/empty', methods=['DELETE'])(empty_cart)