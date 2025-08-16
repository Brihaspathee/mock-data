from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.portico.base import Base

class PPProvType(Base):
    """
    Represents a type of provider with its associated category. This class is linked
    to the `PPProv` table via a relationship, serving as a way to categorize
    providers.

    This class maps to the `pp_prov_type` table in the `portown` schema.

    Purpose:
    - To store provider type details, including type and category.
    - To define relationships between provider types and corresponding providers.

    :ivar id: Unique identifier for the provider type.
    :type id: int
    :ivar type: The type of the provider (e.g., 'ISP', 'Hosting').
    :type type: str
    :ivar category: The category of the provider type (e.g., 'Communication',
        'Technology').
    :type category: str
    :ivar providers: A list of associated providers that belong to this provider
        type.
    :type providers: list[PPProv]
    """
    __tablename__ = 'pp_prov_type'
    __table_args__ = {'schema': 'portown'}

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)

    # providers = relationship("PPProv", back_populates="prov_type")