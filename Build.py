import uuid

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import Base


class Build(Base):
    __tablename__ = "builds"

    _id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String)

    DEFAULT_UPVOTES = "0"
    upvotes = Column(Integer, server_default=DEFAULT_UPVOTES)

    DEFAULT_PRICE = "0"
    #
    cpu_price = Column(Float, server_default=DEFAULT_PRICE)

    cpu_id = Column(Integer, ForeignKey("products._id"))
    cpu = relationship("Product", foreign_keys=cpu_id, uselist=False)
    cpu_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    cpu_availability = relationship("Availability", foreign_keys=cpu_availability_id, uselist=False)
    #
    cooler_price = Column(Float, server_default=DEFAULT_PRICE)

    cooler_id = Column(Integer, ForeignKey("products._id"))
    cooler = relationship("Product", foreign_keys=cooler_id, uselist=False)
    cooler_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    cooler_availability = relationship("Availability", foreign_keys=cooler_availability_id, uselist=False)
    #
    motherboard_price = Column(Float, server_default=DEFAULT_PRICE)

    motherboard_id = Column(Integer, ForeignKey("products._id"))
    motherboard = relationship("Product", foreign_keys=motherboard_id, uselist=False)
    motherboard_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    motherboard_availability = relationship("Availability", foreign_keys=motherboard_availability_id, uselist=False)
    #
    gpu_price = Column(Float, server_default=DEFAULT_PRICE)

    gpu_id = Column(Integer, ForeignKey("products._id"))
    gpu = relationship("Product", foreign_keys=gpu_id, uselist=False)
    gpu_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    gpu_availability = relationship("Availability", foreign_keys=gpu_availability_id, uselist=False)
    #
    case_price = Column(Float, server_default=DEFAULT_PRICE)

    case_id = Column(Integer, ForeignKey("products._id"))
    case = relationship("Product", foreign_keys=case_id, uselist=False)
    case_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    case_availability = relationship("Availability", foreign_keys=case_availability_id, uselist=False)
    #
    ram_price = Column(Float, server_default=DEFAULT_PRICE)

    ram_id = Column(Integer, ForeignKey("products._id"))
    ram = relationship("Product", foreign_keys=ram_id, uselist=False)
    ram_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    ram_availability = relationship("Availability", foreign_keys=ram_availability_id, uselist=False)
    #
    primary_storage_price = Column(Float, server_default=DEFAULT_PRICE)

    primary_storage_id = Column(Integer, ForeignKey("products._id"))
    primary_storage = relationship("Product", foreign_keys=primary_storage_id, uselist=False)
    primary_storage_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    primary_storage_availability = relationship("Availability", foreign_keys=primary_storage_availability_id, uselist=False)
    #
    secondary_storage_price = Column(Float, server_default=DEFAULT_PRICE)

    secondary_storage_id = Column(Integer, ForeignKey("products._id"))
    secondary_storage = relationship("Product", foreign_keys=secondary_storage_id, uselist=False)
    secondary_storage_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    secondary_storage_availability = relationship("Availability", foreign_keys=secondary_storage_availability_id, uselist=False)
    #
    psu_price = Column(Float, server_default=DEFAULT_PRICE)

    psu_id = Column(Integer, ForeignKey("products._id"))
    psu = relationship("Product", foreign_keys=psu_id, uselist=False)
    psu_availability_id = Column(Integer, ForeignKey("products_availabilities._id"))
    psu_availability = relationship("Availability", foreign_keys=psu_availability_id, uselist=False)
    #

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, server_default="False")
