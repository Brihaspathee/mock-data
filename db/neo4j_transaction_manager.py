from neo4j import Transaction, Driver
from sqlalchemy.orm import Session

from db import AtonGraphDB


class Neo4jTransactionManager:

    def __init__(self, db: AtonGraphDB):
        self.db = db

    def execute_transaction(self, func, *args, **kwargs):
        with self.db.get_session() as session:
            transaction: Transaction = session.begin_transaction()
            try:
                func(transaction, *args, **kwargs)
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e