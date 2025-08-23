from aton_writes.service.aton_write import AtonWrite
from db import AtonGraphDB, PorticoDB, DBUtils
from config import settings
from models.aton import Organization
from portico_reads.service.provider import provider_read
from models.portico import Person
from models.portico.pp_prov import PPProv
from transform import transformers
from transform.transformers import transform_to_aton
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
    with portico_db.get_session() as session:
        providers = provider_read.read_provider(session)
    # provider_read: ProviderRead = ProviderRead()
    # providers: list[PPProv] = provider_read.read_provider()
    # Transform Providers into the shape that is compatible with Aton
    organizations: list[Organization] = transform_to_aton(providers)
    # Iterate through the list of organizations and write them to Aton
    for organization in organizations:
        aton_write: AtonWrite = AtonWrite()
        aton_write.write_to_aton(organization)

if __name__ == "__main__":
    main()



