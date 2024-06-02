from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class Cart(Base):
    __tablename__ = 'carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    customer: Mapped["Customer"] = db.relationship(back_populates='carts')

    products: Mapped[List["Product"]] = db.relationship(secondary='cart_product')
