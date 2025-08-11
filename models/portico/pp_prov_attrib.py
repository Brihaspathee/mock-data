from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.portico.base import Base


class PPProvAttrib(Base):

    __tablename__ = "pp_prov_attrib"
    __table_args__ = {"schema": "portown"}

    id = Column(Integer, primary_key=True)
    prov_id = Column(Integer, ForeignKey("portown.pp_prov.id"))
    attribute_id = Column(Integer, ForeignKey("portown.fmg_attribute_types.id"))

    provider = relationship("PPProv", back_populates="attributes")
    values = relationship("PPProvAttribValues", back_populates="provider_attribute")
    attribute_type = relationship("FmgAttributeType", back_populates="provider_attributes")

    def __repr__(self):
        return f"<PPProvAttrib(id={self.id}, prov_id={self.prov_id}, attribute_id={self.attribute_id})>"