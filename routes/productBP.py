from flask import Blueprint
from controllers.productController import save, find_all, update_product, delete_product, find_by_id

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/<int:product_id>', methods=['GET'])(find_by_id)
product_blueprint.route('/<int:product_id>', methods=['PUT'])(update_product)
product_blueprint.route('/<int:product_id>', methods=['DELETE'])(delete_product)