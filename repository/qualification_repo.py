from neo4j import Driver, Transaction
from repository.relationship_repo import create_relationship
from models.aton import Qualification
import logging

log = logging.getLogger(__name__)


def create_qualification(transaction: Transaction, parent_node, qualification: Qualification):
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

