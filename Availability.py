from sqlalchemy import JSON, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class Availability(Base):
    __tablename__ = "products_availabilities"

    _id = Column(Integer, primary_key=True)

    url = Column(String, nullable=False)
    code = Column(Integer, nullable=False, server_default="-1")

    price = Column(Float, nullable=False, server_default="-1")
    stock = Column(Boolean, nullable=False, server_default="0")

    product_id = Column(Integer, ForeignKey("products._id"), nullable=False)
    product = relationship("Product", back_populates="availabilities", uselist=False)

    shop_id = Column(Integer, ForeignKey("shops._id"), nullable=False)
    shop = relationship("Shop", back_populates="availabilities", uselist=False)

    outlet = Column(Boolean, nullable=False, server_default="False")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")

    UniqueConstraint(code, shop_id, name="u_code_shop")
    UniqueConstraint(url, name="u_url")
