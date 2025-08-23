from neo4j import Driver, Transaction
from models.aton import Organization
import logging

log = logging.getLogger(__name__)

def create_org(tx: Transaction, org: Organization):
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
