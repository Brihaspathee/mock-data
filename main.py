from secrets_api import fetch_secrets, define_env
import neo4j
from neo4j import GraphDatabase
# from py2neo import Graph, database

define_env()
secrets = fetch_secrets()
print(secrets)
driver = GraphDatabase.driver(secrets["ss.neo4j.url"],
                              auth=(secrets["ss.neo4j.username"],secrets["ss.neo4j.password"]),
                              database=secrets["ss.neo4j.database"])
# graph = Graph(secrets["ss.neo4j.url"],
#               auth=(secrets["ss.neo4j.username"],secrets["ss.neo4j.password"]),
#               database=secrets["ss.neo4j.database"])



driver.verify_connectivity()
with open("queries/create_org.cypher", "r") as f:
    query = f.read()
with driver.session() as session:
    result = session.run(query)
    print(result)
    for record in result:
        print(record)
