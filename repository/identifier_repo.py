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

    def create_tax_identifier(self, org_node, tax_identifier:Identifier):
        with open("queries/create_tin.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, value=tax_identifier.value,
                                 legal_name=tax_identifier.legal_name,
                                 sourced_from=tax_identifier.sourced_from)
            # print(result)
            for record in result:
                # print(record)
                tin_node = record["tin"]
                # print(tin_node["legalName"])
                labels = list(tin_node.labels)
                # print(labels)
        self.create_relationship(org_node, tin_node, "TIN", "HAS_TIN")
        return tin_node

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
                                 start_date=npi_identifier.start_date,
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
        self.create_relationship(org_node, npi_node, "NPI", "HAS_NPI")
        return npi_node

    def create_identifier(self, org_node, identifier:Identifier):
        if identifier.identifier_type == "NPI":
            print(f"Creating NPI Identifier with start date: {identifier.start_date}")
            self.create_npi_identifier(org_node, identifier)
        elif identifier.identifier_type == "TIN":
            print(f"Creating TIN Identifier {identifier.value} with legal name: {identifier.legal_name}")
            self.create_tax_identifier(org_node, identifier)

    def create_relationship(self, org_node, identifier_node, identifier_label, relationship_label):
        with open("queries/create_rel_identifier.cypher", "r") as f:
            rel_query = f.read()
        with self.driver.session() as session:
            rel_result = session.run(rel_query, parent_labels="Organization",
                                     parent_element_id = org_node.element_id,
                                     identifier_labels=f"Identifier:{identifier_label}",
                                     identifier_element_id=identifier_node.element_id,
                                     rel_type=relationship_label)

        # if "NPI" in identifier_node.labels:
        #     with open("queries/org_rel_identifier_1.cypher", "r") as f:
        #         rel_query = f.read()
        #     with self.driver.session() as session:
        #         rel_result = session.run(rel_query, org_element_id=org_node.element_id,
        #                              npi_element_id=identifier_node.element_id)
        #         # print(rel_result)
        # elif "TIN" in identifier_node.labels:
        #     with open("queries/org_rel_identifier_2.cypher", "r") as f:
        #         rel_query = f.read()
        #     with self.driver.session() as session:
        #         rel_result = session.run(rel_query, org_element_id=org_node.element_id,
        #                              tin_element_id=identifier_node.element_id)

        # id_label = f"{identifier_label}:Identifier"
        # print(f"Organization Node element Id is {org_node.element_id}")
        # print(f"Identifier Node element Id is {identifier_node.element_id}")
        # print(f"Identifier label is {id_label}")
        # org_match_query = """
        # MATCH (o) WHERE elementId(o) = $parent_element_id RETURN labels(o), elementId(o)
        # """
        # with self.driver.session() as session:
        #     rel_result = session.run(org_match_query,
        #                              parent_element_id = org_node.element_id)
        #     for record in rel_result:
        #         print(record)
        #         print(record["labels(o)"])
        #         print(record["elementId(o)"])
        #
        # id_match_query = """
        #         MATCH (o) WHERE elementId(o) = $identifier_element_id RETURN labels(o), elementId(o)
        #         """
        # with self.driver.session() as session:
        #     id_rel_result = session.run(id_match_query,
        #                              identifier_element_id=identifier_node.element_id)
        #     for record in id_rel_result:
        #         print(record)
        #         print(record["labels(o)"])
        #         print(record["elementId(o)"])
