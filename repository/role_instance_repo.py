from neo4j import Transaction
from neo4j.graph import Node
from repository.relationship_repo import create_relationship
from models.aton.role_instance import RoleInstance


def create_role_instance(transaction: Transaction,
                         parent_node: Node) -> Node:
    with open("queries/create_role_nodes.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query,role_label="RoleInstance", props={})
    for record in result:
        ri_node = record["node"]
        create_relationship(transaction, parent_node, ri_node,
                            "RoleInstance",
                            "HAS_ROLE", props={})
    return ri_node