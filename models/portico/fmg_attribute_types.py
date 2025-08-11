from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.portico.base import Base


class FmgAttributeType(Base):

    __tablename__ = "fmg_attribute_types"
    __table_args__ = {"schema": "portown"}

    id = Column(Integer, primary_key=True)
    metatype = Column(String, nullable=False)
    description = Column(String, nullable=True)

    provider_attributes = relationship("PPProvAttrib", back_populates="attribute_type")

    def __repr__(self):
        return f"<FmgAttributeType(id={self.id}, metatype={self.metatype}, description={self.description})>"
