from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.portico.base import Base


class FmgAttributeField(Base):

    __tablename__ = "fmg_attribute_fields"
    __table_args__ = {"schema": "portown"}


    id = Column(Integer, primary_key=True)
    attribute_id = Column(Integer, nullable=False)
    fmgcode = Column(String, nullable=True)
    field_name = Column(String, nullable=False)
    datatype = Column(String, nullable=False)

    values = relationship("PPProvAttribValues", back_populates="field")

    def __repr__(self):
        return f"<FmgAttributeField(id={self.id}, attribute_id={self.attribute_id}, fmgcode={self.fmgcode}, field_name={self.field_name}, datatype={self.datatype})>"