from neo4j import Driver, Transaction

from models.aton import Qualification
import logging

log = logging.getLogger(__name__)


def create_qualification(transaction: Transaction, org_node, qualification: Qualification):
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
        create_relationship(transaction=transaction, source_node=org_node,
                            target_node=qual_node, relationship_type="HAS_QUALIFICATION")


def create_relationship(transaction: Transaction, source_node, target_node, relationship_type):
    # with open("queries/org_rel_qualification.cypher", "r") as f:
    #     query = f.read()
    # log.info(f"Qualification Source node:{source_node.element_id}")
    # log.info(f"Qualification Target node:{target_node.element_id}")
    # log.info(f"Qualification Source label:{list(source_node.labels)[0]}")
    # log.info(f"Qualification Target label:{list(target_node.labels)[0]}:{list(target_node.labels)[1]}")
    with open("queries/create_rels.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, source_label=list(source_node.labels)[0],
                         source_element_id=source_node.element_id,
                         target_label=f"{list(target_node.labels)[0]}:{list(target_node.labels)[1]}",
                         target_element_id=target_node.element_id,
                         rel_type=relationship_type)
        # log.info(result)

# class QualificationRepository:
#     def __init__(self, driver:Driver):
#         self.driver = driver
#
#     def create_qualification(self, org_node, qualification:Qualification):
#         with open("queries/create_qualification.cypher", "r") as f:
#             query = f.read()
#         with self.driver.session() as session:
#             result = session.run(query, type=qualification.qualification_type,
#                                  value=qualification.value,
#                                  start_date=qualification.start_date,
#                                  end_date=qualification.end_date,
#                                  sourced_from=qualification.sourced_from)
#             # log.info(result)
#             for record in result:
#                 # log.info(record)
#                 qual_node = record["qual"]
#                 labels = list(qual_node.labels)
#                 # log.info(labels)
#         self.create_relationship(org_node, qual_node, "HAS_QUALIFICATION")
#
#     def create_relationship(self, source_node, target_node,relationship_type):
#         # with open("queries/org_rel_qualification.cypher", "r") as f:
#         #     query = f.read()
#         # log.info(f"Qualification Source node:{source_node.element_id}")
#         # log.info(f"Qualification Target node:{target_node.element_id}")
#         # log.info(f"Qualification Source label:{list(source_node.labels)[0]}")
#         # log.info(f"Qualification Target label:{list(target_node.labels)[0]}:{list(target_node.labels)[1]}")
#         with open("queries/create_rels.cypher", "r") as f:
#             query = f.read()
#         with self.driver.session() as session:
#             result = session.run(query, source_label=list(source_node.labels)[0],
#                                  source_element_id=source_node.element_id,
#                                  target_label=f"{list(target_node.labels)[0]}:{list(target_node.labels)[1]}",
#                                  target_element_id=target_node.element_id,
#                                  rel_type=relationship_type)
#             # log.info(result)
