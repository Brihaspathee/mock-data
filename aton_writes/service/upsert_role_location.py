import logging

from neo4j import Transaction
from neo4j.graph import Node

from models.aton import Contact
from repository import role_location_repo,contact_repo
from models.aton.role_location import RoleLocation

log = logging.getLogger(__name__)



def create_rl(transaction: Transaction, parent_node:Node, role_location:RoleLocation):
    rl_node = role_location_repo.create_role_location(transaction, parent_node, role_location=role_location)
    role_location.element_id = rl_node.element_id
    for contact in role_location.contacts:
        log.info(f"There are contacts:{contact}")
        log.info(f"Data for telecom node:{contact.telecom}")
        log.info(f"Phone number:{contact.telecom.phone}")
        contact_repo.create_contact(transaction=transaction, parent_node=rl_node, contact=contact, relationship_type="HAS_LOCATION_CONTACT")
    return rl_node
