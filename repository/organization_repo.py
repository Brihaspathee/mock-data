from neo4j import Driver
from models.aton import Organization
import logging

log = logging.getLogger(__name__)


class OrganizationRepository:

    def __init__(self, driver:Driver):
        self.driver = driver

    def get_organization_by_id(self, id):
        pass

    def get_organization_by_name(self, name):
        pass

    def get_organization_by_slug(self, slug):
        pass

    def get_organizations(self):
        pass

    def create_organization(self, organization:Organization):
        with open("queries/create_org.cypher", "r") as f:
            query = f.read()
        log.info(f"Organization Name: {organization.name}")
        log.info(f"Organization Alias Name: {organization.alias_name}")
        log.info(f"Organization Type: {organization.type}")
        log.info(f"Organization Description: {organization.description}")
        log.info(f"Organization Effective Date: {organization.effective_date}")
        with self.driver.session() as session:
            result = session.run(query, org_name=organization.name,
                                 alias_name=organization.alias_name,
                                 type=organization.type,
                                 description=organization.description,
                                 effective_date=organization.effective_date,
                                 capitated=organization.capitated,
                                 sourced_from=organization.sourced_from)
            log.info(result)
            for record in result:
                log.info(record)
                org_node = record["org"]
                log.info(org_node["name"])
                log.info(org_node["alias_name"])
                log.info(org_node["type"])
                log.info(org_node["description"])
                log.info(org_node["effective_date"])
                log.info(org_node["capitated"])
                log.info(org_node["sourced_from"])
        return org_node