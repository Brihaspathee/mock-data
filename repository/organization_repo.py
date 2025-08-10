from neo4j import Driver
from models.aton import Organization


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
        print(f"Organization Name: {organization.name}")
        print(f"Organization Alias Name: {organization.alias_name}")
        print(f"Organization Type: {organization.type}")
        print(f"Organization Description: {organization.description}")
        print(f"Organization Effective Date: {organization.effective_date}")
        with self.driver.session() as session:
            result = session.run(query, org_name=organization.name,
                                 alias_name=organization.alias_name,
                                 type=organization.type,
                                 description=organization.description,
                                 effective_date=organization.effective_date,
                                 capitated=organization.capitated,
                                 sourced_from=organization.sourced_from)
            print(result)
            for record in result:
                print(record)
                org_node = record["org"]
                print(org_node["name"])
                print(org_node["alias_name"])
                print(org_node["type"])
                print(org_node["description"])
                print(org_node["effective_date"])
                print(org_node["capitated"])
                print(org_node["sourced_from"])
        return org_node