from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from models.portico.base import Base

class PPProvAddr(Base):
    """
    Represents the association between providers and addresses.

    This class maps the relationship between a provider and its associated
    address in the database. It is part of the `portown` schema and uses the
    SQLAlchemy ORM for database interactions. Each instance of this class links
    a provider to an address and defines the relationships between the data
    models for provider and address entities.

    :ivar id: Unique identifier for the provider-address association.
    :type id: int
    :ivar prov_id: Identifier linking to the associated provider.
    :type prov_id: int
    :ivar address_id: Identifier linking to the associated address.
    :type address_id: int
    :ivar providers: Relationship to the `PPProv` model.
    :type providers: sqlalchemy.orm.RelationshipProperty
    :ivar address: Relationship to the `PPAddr` model.
    :type address: sqlalchemy.orm.RelationshipProperty
    """
    __tablename__ = "pp_prov_addr"
    __table_args__ = {"schema": "portown"}

    id = Column(Integer, primary_key=True)
    prov_id = Column(Integer, ForeignKey("portown.pp_prov.id"))
    address_id = Column(Integer, ForeignKey("portown.pp_addr.id"))

    providers = relationship("PPProv", back_populates="addresses")
    address = relationship("PPAddr", back_populates="provider_address")