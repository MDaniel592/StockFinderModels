from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class Manufacturer(Base):
    __tablename__ = "manufacturers"

    _id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    UniqueConstraint(name, name="u_manufacturer_name")
