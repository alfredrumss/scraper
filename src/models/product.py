from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str = Field(index=True)
    image: str | None = Field(default=None)
    price: float | None = Field(default=None)
    total_offers: str | None = Field(default=None)
    orders: str | None = Field(default=None)
    product_metadata: str | None = Field(default=None)


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    pass
