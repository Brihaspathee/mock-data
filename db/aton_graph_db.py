from neo4j import GraphDatabase
from config import settings
from repository import OrganizationRepository, IdentifierRepository
from repository.address_repo import AddressRepository
from repository.contact_repo import ContactRepository
from repository.qualification_repo import QualificationRepository


# from py2neo import Graph, database


class AtonGraphDB:
    def __init__(self):
        self.driver = None

    def connect(self):
        # define_env()
        # secrets = fetch_secrets()
        # print(secrets)
        self.driver = GraphDatabase.driver(settings.NEO4J["url"],
                              auth=(settings.NEO4J["username"],settings.NEO4J["password"]),
                              database=settings.NEO4J["database"])
        # graph = Graph(secrets["ss.neo4j.url"],
        #               auth=(secrets["ss.neo4j.username"],secrets["ss.neo4j.password"]),
        #               database=secrets["ss.neo4j.database"])
        self.driver.verify_connectivity()
        return self.driver

    def close(self):
        self.driver.close()

    def get_org_repo(self):
        return OrganizationRepository(self.driver)

    def get_identifier_repo(self):
        return IdentifierRepository(self.driver)

    def get_qualification_repo(self):
        return QualificationRepository(self.driver)

    def get_contact_repo(self):
        return ContactRepository(self.driver)

    def get_address_repo(self):
        return AddressRepository(self.driver)





