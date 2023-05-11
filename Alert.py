from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from .base import Base


# Un usuario puede tener una alerta por disponibilidad (url de tienda concreta) o por producto (conjunto de url)
# Esta posibilidad debería estar limitada por el rol del usuario
class Alert(Base):
    __tablename__ = "alerts"

    _id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users._id"), nullable=False)
    user = relationship("User", back_populates="alerts", uselist=False)

    product_id = Column(Integer, ForeignKey("products._id"), nullable=True)
    product = relationship("Product", uselist=False)

    availability_id = Column(Integer, ForeignKey("products_availabilities._id"), nullable=True)
    availability = relationship("Availability", uselist=False)

    spec_id = Column(Integer, ForeignKey("specs._id"), nullable=True)
    spec = relationship("Spec", uselist=False)
    spec_value = Column(String)

    max_price = Column(Float, nullable=False)
    alert_by_telegram = Column(Boolean, server_default="False")
    alert_by_email = Column(Boolean, server_default="False")

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")

    UniqueConstraint(user_id, product_id, availability_id, name="u_user_product_availability")
    CheckConstraint("NOT(product_id IS NULL AND availability_id IS NULL)")
