from db import AtonGraphDB, PorticoDB, DBUtils
from neo4j import Driver

from models.aton import Organization
from models.portico import Person
from models.portico.pp_prov import PPProv


def get_person():
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

def get_provider():
    try:
        providers: list[PPProv] = session.query(PPProv).all()
        for provider in providers:
            print(provider)
            print(provider.name)
            print(provider.prov_type.type)
            create_organization(provider)
            for address in provider.addresses:
                print(address)
                print(address.address.type)
                print(address.address.addr1)
                for phone in address.address.phones:
                    print(phone)
                    print(phone.phone.type)
                    print(phone.phone.number)

    except Exception as e:
        session.rollback()
        print("Error: ", e, "\n")

    finally:
        session.close()
        portico_db.close()

def create_organization(provider:PPProv):
    aton_graph: AtonGraphDB = AtonGraphDB()
    driver: Driver = aton_graph.connect()
    effective_date_str="2023-01-01"
    effective_date = DBUtils.convert_date_to_neo4j_date(effective_date_str)
    organization = Organization(name=provider.name,
                                alias_name="Org 1",
                                type=provider.prov_type.type,
                                description="Description 1",
                                effective_date=effective_date,
                                capitated=True,
                                sourced_from="Source 1")
    org_repo = aton_graph.get_org_repo()
    org_repo.create_organization(organization)

portico_db: PorticoDB = PorticoDB()
portico_db.connect()
session = portico_db.get_session()
# get_person()
get_provider()



