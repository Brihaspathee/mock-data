from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from models.portico.base import Base

class PPAddr(Base):
    __tablename__ = 'pp_addr'
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    addr1 = Column(String, nullable=False)
    addr2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    county = Column(String, nullable=True)
    fips = Column(String, nullable=True)
    latitude = Column(String, nullable=True)
    longitude = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)


    providers = relationship("PPProv", back_populates="address")
    phones = relationship("PPAddrPhones", back_populates="address")
    provider_address = relationship("PPProvAddr", back_populates="address")
