from db import AtonGraphDB
from models.aton import Organization
from repository import OrganizationRepository, IdentifierRepository


def create_organization(organization:Organization):
    print("Creating organization")
    aton_graph: AtonGraphDB = AtonGraphDB()
    aton_graph.connect()
    org_repo: OrganizationRepository = aton_graph.get_org_repo()
    org_node = org_repo.create_organization(organization)
    for identifier in organization.identifiers:
        print(f"identifier: {identifier.identifier_type} - {identifier.value}")
        identifier_repo: IdentifierRepository = aton_graph.get_identifier_repo()
        identifier_node = identifier_repo.create_identifier(org_node, identifier)
    return organization