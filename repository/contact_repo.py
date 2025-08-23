from neo4j import Driver, Transaction
from sqlalchemy.orm import relationship
from repository.relationship_repo import create_relationship
from models.aton import Contact, Address, Telecom
import logging

log = logging.getLogger(__name__)


def create_contact(transaction: Transaction, parent_node, contact: Contact):
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
                        source_node=parent_node,
                        target_node=contact_node,
                        target_node_label=list(contact_node.labels)[0],
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
        create_relationship(transaction=transaction,
                            source_node=contact_node,
                            target_node=address_node,
                            target_node_label=list(address_node.labels)[0],
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
                            target_node_label=list(telecom_node.labels)[0],
                            relationship_type="TELECOM_IS")

