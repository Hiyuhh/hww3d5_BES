from database import db

cart_product = db.Table(
    "cart_product",
    db.Column('product_id', db.ForeignKey('products.id'), primary_key=True),
    db.Column('cart_id', db.ForeignKey('carts.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False)
)