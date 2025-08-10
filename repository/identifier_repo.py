from neo4j import Driver

from models.aton import Identifier, Organization

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

    def create_npi_identifier(self, org_node, npi_identifier:Identifier):
        """
        Creates an NPI (National Provider Identifier) node in the database, establishes a relationship
        between the given organizational node and the created NPI node, and returns the created NPI node.

        This function reads a Cypher query from a file, executes it with the provided identifier's data,
        and iterates over the resulting records to extract the created NPI node.

        :param org_node: The organizational node used as the source for creating a relationship
                         with the NPI node.
        :type org_node: any
        :param npi_identifier: The identifier object containing the value, start date, end date, and
                               sourcing information to create the NPI node in the database.
        :type npi_identifier: Identifier
        :return: The NPI node created in the database, containing its attributes such as value,
                 start date, end date, source information, labels, and element ID.
        :rtype: Node
        """
        with open("queries/create_npi.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, value=npi_identifier.value,
                                 start_date=npi_identifier.startDate,
                                 end_date=npi_identifier.endDate,
                                 sourced_from=npi_identifier.sourced_from)
            # print(result)
            for record in result:
                # print(record)
                npi_node = record["npi"]
                # print(npi_node["value"])
                # print(npi_node["startDate"])
                # print(npi_node["endDate"])
                # print(npi_node["sourced_from"])
                # print(npi_node.element_id)
                labels = list(npi_node.labels)
                # print(labels)
        self.create_relationship(org_node, npi_node)
        return npi_node

    def create_identifier(self, org_node, identifier:Identifier):
        if identifier.identifierType == "NPI":
            self.create_npi_identifier(org_node, identifier)

    def create_relationship(self, org_node, identifier_node):
        with open("queries/org_rel_identifier.cypher", "r") as f:
            rel_query = f.read()
        with self.driver.session() as session:
            rel_result = session.run(rel_query, org_element_id=org_node.element_id,
                                 npi_element_id=identifier_node.element_id)
            # print(rel_result)
