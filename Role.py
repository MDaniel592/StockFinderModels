from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


class Role(Base):
    __tablename__ = "roles"

    _id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    priority = Column(Integer, server_default="0")

    DEFAULT_NUMBER = "10"
    max_watches = Column(Integer, nullable=False, server_default=DEFAULT_NUMBER)
    max_builds = Column(Integer, nullable=False, server_default=DEFAULT_NUMBER)
    users = relationship("User", back_populates="role")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")

    UniqueConstraint(name, name="u_role_name")
    UniqueConstraint(priority, name="u_priority")
    UniqueConstraint(name, priority, name="u_name_priority")
