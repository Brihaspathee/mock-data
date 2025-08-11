from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.portico.base import Base


class PPProvAttribValues(Base):

    __tablename__ = "pp_prov_attrib_values"
    __table_args__ = {"schema": "portown"}

    id = Column(Integer, primary_key=True)
    prov_attribute_id = Column(Integer, ForeignKey("portown.pp_prov_attrib.id"))
    field_id = Column(Integer, ForeignKey("portown.fmg_attribute_fields.id"))
    value = Column(String, nullable=True)
    value_date = Column(Date, nullable=True)
    value_number = Column(Numeric, nullable=True)

    provider_attribute = relationship("PPProvAttrib", back_populates="values")
    field = relationship("FmgAttributeField", back_populates="values")

    def __repr__(self):
        return (f"<PPProvAttribValues(id={self.id}, prov_attribute_id={self.prov_attribute_id}, field_id={self.field_id}, "
                f"value={self.value}, value_date={self.value_date}, value_number={self.value_number})>")