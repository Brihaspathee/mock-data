from neo4j import Driver

from models.aton import Contact, Address, Telecom
import logging

log = logging.getLogger(__name__)

class ContactRepository:

    def __init__(self, driver:Driver):
        self.driver = driver

    def create_contact(self, org_node, contact:Contact):
        with open("queries/create_contact.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, use=contact.use)
            log.info(f"Results is: {result}")
            for record in result:
                log.info(f"Record: {record}")
                contact_node = record["contact"]
                log.info(f"Contact node: {contact_node}")
        self.create_contact_relationship(org_node, contact_node)
        if contact.address is not None:
            self.create_address(contact_node, contact.address)
        return contact_node

    def create_contact_relationship(self, org_node, contact_node):
        log.info(f"Org node:{org_node.element_id}")
        log.info(f"Contact node:{contact_node.element_id}")
        with open("queries/org_rel_contact.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, org_element_id=org_node.element_id,
                                 contact_element_id=contact_node.element_id)

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
                self.create_address_relationship(contact_node, address_node)

    def create_address_relationship(self, contact_node, address_node):
        with open("queries/contact_rel_address.cypher", "r") as f:
            query = f.read()
        with self.driver.session() as session:
            result = session.run(query, contact_element_id=contact_node.element_id,
                                 address_element_id=address_node.element_id)