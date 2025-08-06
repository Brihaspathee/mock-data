from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class PP_PHONES(Base):

    __tablename__ = "pp_phones"
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    area_code = Column(String, nullable=False)
    exchange = Column(String, nullable=False)
    number = Column(String, nullable=False)

    addresses = relationship('PP_ADDR_PHONES', back_populates='phone')