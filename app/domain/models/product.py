# app/domain/models/product.py
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class ProductBase(SQLModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int

class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    # Relación 1 a muchos con Cart: cada producto pertenece a un carrito
    cart_id: Optional[int] = Field(default=None, foreign_key="cart.id")
    cart: Optional["Cart"] = Relationship(back_populates="products")


class ProductCreate(ProductBase):
    cart_id: Optional[int] = None  # al crear un producto, puede asignarse a un carrito

class ProductRead(ProductBase):
    id: int
    cart_id: Optional[int] = None

class ProductUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    cart_id: Optional[int] = None
