from neo4j import Transaction
from neo4j.graph import Node, Graph

from models.aton.location import Location
from models.aton.role_location import RoleLocation
from repository.relationship_repo import create_relationship
from aton_writes.service.upsert_location import create_location
import logging

log = logging.getLogger(__name__)


def create_role_location(transaction: Transaction,
                         parent_node: Node,
                         role_location:RoleLocation) -> Node:
    if role_location.location is None:
        raise Exception("Location cannot be None")
    location:Location = role_location.location
    loc_node: Node | None = None
    if location.element_id is None:
        log.info(f"Location element id is None, the location has to be created first")
        loc_node = create_location(transaction, location)
        location.element_id = loc_node.element_id
    else:
        loc_node = Node(Graph(), location.element_id, 0)
    with open("queries/create_role_nodes.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query,role_label="RoleLocation", props={})
    for record in result:
        rl_node = record["node"]
        create_relationship(transaction, parent_node, rl_node, "RoleLocation","PERFORMED_AT", props={})
        create_relationship(transaction, rl_node, loc_node, "Location","LOCATION_IS", props={})
    return rl_node