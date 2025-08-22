from neo4j import Transaction, Driver


class Neo4jTransactionManager:

    def __init__(self, driver: Driver):
        self.driver = driver

    def execute_transaction(self, func, *args, **kwargs):
        with self.driver.session() as session:
            transaction: Transaction = session.begin_transaction()
            try:
                func(transaction, *args, **kwargs)
                transaction.commit()
            except Exception as e:
                transaction.rollback()
                raise e