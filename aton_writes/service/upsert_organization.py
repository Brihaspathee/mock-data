from neo4j import Session, Driver, Transaction
from neo4j.graph import Node, Graph

import models
from db.neo4j_transaction_manager import Neo4jTransactionManager
from models.aton import Organization
from models.aton.role_location import RoleLocation
from repository import organization_repo, qualification_repo, identifier_repo, contact_repo
from aton_writes.service.upsert_role_instance import create_ri
from aton_writes.service.upsert_role_location import create_rl
from aton_writes.service.upsert_role_network import create_rn
import logging

log = logging.getLogger(__name__)

def create_organization(organization:Organization):
    transaction_manager = Neo4jTransactionManager()
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
        contact_repo.create_contact(transaction=transaction, parent_node=org_node, contact=contact, relationship_type="HAS_ORGANIZATIONAL_CONTACT")
    for roleInstance in organization.roleInstances:
        # log.info(f"There are role instances:{roleInstance}")
        ri_node: Node = create_ri(transaction=transaction, parent_node=org_node, ri=roleInstance)
        for role_location in roleInstance.roleLocations:
            rl_node: Node = create_rl(transaction=transaction, parent_node=ri_node, role_location=role_location)
            # log.info(f"There are role locations:{role_location}")
        for role_network in roleInstance.roleNetworks:
            rn_node: Node = create_rn(transaction=transaction, ri_node=ri_node, role_network=role_network)
            log.info(f"There are role networks:{role_network}")
            # for associated_location in role_network.associated_locations:
            #     log.info(f"There are associated locations:{associated_location}")
            #     role_location: RoleLocation = associated_location.roleLocation
            #     rl_node: Node = Node(Graph(), role_location.element_id, 0)
            #     for role_location_serve in associated_location.role_location_serves:
            #         log.info(f"There are role location serves:{role_location_serve}")
    return org_node
