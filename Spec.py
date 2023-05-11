from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from .base import Base


class Spec(Base):
    __tablename__ = "specs"

    _id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    spec_value = relationship("ProductSpec", back_populates="spec")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")
