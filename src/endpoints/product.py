from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette import status

from src.contrib.db_setup import get_session
from src.models.product import Product, ProductCreate
from src.repositories.product import get_products, post_product

router = APIRouter(
    tags=["products"],
)


@router.get(
    "/products",
    response_model=List[Product],
    status_code=status.HTTP_200_OK,
)
def get_all_products(session: Session = Depends(get_session)) -> List[Product]:
    return get_products(session=session)


@router.post(
    "/products",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    product: ProductCreate, session: Session = Depends(get_session)
) -> Product:
    product = Product.model_validate(product)
    return post_product(product=product, session=session)
