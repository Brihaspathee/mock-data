from neo4j import Driver, Transaction
from neo4j.graph import Node

from db.neo4j_transaction_manager import Neo4jTransactionManager
from models.aton.product import Product
import logging

from repository import product_repo, network_repo

log = logging.getLogger(__name__)


def create_product(driver: Driver,product: Product):
    """
    Executes a transaction to create a product in the database by using the provided transaction manager.
    This function ensures the creation operation is executed, logging success or failure messages, and
    handles resource cleanup by closing the database driver after the transaction completes.

    :param driver: The database driver instance used to establish the connection to the database.
    :type driver: Driver
    :param product: The product entity containing information to be stored in the database.
    :type product: Product
    :return: None
    """
    transaction_manager = Neo4jTransactionManager(driver=driver)
    try:
        transaction_manager.execute_transaction(create_prod_net, product)
        log.info("Transaction successful")
        log.info("Product {} created".format(product.name))
    except Exception as e:
        log.error("Transaction failed: {}".format(e))
        log.error(e)
    finally:
        driver.close()

def create_prod_net(transaction: Transaction, product: Product):
    """
    Creates a product node in the repository and its associated network nodes.

    This function initializes a product node using the provided product object
    and transaction context. It also iteratively creates network nodes for
    each network associated with the product.

    :param transaction: The transaction context used for creating the product
        and network nodes.
    :type transaction: Transaction
    :param product: The product object containing information about the
        product and its associated networks.
    :type product: Product
    :return: None
    """
    prod_node = product_repo.create_product(transaction, product)
    for network in product.networks:
        net_node: Node = network_repo.create_network(transaction, prod_node, network)