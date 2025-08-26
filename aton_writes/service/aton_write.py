from neo4j import Driver
from sqlalchemy.orm import Session

from db import AtonGraphDB
from db.neo4j_transaction_manager import Neo4jTransactionManager
from models.aton import Organization
from aton_writes.service.upsert_organization import create_organization
from models.aton.product import Product
from aton_writes.service.upsert_product import create_product


class AtonWrite:
    def __init__(self, db:AtonGraphDB):
        self.db = db

    def write_to_aton(self, organization: Organization):
        """
        Writes the given organization data to ATON by utilizing the provided driver instance.

        The function uses the `create_organization` function to handle the creation
        process within the ATON system. The provided organization details are passed
        to the `create_organization` function to execute this operation.

        :param organization: The organization object containing the data to be written
            to ATON.
        :type organization: Organization
        :return: None
        """
        create_organization(db=self.db, organization=organization)

    def write_products_networks(self, product: Product):
        """
        Writes the specified product's networks configuration using the driver instance.

        This method creates or updates the product's network data within the given
        driver session. The process utilizes the provided driver instance to handle
        the product's configuration efficiently.

        :param product: The Product instance containing the necessary information for
            network configuration.
        :type product: Product

        :return: None
        """
        create_product(db=self.db, product=product)
