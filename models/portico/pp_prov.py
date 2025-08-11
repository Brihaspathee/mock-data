from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.portico.base import Base

class PPProv(Base):
    __tablename__ = "pp_prov"
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tin_id = Column(String, ForeignKey('portown.pp_prov_tin.id'))
    prov_type_id = Column(String, ForeignKey('portown.pp_prov_type.id'))
    address_id = Column(String, ForeignKey('portown.pp_addr.id'))
    specialty_id = Column(String, ForeignKey('portown.pp_spec.id'))

    tin = relationship("PPProvTIN", back_populates="providers")
    prov_type = relationship("PPProvType", back_populates="providers")
    address = relationship("PPAddr", back_populates="providers")
    specialty = relationship("PPSpec", back_populates="providers")

    addresses = relationship("PPProvAddr", back_populates="providers")

    attributes = relationship("PPProvAttrib", back_populates="provider")
