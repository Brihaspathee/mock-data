from neo4j import Driver, Transaction
from neo4j.graph import Node
from sqlalchemy.orm import relationship
from repository.relationship_repo import create_relationship
from models.aton import Contact, Address, Telecom
import logging

log = logging.getLogger(__name__)


def create_contact(transaction: Transaction, parent_node: Node, contact: Contact) -> Node | None:
    """
    Creates a contact node in the database and establishes its relationships and associated
    information, such as address and telecom, if applicable.

    :param transaction: A Neo4j database transaction object used to run the Cypher query.
    :param parent_node: The parent node to which the contact node relationship is established.
    :param contact: An instance representing the contact information to be added.
    :return: The created contact Node if successful, otherwise None.
    """
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


def create_address(transaction: Transaction, contact_node: Node, address: Address) -> None:
    """
    Creates an address node in the database and establishes a relationship
    between the contact node and the created address node. This function
    reads a Cypher query from a file, executes it with the provided
    address details, and establishes the relationship using the address'
    label.

    :param transaction: Transaction object used to run the Cypher query.
    :type transaction: Transaction
    :param contact_node: Node object representing the contact.
    :type contact_node: Node
    :param address: Address object containing details of the address to
        be created in the database.
    :type address: Address
    :return: None
    """
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


def create_telecom(transaction: Transaction, contact_node: Node, telecom: Telecom) -> None:
    """
    Creates a telecom entity in the database and establishes a relationship between a contact node
    and the newly created telecom node. This function reads a Cypher query from an external file,
    executes it to create or retrieve the telecom node, and then creates a relationship of type
    "TELECOM_IS" between the contact node and the created telecom node.

    :param transaction: The Neo4j transaction instance used to execute database queries.
    :type transaction: Transaction
    :param contact_node: The contact node to which the created telecom node will be linked.
    :type contact_node: Node
    :param telecom: An instance of the Telecom class containing details such as phone, fax,
        tty, after-hours number, email, secure email, and website used to populate the
        telecom node.
    :type telecom: Telecom
    :return: This function does not return a value.
    :rtype: None
    """
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

