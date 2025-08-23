from neo4j import Driver, Transaction
from models.aton import Organization
import logging

log = logging.getLogger(__name__)


def create_org(tx: Transaction, org: Organization) -> object | None:
    """
    Creates an organization node in the database using the provided transaction
    and organization object. The Cypher query is read from a file and executed
    using the attributes of the organization object as parameters.

    :param tx: The open transaction to the database for executing the query.
               Must implement the required ``run`` method with query support.
    :param org: An instance of the ``Organization`` class. Provides the details
                of the organization such as name, alias, type, description,
                and other related attributes.
    :return: The created organization node if successful, otherwise ``None``.
    :rtype: Any
    """
    with open("queries/create_org.cypher", "r") as f:
        query = f.read()
    result = tx.run(query, org_name=org.name,
                                 alias_name=org.alias_name,
                                 type=org.type,
                                 description=org.description,
                                 capitated=org.capitated,
                                 atypical=org.atypical,
                                 pcp_practitioner_required=org.pcp_practitioner_required,
                                 popularity=org.popularity)
    for record in result:
        org_node = record["org"]
        return org_node
    return None
