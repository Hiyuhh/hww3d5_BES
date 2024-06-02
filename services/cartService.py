from models.cart import Cart
from models.cartProduct import cart_product
from models.product import Product
from database import db
from sqlalchemy.orm import Session

def get_cart(cart_id):
    return db.session.get(Cart, cart_id)

def create_cart(customer_id):
    with Session(db.engine) as session:
        cart = Cart(customer_id=customer_id)
        session.add(cart)
        session.commit()
        return cart

def add_item_to_cart(cart_id, product_id, quantity):
    with Session(db.engine) as session:
        cart = session.get(Cart, cart_id)
        product = session.get(Product, product_id)
        if product is None:
            raise ValueError("Product not found")
        if cart is None:
            raise ValueError("Cart not found")
        cart.products.append(product)
        session.commit()

def remove_item_from_cart(cart_id, product_id):
    with Session(db.engine) as session:
        cart = session.get(Cart, cart_id)
        product = session.get(Product, product_id)
        if product is None:
            raise ValueError("Product not found")
        if cart is None:
            raise ValueError("Cart not found")
        cart.products.remove(product)
        session.commit()

def update_item_quantity(cart_id, product_id, quantity):
    with Session(db.engine) as session:
        cart = session.get(Cart, cart_id)
        product = session.get(Product, product_id)
        if product is None:
            raise ValueError("Product not found")
        if cart is None:
            raise ValueError("Cart not found")
        cart_product_query = db.select(cart_product).where(cart_product.c.cart_id == cart_id).where(cart_product.c.product_id == product_id)
        cart_product_row = session.execute(cart_product_query).first()
        if cart_product_row is None:
            raise ValueError("Product not found in cart")
        cart_product_row.quantity = quantity
        session.commit()

def empty_cart(cart_id):
    with Session(db.engine) as session:
        cart = session.get(Cart, cart_id)
        if cart is None:
            raise ValueError("Cart not found")
        cart.products = []
        session.commit()

