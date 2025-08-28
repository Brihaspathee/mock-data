from sqlalchemy import ForeignKey, Column, Integer, Boolean
from sqlalchemy.orm import relationship


class PPProvLoc:

    __tablename__ = "pp_prov_loc"
    __table_args__ = {"schema": "portown"}

    prov_id = Column(Integer, ForeignKey("portown.pp_prov.id"))
    loc_id = Column(Integer, ForeignKey("portown.pp_prov_tin_loc.id"))
    primary = Column(Boolean, default=False)

    provider = relationship("PPProv", back_populates="locations")
    location = relationship("PPProvTINLoc")

    def __repr__(self):
        return (
            f"<PPProvLoc(prov_id={self.prov_id}, loc_id={self.loc_id}, primary={self.primary})>"
        )