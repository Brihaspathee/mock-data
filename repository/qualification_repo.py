from neo4j import Driver, Transaction
from repository.relationship_repo import create_relationship
from models.aton import Qualification
import logging

log = logging.getLogger(__name__)


def create_qualification(transaction: Transaction, parent_node: object, qualification: Qualification) -> None:
    """
    Creates a qualification node in the database and establishes a relationship between
    a parent node and the created qualification node. The function processes the query
    for the creation of the qualification node using provided information from a
    Qualification object. It also establishes a "HAS_QUALIFICATION" relationship
    between the parent node and the created qualification node.

    :param transaction: The database transaction in which the operation is executed.
                        It is used to interact with the graph database.
    :type transaction: Transaction
    :param parent_node: The parent node object to which the qualification will be linked.
    :type parent_node: object
    :param qualification: An instance of the Qualification class that contains
                          details of the qualification that needs to be created.
    :type qualification: Qualification
    :return: This function does not return any value; it performs database operations.
    :rtype: None
    """
    with open("queries/create_qualification.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query,
                             type=qualification.qualification_type,
                             value=qualification.value,
                             issuer=qualification.issuer,
                             state=qualification.state,
                             status=qualification.status,
                             level=qualification.level,
                             specialty=qualification.specialty,
                             start_date=qualification.start_date,
                             end_date=qualification.end_date)
    # log.info(result)
    for record in result:
        # log.info(record)
        qual_node = record["qual"]
        labels = list(qual_node.labels)
        # log.info(labels)
        create_relationship(transaction=transaction,
                            source_node=parent_node,
                            target_node=qual_node,
                            target_node_label = f"{list(qual_node.labels)[0]}:{list(qual_node.labels)[1]}",
                            relationship_type="HAS_QUALIFICATION")

