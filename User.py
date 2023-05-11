from sqlalchemy import BIGINT, Boolean, Column, Date, DateTime, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from .base import Base


# Un usuario puede tener solo 1 rol. (¿role_id con  default?)
class User(Base):
    __tablename__ = "users"

    _id = Column(Integer, primary_key=True)

    telegram = Column(BIGINT)
    _email = Column(String)
    password = Column(String)

    role_id = Column(Integer, ForeignKey("roles._id"), nullable=False, server_default="1")
    role = relationship("Role", back_populates="users", uselist=False)

    alerts = relationship("Alert", back_populates="user")
    messages = relationship("Message", back_populates="user")

    password_reseted_at = Column(DateTime, server_default=func.now())
    last_login_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")

    UniqueConstraint(_email, name="u_email")
    UniqueConstraint(telegram, name="u_telegram")
    UniqueConstraint(_email, telegram, name="u_email_telegram")

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email.lower()
