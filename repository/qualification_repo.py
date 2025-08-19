from neo4j import Driver

from models.aton import Qualification
import logging

log = logging.getLogger(__name__)

class QualificationRepository:
    def __init__(self, driver:Driver):
        self.driver = driver

    def create_qualification(self, org_node, qualification:Qualification):
        with open("queries/create_qualification.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, type=qualification.qualification_type,
                                 value=qualification.value,
                                 start_date=qualification.start_date,
                                 end_date=qualification.end_date,
                                 sourced_from=qualification.sourced_from)
            # log.info(result)
            for record in result:
                # log.info(record)
                qual_node = record["qual"]
                # log.info(tin_node["legalName"])
                labels = list(qual_node.labels)
                # log.info(labels)
        self.create_relationship(org_node, qual_node)

    def create_relationship(self, org_node, qual_node):
        with open("queries/org_rel_qualification.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, org_element_id=org_node.element_id,
                                 qual_element_id=qual_node.element_id)
            # log.info(result)
