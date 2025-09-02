from neo4j import Transaction
from neo4j.graph import Node
from repository.relationship_repo import create_relationship
from db.aton_graph_db import get_session
from models.aton.network import Network
import logging

log = logging.getLogger(__name__)


def create_network(transaction: Transaction, parent_node: Node, network: Network) -> Node | None:

    with open("queries/create_network.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, code=network.code,
                           name=network.name,
                           description=network.description)
    for record in result:
        net_node = record["network"]
        create_relationship(transaction, parent_node, net_node, "Network",
                            "PART_OF", props={})
        return net_node
    return None

def match_network(net_code: str):
    with open("queries/match_network.cypher", "r") as f:
        query = f.read()

    with get_session() as session:
        result = session.run(query, network_code=str(net_code))
        record = result.single()
        if record:
            log.info(f"network matched for code {net_code}: {record["network"]}")
            return record["network"]
        else:
            log.info(f"network not found for code: {net_code}")
            return None