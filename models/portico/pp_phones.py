from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.portico.base import Base

class PPPhones(Base):

    __tablename__ = "pp_phones"
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    area_code = Column(String, nullable=False)
    exchange = Column(String, nullable=False)
    number = Column(String, nullable=False)

    addresses = relationship('PPAddrPhones', back_populates='phone')