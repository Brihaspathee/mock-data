from sqlalchemy import alias

from models.aton.neomodel.identifier import Identifier, TIN
from models.aton.neomodel.organization import Organization
from transform.neomodel.transformers import transform_to_aton
import logging

from models.portico import PPProv

log = logging.getLogger(__name__)

@transform_to_aton.register(PPProv)
def _(provider:PPProv) -> Organization:
    organization = Organization(name=provider.name)
    organization.description = provider.name
    organization.type = provider.prov_type.type
    organization.capitate = False
    organization.pcp_practitioner_required = False
    organization.atypical = False
    return organization

def get_tin(provider:PPProv) -> Identifier:
    tin: TIN = TIN(value= provider.tin.tin,
                   legal_name = provider.tin.name)
    return tin