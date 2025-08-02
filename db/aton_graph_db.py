from neo4j import GraphDatabase
from secrets_api import fetch_secrets, define_env
from repository import OrganizationRepository
# from py2neo import Graph, database


class AtonGraphDB:
    def __init__(self):
        self.driver = None

    def connect(self):
        define_env()
        secrets = fetch_secrets()
        print(secrets)
        self.driver = GraphDatabase.driver(secrets["ss.neo4j.url"],
                              auth=(secrets["ss.neo4j.username"],secrets["ss.neo4j.password"]),
                              database=secrets["ss.neo4j.database"])
        # graph = Graph(secrets["ss.neo4j.url"],
        #               auth=(secrets["ss.neo4j.username"],secrets["ss.neo4j.password"]),
        #               database=secrets["ss.neo4j.database"])
        self.driver.verify_connectivity()
        return self.driver

    def close(self):
        self.driver.close()

    def get_org_repo(self):
        return OrganizationRepository(self.driver)



