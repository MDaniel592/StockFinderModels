from itertools import product

from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class ProductSpec(Base):
    __tablename__ = "product_specs"

    product_id = Column(Integer, ForeignKey("products._id"), primary_key=True)
    product = relationship("Product", back_populates="product_specs")

    spec_id = Column(Integer, ForeignKey("specs._id"), primary_key=True)
    spec = relationship("Spec", back_populates="spec_value", uselist=False)

    value = Column(String, nullable=False)
