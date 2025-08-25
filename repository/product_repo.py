from neo4j import Transaction
from neo4j.graph import Node

from models.aton.product import Product
import logging

log = logging.getLogger(__name__)


def create_product(tx: Transaction, prod: Product) -> Node | None:

    with open("queries/create_product.cypher", "r") as f:
        query = f.read()
    result = tx.run(query, code=prod.code,
                           name=prod.name,
                           description=prod.description)
    for record in result:
        prod_node = record["product"]
        return prod_node
    return None