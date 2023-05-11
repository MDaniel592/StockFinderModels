from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class Shop(Base):
    __tablename__ = "shops"

    _id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    availabilities = relationship("Availability", back_populates="shop")

    UniqueConstraint(name, name="u_shop_name")
