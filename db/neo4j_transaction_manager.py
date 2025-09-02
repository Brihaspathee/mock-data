from neo4j import Transaction, Driver
from sqlalchemy.orm import Session

from db.aton_graph_db import get_session


class Neo4jTransactionManager:

    # def __init__(self, db: AtonGraphDB):
    #     self.db = db

    def execute_transaction(self, func, *args, **kwargs):
        with get_session() as session:
            transaction: Transaction = session.begin_transaction()
            try:
                func(transaction, *args, **kwargs)
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e