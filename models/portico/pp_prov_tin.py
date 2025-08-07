from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.portico.base import Base

class PPProvTIN(Base):

    __tablename__ = "pp_prov_tin"
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tin = Column(Integer, nullable=False)

    providers = relationship("PPProv", back_populates="tin")