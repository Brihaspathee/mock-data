from neo4j import Driver

from models.aton import Identifier, Organization
import logging

log = logging.getLogger(__name__)

"""
This module contains the logic for creating and managing identifiers
for organizations."""
class IdentifierRepository:

    """
    Represents a repository for handling identifier-related operations
    with a database driver session.

    This class is designed to manage the creation and association of
    identifiers, specifically NPIs (National Provider Identifiers), with
    organizational nodes. It provides functionality to execute necessary
    database queries and establish relevant relationships between entities.

    :ivar driver: The database driver used for establishing sessions and
                  executing queries.
    :type driver: Driver
    """

    def __init__(self, driver:Driver):
        self.driver = driver

    def create_identifier(self, org_node, identifier:Identifier):
        with open("queries/create_identifier.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, identifier_label=identifier.identifier_label,
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
        self.create_relationship(org_node, identifier_node, identifier.identifier_label, identifier.identifier_rel)
        # if identifier.identifier_type == "NPI":
        #     log.info(f"Creating NPI Identifier with start date: {identifier.start_date}")
        #     # self.create_npi_identifier(org_node, identifier)
        #     self.create_relationship(org_node, identifier_node, "NPI", "HAS_NPI")
        # elif identifier.identifier_type == "TIN":
        #     log.info(f"Creating TIN Identifier {identifier.value} with legal name: {identifier.legal_name}")
        #     # self.create_tax_identifier(org_node, identifier)
        #     self.create_relationship(org_node, identifier_node, "TIN", "HAS_TIN")
        # elif identifier.identifier_type == "MedicareID":
        #     self.create_relationship(org_node, identifier_node, "MedicareID", "HAS_MEDICARE_ID")

    def create_relationship(self, org_node, identifier_node, identifier_label, relationship_label):
        # with open("queries/delete_create_rel_identifier.cypher", "r") as f:
        #     rel_query = f.read()
        # log.info(f"Relationship Source node:{org_node.element_id}")
        # log.info(f"Relationship Target node:{identifier_node.element_id}")
        with open("queries/create_rels.cypher", "r") as f:
            rel_query = f.read()
        with self.driver.session() as session:
            rel_result = session.run(rel_query, source_label="Organization",
                                     source_element_id = org_node.element_id,
                                     target_label=f"Identifier:{identifier_label}",
                                     target_element_id=identifier_node.element_id,
                                     rel_type=relationship_label)

