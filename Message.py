from email.policy import default

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class Message(Base):
    __tablename__ = "messages"

    _id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users._id"), nullable=False)
    user = relationship("User", back_populates="messages", uselist=False)

    message_telegram = Column(String)
    message_telegram_counter = Column(Integer, nullable=False, server_default="0")
    message_email = Column(String)
    message_email_counter = Column(Integer, nullable=False, server_default="0")
    message_thread_id = Column(Integer, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")

    UniqueConstraint(user_id, message_telegram, message_email, name="u_user_messages")
    CheckConstraint("NOT(message_telegram IS NULL AND message_email IS NULL)")
