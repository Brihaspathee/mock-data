from neo4j import Session, Driver, Transaction

from db import AtonGraphDB
from db.neo4j_transaction_manager import Neo4jTransactionManager
from models.aton import Organization
from repository import organization_repo, qualification_repo, identifier_repo, contact_repo
import logging

log = logging.getLogger(__name__)

def create_organization(db:AtonGraphDB, organization:Organization):
    transaction_manager = Neo4jTransactionManager(db=db)
    try:
        transaction_manager.execute_transaction(create_org, organization)
        log.info("Transaction successful")
        log.info("Organization {} created".format(organization.name))
    except Exception as e:
        log.error("Transaction failed: {}".format(e))
    finally:
        log.info("Transaction completed")

def create_org(transaction: Transaction, organization: Organization):
    org_node = organization_repo.create_org(transaction, organization)
    for identifier in organization.identifiers:
        identifier_repo.create_identifier(transaction=transaction, parent_node=org_node, identifier=identifier)
    for qualification in organization.qualifications:
        qualification_repo.create_qualification(transaction=transaction, parent_node=org_node, qualification=qualification)
    for contact in organization.contacts:
        contact_repo.create_contact(transaction=transaction, parent_node=org_node, contact=contact)
    return org_node