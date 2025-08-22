import pytest
from testcontainers.postgres import PostgresContainer
from testcontainers.neo4j import Neo4jContainer
from neo4j import GraphDatabase
import psycopg2

class AtonNeo4jContainer(Neo4jContainer):
    def __init__(self, image="neo4j:latest", **kwargs):
        super().__init__(image=image, **kwargs)
        # Enable APOC plugin
        self.with_env("NEO4J_APOC_PLUGINS", '["apoc"]')
        self.with_env("NEO4J_dbms_security_procedures_unrestricted", "apoc.*")
        self.with_env("NEO4J_dbms_security_procedures_allowlist", "apoc.*")