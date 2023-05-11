from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class NewAvailability(Base):
    __tablename__ = "new_availabilities"

    _id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)

    url = Column(String, nullable=False)
    max_price = Column(Float, nullable=False, server_default="-1")

    alert_by_telegram = Column(Boolean, server_default="False")
    alert_by_email = Column(Boolean, server_default="False")

    processed = Column(Boolean, server_default="False")
    invalid = Column(Boolean, server_default="False")
    counter = Column(Integer, server_default="0")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    UniqueConstraint(user_id, url, name="u_user_url")
