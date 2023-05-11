from sqlalchemy import BIGINT, Boolean, Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class TelegramChannel(Base):
    __tablename__ = "telegram_channels"

    _id = Column(Integer, primary_key=True)

    channel_name = Column(String, nullable=False)
    telegram = Column(BIGINT, nullable=False)
    max_price = Column(Float, nullable=False)
    message_thread_id = Column(Integer, nullable=True)

    spec_id = Column(Integer, ForeignKey("specs._id"), nullable=False)
    spec = relationship("Spec", uselist=False)
    product_spec_value = Column(String, nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")

    UniqueConstraint(telegram, spec_id, product_spec_value, name="u_telegram_spec_id_product_spec_value")
