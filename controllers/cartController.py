from flask import request, jsonify
from schemas.cartSchema import cart_schema
from services import cartService
from auth import token_auth

@token_auth.login_required
def create_cart():
    customer_id = token_auth.current_user().id
    try:
        cartService.create_cart(customer_id)
        return jsonify({'message': 'Shopping cart created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@token_auth.login_required
def add_item_to_cart():
    customer_id = token_auth.current_user().id
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    if not product_id or not quantity:
        return jsonify({'error': 'Missing product_id or quantity'}), 400
    try:
        quantity = int(quantity)
    except ValueError:
        return jsonify({'error': 'Invalid quantity value'}), 400
    try:
        cartService.add_item_to_cart(customer_id, product_id, quantity)
        cart = cartService.get_cart(customer_id)
        return cart_schema.jsonify(cart), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@token_auth.login_required
def remove_item_from_cart():
    customer_id = token_auth.current_user().id
    product_id = request.json.get('product_id')

    if not product_id:
        return jsonify({'error': 'Missing product_id'}), 400
    try:
        cartService.remove_item_from_cart(customer_id, product_id)
        cart = cartService.get_cart(customer_id)
        return cart_schema.jsonify(cart), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@token_auth.login_required
def update_item_quantity():
    customer_id = token_auth.current_user().id
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')

    if not product_id or not quantity:
        return jsonify({'error': 'Missing product_id or quantity'}), 400
    try:
        quantity = int(quantity)
    except ValueError:
        return jsonify({'error': 'Invalid quantity value'}), 400
    try:
        cartService.update_item_quantity(customer_id, product_id, quantity)
        cart = cartService.get_cart(customer_id)
        return cart_schema.jsonify(cart), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@token_auth.login_required
def get_cart():
    customer_id = token_auth.current_user().id
    try:
        cart = cartService.get_cart(customer_id)
        if cart:
            return cart_schema.jsonify(cart), 200
        else:
            return jsonify({'message': 'Shopping cart is empty'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@token_auth.login_required
def empty_cart():
    customer_id = token_auth.current_user().id
    try:
        cartService.empty_cart(customer_id)
        return jsonify({'message': 'Shopping cart emptied'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500