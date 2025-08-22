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

# class OrganizationRepository:
#
#     def __init__(self, driver:Driver):
#         self.driver = driver
#
#     def get_organization_by_id(self, id):
#         pass
#
#     def get_organization_by_name(self, name):
#         pass
#
#     def get_organization_by_slug(self, slug):
#         pass
#
#     def get_organizations(self):
#         pass
#
#     def create_organization(self, organization:Organization):
#         with open("queries/create_org.cypher", "r") as f:
#             query = f.read()
#         # log.info(f"Organization Name: {organization.name}")
#         # log.info(f"Organization Alias Name: {organization.alias_name}")
#         # log.info(f"Organization Type: {organization.type}")
#         # log.info(f"Organization Description: {organization.description}")
#         # log.info(f"Organization Effective Date: {organization.effective_date}")
#         with self.driver.session() as session:
#             result = session.run(query, org_name=organization.name,
#                                  alias_name=organization.alias_name,
#                                  type=organization.type,
#                                  description=organization.description,
#                                  capitated=organization.capitated,
#                                  atypical=organization.atypical,
#                                  pcp_practitioner_required=organization.pcp_practitioner_required,
#                                  popularity=organization.popularity)
#             # log.info(result)
#             for record in result:
#                 # log.info(record)
#                 org_node = record["org"]
#                 # log.info(org_node["name"])
#                 # log.info(org_node["alias_name"])
#                 # log.info(org_node["type"])
#                 # log.info(org_node["description"])
#                 # log.info(org_node["effective_date"])
#                 # log.info(org_node["capitated"])
#                 # log.info(org_node["sourced_from"])
#         return org_node