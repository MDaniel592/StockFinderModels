from itertools import product

from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class ProductPartNumber(Base):
    __tablename__ = "product_part_numbers"

    product_id = Column(Integer, ForeignKey("products._id"), primary_key=True)
    product = relationship("Product", back_populates="product_part_numbers")

    part_number = Column(String, nullable=False, primary_key=True)

    UniqueConstraint(product_id, part_number, name="u_p_partnumber")
