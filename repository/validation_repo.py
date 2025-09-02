from neo4j import Transaction
from neo4j.graph import Node

from models.aton.validation import Validation
from repository.relationship_repo import create_relationship


def create_validation(transaction: Transaction,
                         parent_node: Node,
                      validation:Validation) -> Node:
    with open("queries/create_validation.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query,type=validation.type,
                             source=validation.source,
                             key=validation.key)
    for record in result:
        validation_node = record["validation"]
        create_relationship(transaction, parent_node, validation_node,
                            "Validation",
                            "VALIDATED", props={})
    return validation_node