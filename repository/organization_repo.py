from neo4j import Driver
from models import Organization


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
        with self.driver.session() as session:
            result = session.run(query, org_name=organization.name,
                                 alias_name=organization.alias_name,
                                 description=organization.description,
                                 effective_date=organization.effective_date,
                                 capitated=organization.capitated,
                                 sourced_from=organization.sourced_from)
            print(result)
            for record in result:
                print(record)
