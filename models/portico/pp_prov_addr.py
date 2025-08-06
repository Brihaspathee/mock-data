from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base

class PPProvAddr(Base):
    __tablename__ = "pp_prov_addr"
    __table_args__ = {"schema": "portown"}

    id = Column(Integer, primary_key=True)
    prov_id = Column(Integer, ForeignKey("portown.pp_prov.id"))
    address_id = Column(Integer, ForeignKey("portown.pp_addr.id"))

    provider = relationship("PPProv", back_populates="addresses")
    address = relationship("PPProvAddr", back_populates="provider_address")