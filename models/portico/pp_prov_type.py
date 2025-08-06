from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base

class PPProvType(Base):

    __tablename__ = 'pp_prov_type'
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)

    providers = relationship("PPProv", back_populates="prov_type")