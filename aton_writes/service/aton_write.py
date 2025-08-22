from neo4j import Driver
from sqlalchemy.orm import Session

from db import AtonGraphDB
from db.neo4j_transaction_manager import Neo4jTransactionManager
from models.aton import Organization
from aton_writes.service.upsert_organization import create_organization


class AtonWrite:
    def __init__(self):
        db: AtonGraphDB = AtonGraphDB()
        db.connect()
        self.driver: Driver = db.driver

    def write_to_aton(self, organization: Organization):
        create_organization(driver=self.driver, organization=organization)
