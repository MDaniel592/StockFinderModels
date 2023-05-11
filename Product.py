import uuid
from email.policy import default

from sqlalchemy import JSON, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Product(Base):
    __tablename__ = "products"

    _id = Column(Integer, primary_key=True)

    # part_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    short_name = Column(String, nullable=True)

    category_id = Column(Integer, ForeignKey("categories._id"), nullable=False)
    category = relationship("Category", foreign_keys="Product.category_id", uselist=False)

    manufacturer_id = Column(Integer, ForeignKey("manufacturers._id"), nullable=False)
    manufacturer = relationship("Manufacturer", uselist=False)

    product_specs = relationship("ProductSpec", back_populates="product")
    availabilities = relationship("Availability", back_populates="product")
    product_part_numbers = relationship("ProductPartNumber", back_populates="product")

    refurbished = Column(Boolean, nullable=False, server_default="False")
    images = Column(JSON)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")

    manufacturer_data = Column(Boolean, server_default="False")

    # UniqueConstraint(part_number, name="u_partnumber")
    UniqueConstraint(uuid, name="u_uuid")
