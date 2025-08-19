from neo4j import Driver

from models.aton import Address
import logging

class AddressRepository:

    def __init__(self, driver:Driver):
        self.driver = driver

    def create_address(self, contact_node, address:Address):
        with open("queries/create_address.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, street_address=address.street_address,
                                 secondary_address=address.secondary_address,
                                 city=address.city,
                                 state=address.state,
                                 zip=address.zip_code,
                                 county=address.county,
                                 fips=address.fips,
                                 latitude=address.latitude,
                                 longitude=address.longitude )
            for record in result:
                address_node = record["address"]
                self.create_relationship(contact_node, address_node)

    def create_relationship(self, contact_node, address_node):
        with open("queries/contact_rel_address.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, contact_element_id=contact_node.element_id,
                                 address_element_id=address_node.element_id)
