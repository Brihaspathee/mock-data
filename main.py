from utils.log_provider import log_providers
from aton_writes.service.aton_write import AtonWrite
from db import PorticoDB, DBUtils
from db.aton_graph_db import get_driver, close_driver
from config import settings
from models.aton import Organization
from models.aton.product import Product
from models.portico.pp_net import PPNetDict, PPNet
from portico_reads.service.provider import provider_read
from portico_reads.service.network import network_read
from models.portico.person import Person
from models.portico.pp_prov import PPProv
from transform import transformers
from transform.transformers import transformer, transform_to_aton
import transform.transform_provider
import transform.transform_network
import logging

log = logging.getLogger(__name__)


def main():
    log.info("Starting...")
    log.info(f"Running on {settings.ENVIRONMENT} environment")
    log.info(f"POSTGRES info {settings.POSTGRES} environment")
    log.info(f"NEO4J info {settings.NEO4J} environment")
    log.info(f"Attributes JSON{settings.FLAT_CONFIG}")

    # Read the providers from Portico
    portico_db: PorticoDB = PorticoDB()
    portico_db.connect()
    with (portico_db.get_session() as session):
        networks: list[PPNet] = network_read.get_networks(session)
        providers: list[PPProv] = provider_read.read_provider(session)
        # log_providers(providers)
        # log.info(f"# of level 5 networks:{len(networks)}")
    # Transform Networks into the shape that is compatible with Aton
    products: list[Product] = transformer(networks)
    # aton_db: AtonGraphDB = AtonGraphDB()
    # aton_db.connect()
    #
    for product in products:
        aton_write: AtonWrite = AtonWrite()
        aton_write.write_products_networks(product)
    # # Transform Providers into the shape that is compatible with Aton
    organizations: list[Organization] = transformer(providers)
    # # Iterate through the list of organizations and write them to Aton
    for organization in organizations:
        aton_write: AtonWrite = AtonWrite()
        aton_write.write_to_aton(organization)
    # aton_db.close()

if __name__ == "__main__":
    driver = get_driver()
    main()
    close_driver()



