from neo4j import Transaction
from neo4j.graph import Node

from db.neo4j_transaction_manager import Neo4jTransactionManager
from models.aton.role_instance import RoleInstance
from repository import role_instance_repo
import logging

log = logging.getLogger(__name__)



def create_ri(transaction: Transaction, parent_node:Node, ri:RoleInstance) -> Node | None:
    ri_node = role_instance_repo.create_role_instance(transaction, parent_node)
    ri.element_id = ri_node.element_id
    return ri_node