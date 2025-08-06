from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class PPAddrPhones(Base):
    __tablename__ = "PP_ADDR_PHONES"
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    address_id = Column(Integer, ForeignKey('portown.pp_addr.id'))
    phone_id = Column(Integer, ForeignKey('portown.pp_phones.id'))

    address = relationship("PPAddr", back_populates="phones")
    phone = relationship("PPPhones", back_populates="addresses")
