from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.customer import Customer
from werkzeug.security import generate_password_hash, check_password_hash
from utils.util import encode_token


def fallback_func(customer_data):
    print('The fallback function is being executed')
    return None

def save(customer_data):
    with Session(db.engine) as session:
        with session.begin():
            customer_query = select(Customer).where(Customer.username == customer_data['username'])
            customer_check = session.execute(customer_query).scalars().first()
            if customer_check is not None:
                raise ValueError("Customer with that username already exists")
            
            new_customer = Customer(
                name=customer_data['name'], 
                email=customer_data['email'], 
                phone=customer_data['phone'], 
                username=customer_data['username'], 
                password=generate_password_hash(customer_data['password'])
                )
            
            session.add(new_customer)
            session.commit()
        session.refresh(new_customer)
        return new_customer

def find_all(page=1, per_page=10):
    query = db.select(Customer).offset((page-1) * per_page).limit(per_page)
    customers = db.session.execute(query).scalars().all()
    return customers

def get_token(username, password):
    query = db.select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalars().first()
    if customer is not None and check_password_hash(customer.password, password):
        auth_token = encode_token(customer.id)
        return auth_token
    else:
        return None

def get_customer(customer_id):
    return db.session.get(Customer, customer_id)

def update(customer_id, customer_data):
    with Session(db.engine) as session:
        customer = session.get(Customer, customer_id)
        if customer:
            for key, value in customer_data.items():
                setattr(customer, key, value)
            session.commit()
            session.refresh(customer)
            return customer
    return None

def delete(customer_id):
    with Session(db.engine) as session:
        customer = session.get(Customer, customer_id)
        if customer:
            session.delete(customer)
            session.commit()
            return True
    return False