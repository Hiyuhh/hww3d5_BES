from flask import request, jsonify
from schemas.customerSchema import customer_input_schema, customer_output_schema, customers_schema, customer_login_schema
from services import customerService
from marshmallow import ValidationError


def save():
    try:
        customer_data = customer_input_schema.load(request.json)
        customer_save = customerService.save(customer_data)
        return customer_output_schema.jsonify(customer_save), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({"error": str(err)}), 400


def find_all():
    args = request.args
    page = args.get('page', 1, type=int)
    per_page = args.get('per_page', 10, type=int)
    customers = customerService.find_all(page, per_page)
    return customers_schema.jsonify(customers), 200


def get_token():
    try:
        customer_data = customer_login_schema.load(request.json)
        token = customerService.get_token(customer_data['username'], customer_data['password'])
        if token:
            resp = {
                "status": "success",
                "message": "You have successfully logged in",
                "token": token
            }
            return jsonify(resp), 200
        else:
            resp = {
                "status": "error",
                "message": "Username and/or password is incorrect"
            }
            return jsonify(resp), 401
    except ValidationError as err:
        return jsonify(err.messages), 400


def get_customer(customer_id):
    customer = customerService.get_customer(customer_id)
    if customer:
        return customer_output_schema.jsonify(customer)
    else:
        resp = {
            "status": "error",
            "message": f'A customer with ID {customer_id} does not exist'
        }
        return jsonify(resp), 404
    

def update_customer(customer_id):
    try:
        customer_data = customer_input_schema.load(request.json)
        customer = customerService.update_customer(customer_id, customer_data)
        return customer_output_schema.jsonify(customer), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({"error": str(err)}), 400
    

def delete_customer(customer_id):
    customer = customerService.delete_customer(customer_id)
    if customer:
        return customer_output_schema.jsonify(customer)
    else:
        resp = {
            "status": "error",
            "message": f'A customer with ID {customer_id} does not exist'
        }
        return jsonify(resp), 404