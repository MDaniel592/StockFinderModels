from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class NewAvailabilityChannels(Base):
    __tablename__ = "new_availabilities_channels"

    _id = Column(Integer, primary_key=True)

    #
    url = Column(String, nullable=False)
    shop_name = Column(String, nullable=True)
    code = Column(Integer, nullable=True, server_default="-1")
    #
    error_message = Column(String, nullable=True)
    #
    name = Column(String, nullable=True)
    category = Column(String, nullable=True)
    second_name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    part_number = Column(String, nullable=True)
    manufacturer = Column(String, nullable=True)
    #
    processed = Column(Boolean, server_default="False")
    invalid = Column(Boolean, server_default="False")
    counter = Column(Integer, server_default="0")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    UniqueConstraint(url, name="u_url_channel_telegram")
