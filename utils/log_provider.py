from models.portico import PPProv
import logging

log = logging.getLogger(__name__)


def log_providers(providers: list[PPProv]):
    for provider in providers:
        log_provider(provider)

def log_provider(provider: PPProv):
    log.info(provider)
    log.info(provider.name)
    log.info(provider.prov_type.type)
    log.info(provider.tin.tin)
    for address in provider.addresses:
        log.info(address)
        log.info(address.address.type)
        log.info(address.address.addr1)
        for phone in address.address.phones:
            log.info(phone)
            log.info(phone.phone.type)
            log.info(phone.phone.number)
    for attribute in provider.attributes:
        log.info(f"Provider Attribute:{attribute.attribute_type}")
        log.info(attribute)
        log.info(attribute.attribute_type)
        for value in attribute.values:
            log.info(value)
            log.info(value.field)
            log.info(value.value)
            log.info(value.value_date)