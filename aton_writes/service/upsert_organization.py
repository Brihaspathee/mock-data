from neo4j import Session, Driver, Transaction

from db import AtonGraphDB
from db.neo4j_transaction_manager import Neo4jTransactionManager
from models.aton import Organization
from repository import OrganizationRepository, QualificationRepository, identifier_repo
from repository import organization_repo
import logging

from repository.contact_repo import ContactRepository

log = logging.getLogger(__name__)

def create_organization(driver: Driver, organization:Organization):
    transaction_manager = Neo4jTransactionManager(driver=driver)
    try:
        transaction_manager.execute_transaction(create_org, organization)
        log.info("Transaction successful")
        log.info("Organization {} created".format(organization.name))
    except Exception as e:
        log.error("Transaction failed: {}".format(e))
    finally:
        driver.close()

def create_org(transaction: Transaction, organization: Organization):
    org_node = organization_repo.create_org(transaction, organization)
    for identifier in organization.identifiers:
        identifier_repo.create_identifier(transaction=transaction, org_node=org_node, identifier=identifier)

# def create_organization(organization:Organization):
#     log.info("Creating organization")
#     aton_graph: AtonGraphDB = AtonGraphDB()
#     aton_graph.connect()
#     org_repo: OrganizationRepository = aton_graph.get_org_repo()
#     org_node = org_repo.create_organization(organization)
#     for identifier in organization.identifiers:
#         log.info(f"identifier: {identifier.identifier_type} - {identifier.value}")
#         identifier_repo: IdentifierRepository = aton_graph.get_identifier_repo()
#         identifier_node = identifier_repo.create_identifier(org_node, identifier)
#     log.info(f"Creating qualifications: {organization.qualifications}")
#     for qualification in organization.qualifications:
#         log.info(f"qualification: {qualification.qualification_type} - {qualification.value}")
#         qualification_repo: QualificationRepository = aton_graph.get_qualification_repo()
#         qualification_node = qualification_repo.create_qualification(org_node, qualification)
#     for contact in organization.contacts:
#         log.info(f"Contact: {contact.use}")
#         contact_repo: ContactRepository = aton_graph.get_contact_repo()
#         contact_node = contact_repo.create_contact(org_node, contact)
#     return organization