from typing import Any

from neo4j import Transaction
import logging

log = logging.getLogger(__name__)


def create_relationship(transaction: Transaction, source_node: Any, target_node: Any, target_node_label: str,
                        relationship_type: str,
                        props:dict[str, Any]) -> None:
    """
    Creates a relationship of a specified type between a source node and a target node in the
    database using a provided transaction.

    This function reads a Cypher query from a file and executes it through a transaction to
    create the relationship. The source and target nodes, along with their labels, must be
    provided. The type of the relationship to establish also needs to be specified.

    :param props:
    :param transaction: Transaction object used to execute the database query.
    :type transaction: Transaction
    :param source_node: The source node involved in the relationship.
    :type source_node: Any
    :param target_node: The target node involved in the relationship.
    :type target_node: Any
    :param target_node_label: The label of the target node, used in the Cypher query.
    :type target_node_label: str
    :param relationship_type: The type of the relationship to create.
    :type relationship_type: str
    :return: None
    """
    # log.info(f"Source node:{source_node.element_id}")
    # log.info(f"Target node:{target_node.element_id}")
    # log.info(f"Source label:{list(source_node.labels)[0]}")
    # log.info(f"Target label:{list(target_node.labels)[0]}")
    with open("queries/create_rels.cypher", "r") as f:
        query = f.read()
        log.info(f"About to create the edge")
        log.info(f"source node labels: {list(source_node.labels)}")
    result = transaction.run(query, source_label=list(source_node.labels)[0],
                         source_element_id=source_node.element_id,
                         target_label=target_node_label,
                         target_element_id=target_node.element_id,
                         rel_type=relationship_type,
                             props=props)