from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base

class PPSpec(Base):
    __tablename__ = "pp_spec"
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    description = Column(String, nullable=True)
    site_visit_req = Column(String, nullable=True)

    providers = relationship("PPProv", back_populates="specialty")