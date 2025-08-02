from db import AtonGraphDB, PorticoDB, DBUtils
from neo4j import Driver

from models import Organization
from models.portico import Person

aton_graph: AtonGraphDB = AtonGraphDB()
driver: Driver = aton_graph.connect()
effective_date_str="2023-01-01"
effective_date = DBUtils.convert_date_to_neo4j_date(effective_date_str)
organization = Organization(name="Organization 1",
                            alias_name="Org 1",
                            description="Description 1",
                            effective_date=effective_date,
                            capitated=True,
                            sourced_from="Source 1")
org_repo = aton_graph.get_org_repo()
org_repo.create_organization(organization)

portico_db: PorticoDB = PorticoDB()
portico_db.connect()
session = portico_db.get_session()
try:
    people = session.query(Person).all()
    for person in people:
        print(person)
        print(person.name)

    new_person = Person(name="John Doe", age=50)
    session.add(new_person)
    session.commit()

    people = session.query(Person).all()
    for person in people:
        print(person)
        print(person.name)

except Exception as e:
    session.rollback()
    print("Error: ", e, "\n")

finally:
    session.close()
    portico_db.close()

