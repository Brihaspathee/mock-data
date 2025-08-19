from db import AtonGraphDB
from models.aton import Organization
from repository import OrganizationRepository, IdentifierRepository,QualificationRepository
import logging

from repository.address_repo import AddressRepository
from repository.contact_repo import ContactRepository

log = logging.getLogger(__name__)


def create_organization(organization:Organization):
    log.info("Creating organization")
    aton_graph: AtonGraphDB = AtonGraphDB()
    aton_graph.connect()
    org_repo: OrganizationRepository = aton_graph.get_org_repo()
    org_node = org_repo.create_organization(organization)
    for identifier in organization.identifiers:
        log.info(f"identifier: {identifier.identifier_type} - {identifier.value}")
        identifier_repo: IdentifierRepository = aton_graph.get_identifier_repo()
        identifier_node = identifier_repo.create_identifier(org_node, identifier)
    log.info(f"Creating qualifications: {organization.qualifications}")
    for qualification in organization.qualifications:
        log.info(f"qualification: {qualification.qualification_type} - {qualification.value}")
        qualification_repo: QualificationRepository = aton_graph.get_qualification_repo()
        qualification_node = qualification_repo.create_qualification(org_node, qualification)
    for contact in organization.contacts:
        log.info(f"Contact: {contact.use}")
        contact_repo: ContactRepository = aton_graph.get_contact_repo()
        contact_node = contact_repo.create_contact(org_node, contact)
    return organization