from typing import Any

from neo4j import Transaction


def create_relationship(transaction: Transaction,
                        source_node: Any,
                        target_node: Any,
                        target_node_label: str,
                        relationship_type: str) -> None:
    # log.info(f"Source node:{source_node.element_id}")
    # log.info(f"Target node:{target_node.element_id}")
    # log.info(f"Source label:{list(source_node.labels)[0]}")
    # log.info(f"Target label:{list(target_node.labels)[0]}")
    with open("queries/create_rels.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, source_label=list(source_node.labels)[0],
                         source_element_id=source_node.element_id,
                         target_label=target_node_label,
                         target_element_id=target_node.element_id,
                         rel_type=relationship_type)