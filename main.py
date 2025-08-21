from db import AtonGraphDB, PorticoDB, DBUtils
from config import settings
from models.aton import Organization
from models.portico import Person
from models.portico.pp_prov import PPProv
from portico_reads.service.provider.provider_read import ProviderRead
from transform import transformers
from transform.transformers import transform_to_aton
import logging

log = logging.getLogger(__name__)




log.info("Starting...")
log.info(f"Running on {settings.ENVIRONMENT} environment")
log.info(f"POSTGRES info {settings.POSTGRES} environment")
log.info(f"NEO4J info {settings.NEO4J} environment")
log.info(f"Attributes JSON{settings.FLAT_CONFIG}")

# Read the providers from Portico
provider_read: ProviderRead = ProviderRead()
providers: list[PPProv] = provider_read.read_provider()
# Transform Providers into the shape that is compatible with Aton
transform_to_aton(providers)



