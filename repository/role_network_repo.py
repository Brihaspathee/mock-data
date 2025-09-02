from neo4j import Transaction
from neo4j.graph import Node
from repository.relationship_repo import create_relationship
from models.aton.role_network import RoleNetwork, RoleLocationServes


def create_role_network(transaction: Transaction,
                         ri_node: Node,
                        net_node: Node) -> Node:
    with open("queries/create_role_nodes.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query,role_label="RoleNetwork", props={})
    for record in result:
        rn_node = record["node"]
        create_relationship(transaction, ri_node, rn_node, "RoleNetwork","SERVES",props={})
        create_relationship(transaction, rn_node, net_node, "Network", "NETWORK_IS",props={})
    return rn_node

def create_rls(transaction: Transaction, rl_node: Node, rn_node: Node, rls:RoleLocationServes):
    create_relationship(transaction, source_node=rl_node, target_node=rn_node,
                        target_node_label="RoleNetwork", relationship_type="ROLE_LOCATION_SERVES",
                        props={
                            "start_date": rls.start_date,
                            "end_date": rls.end_date
                        })