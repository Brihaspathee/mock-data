from neo4j import Driver, Transaction
from sqlalchemy.orm import relationship

from models.aton import Contact, Address, Telecom
import logging

log = logging.getLogger(__name__)


def create_contact(transaction: Transaction, org_node, contact: Contact):
    with open("queries/create_contact.cypher", "r") as f:
        query = f.read()
    # with self.driver.session() as session:
    result = transaction.run(query, use=contact.use)
    # log.info(f"Results is: {result}")
    for record in result:
        # log.info(f"Record: {record}")
        contact_node = record["contact"]
        # log.info(f"Contact node: {contact_node}")
        create_relationship(transaction=transaction,
                        source_node=org_node,
                        target_node=contact_node,
                        relationship_type="HAS_ORGANIZATIONAL_CONTACT")
        if contact.address is not None:
            create_address(transaction=transaction,
                           contact_node=contact_node,
                           address=contact.address)
        if contact.telecom is not None:
            create_telecom(transaction=transaction,
                           contact_node=contact_node,
                           telecom=contact.telecom)
        return contact_node
    return None


def create_address(transaction: Transaction, contact_node, address: Address):
    with open("queries/create_address.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, street_address=address.street_address,
                         secondary_address=address.secondary_address,
                         city=address.city,
                         state=address.state,
                         zip=address.zip_code,
                         county=address.county,
                         fips=address.fips,
                         latitude=address.latitude,
                         longitude=address.longitude)
    for record in result:
        address_node = record["address"]
        create_relationship(transaction= transaction,
                            source_node=contact_node,
                            target_node=address_node,
                            relationship_type="ADDRESS_IS")


def create_telecom(transaction: Transaction,  contact_node, telecom: Telecom):
    with open("queries/create_telecom.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, phone=telecom.phone,
                         fax=telecom.fax,
                         tty=telecom.tty,
                         after_hours_number=telecom.after_hours_number,
                         email=telecom.email,
                         secure_email=telecom.secure_email,
                         website=telecom.website)
    for record in result:
        telecom_node = record["telecom"]
        create_relationship(transaction=transaction,
                            source_node=contact_node,
                            target_node=telecom_node,
                            relationship_type="TELECOM_IS")


def create_relationship(transaction: Transaction,  source_node, target_node, relationship_type):
    # log.info(f"Source node:{source_node.element_id}")
    # log.info(f"Target node:{target_node.element_id}")
    # log.info(f"Source label:{list(source_node.labels)[0]}")
    # log.info(f"Target label:{list(target_node.labels)[0]}")
    with open("queries/create_rels.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, source_label=list(source_node.labels)[0],
                         source_element_id=source_node.element_id,
                         target_label=list(target_node.labels)[0],
                         target_element_id=target_node.element_id,
                         rel_type=relationship_type)

# class ContactRepository:
#
#     def __init__(self, driver:Driver):
#         self.driver = driver
#
#     def create_contact(self, org_node, contact:Contact):
#         with open("queries/create_contact.cypher", "r") as f:
#             query = f.read()
#         with self.driver.session() as session:
#             result = session.run(query, use=contact.use)
#             # log.info(f"Results is: {result}")
#             for record in result:
#                 # log.info(f"Record: {record}")
#                 contact_node = record["contact"]
#                 # log.info(f"Contact node: {contact_node}")
#         self.create_relationship(org_node, contact_node, "HAS_ORGANIZATIONAL_CONTACT")
#         if contact.address is not None:
#             self.create_address(contact_node, contact.address)
#         if contact.telecom is not None:
#             self.create_telecom(contact_node, contact.telecom)
#         return contact_node
#
#
#     def create_address(self, contact_node, address:Address):
#         with open("queries/create_address.cypher", "r") as f:
#             query = f.read()
#         with self.driver.session() as session:
#             result = session.run(query, street_address=address.street_address,
#                                  secondary_address=address.secondary_address,
#                                  city=address.city,
#                                  state=address.state,
#                                  zip=address.zip_code,
#                                  county=address.county,
#                                  fips=address.fips,
#                                  latitude=address.latitude,
#                                  longitude=address.longitude )
#             for record in result:
#                 address_node = record["address"]
#         self.create_relationship(contact_node, address_node, "ADDRESS_IS")
#
#
#     def create_telecom(self, contact_node, telecom:Telecom):
#         with open("queries/create_telecom.cypher", "r") as f:
#             query = f.read()
#         with self.driver.session() as session:
#             result = session.run(query, phone=telecom.phone,
#                                  fax=telecom.fax,
#                                  tty=telecom.tty,
#                                  after_hours_number=telecom.after_hours_number,
#                                  email=telecom.email,
#                                  website=telecom.website)
#             for record in result:
#                 telecom_node = record["telecom"]
#         self.create_relationship(contact_node, telecom_node, "TELECOM_IS")
#
#     def create_relationship(self, source_node, target_node, relationship_type):
#         # log.info(f"Source node:{source_node.element_id}")
#         # log.info(f"Target node:{target_node.element_id}")
#         # log.info(f"Source label:{list(source_node.labels)[0]}")
#         # log.info(f"Target label:{list(target_node.labels)[0]}")
#         with open("queries/create_rels.cypher", "r") as f:
#             query = f.read()
#         with self.driver.session() as session:
#             result = session.run(query, source_label=list(source_node.labels)[0],
#                                  source_element_id=source_node.element_id,
#                                  target_label=list(target_node.labels)[0],
#                                  target_element_id=target_node.element_id,
#                                  rel_type = relationship_type)