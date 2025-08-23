from neo4j import Driver, Transaction
from repository.relationship_repo import create_relationship
from models.aton import Identifier, Organization
import logging

log = logging.getLogger(__name__)

"""
This module contains the logic for creating and managing identifiers
for organizations."""


def create_identifier(transaction: Transaction, parent_node: any, identifier: Identifier) -> None:
    """
    Executes a Cypher query to create an identifier node in the database and establishes a
    relationship with the provided parent node.

    :param transaction: The transaction object used to execute the Cypher query.
        It facilitates communication with the database to ensure the operation is
        executed within a transactional context.
    :type transaction: Transaction
    :param parent_node: The node with which the identifier node is to be connected.
    :type parent_node: any
    :param identifier: The identifier object containing details such as label,
        value, start date, end date, legal name, and the relationship type to
        establish with the parent node.
    :type identifier: Identifier
    :return: None.
    """
    with open("queries/create_identifier.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, identifier_label=identifier.identifier_label,
                         value=identifier.value,
                         start_date=identifier.start_date,
                         end_date=identifier.end_date,
                         legal_name=identifier.legal_name)
    # log.info(result)
    for record in result:
        # log.info(record)
        identifier_node = record["node"]
        # log.info(tin_node["legalName"])
        labels = list(identifier_node.labels)
        # log.info(labels)
        create_relationship(transaction, parent_node, identifier_node, f"Identifier:{identifier.identifier_label}",
                            identifier.identifier_rel)



