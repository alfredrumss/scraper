from typing import List

from sqlmodel import Session, select

from src.models.product import Product


def post_product(session: Session, product: Product) -> Product:
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def get_products(session: Session) -> List[Product]:
    return session.exec(select(Product)).all()  # type: ignore
