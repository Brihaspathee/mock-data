import pytest
import subprocess
import time
import os
import docker
from testcontainers.postgres import PostgresContainer
from testcontainers.neo4j import Neo4jContainer
from neo4j import GraphDatabase
import psycopg2

DOCKER_COMPOSE_FILE = os.path.join(os.path.dirname(__file__), "docker-compose-test.yaml")
POSTGRES_DB = "portico"
POSTGRES_USER = "porticoadmin"
POSTGRES_PASSWORD = "password"
POSTGRES_SCHEMA = "portown"
POSTGRES_PORT = 5433

NEO4J_BOLT_PORT = 7688
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "test"

# ------------------ Helper functions ------------------

def wait_for_postgres(max_retries=30, delay=2):
    """Wait until Postgres is ready to accept connections."""
    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                dbname=POSTGRES_DB,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                host="localhost",
                port=POSTGRES_PORT,
            )
            conn.close()
            return
        except psycopg2.OperationalError as e:
            print(f"Postgres not ready yet ({e}), retrying in {delay}s...")
            time.sleep(delay)
    raise TimeoutError("Postgres did not become ready in time")

def wait_for_neo4j(max_retries=30, delay=2):
    """Wait until Neo4j is ready by running a test query."""
    for attempt in range(max_retries):
        try:
            driver = GraphDatabase.driver(
                f"bolt://localhost:{NEO4J_BOLT_PORT}",
                auth=(NEO4J_USER, NEO4J_PASSWORD)
            )
            with driver.session() as session:
                session.run("RETURN 1").single()
            driver.close()
            return
        except Exception as e:
            print(f"Neo4j not ready yet ({e}), retrying in {delay}s...")
            time.sleep(delay)
    raise TimeoutError("Neo4j did not become ready in time")

@pytest.fixture(scope="session", autouse=True)
def docker_compose_environment():
    """Spin up test containers using docker-compose before tests, tear down after."""
    client = docker.from_env()

    # Start containers
    os.system(f"docker compose -f {DOCKER_COMPOSE_FILE} up -d")

    # Wait for DBs
    wait_for_postgres()
    wait_for_neo4j()

    yield  # run the tests

    # Tear down containers
    os.system(f"docker compose -f {DOCKER_COMPOSE_FILE} down -v")