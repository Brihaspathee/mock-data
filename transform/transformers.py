from neo4j.time import DateType
from config import settings
from db import DBUtils
from models.portico import PPProv, PPProvAttrib, PPProvAddr, PPAddr, PPPhones, PPAddrPhones
from models.aton import Organization, Identifier, Qualification, Person, Telecom, Address, Contact
from aton_writes.service import upsert_organization
from utils.log_provider import log_provider
from typing import cast, Any
from transform.attribute_transformer import AttributeStructure, Result, build_node_data, get_attribute
import logging


log = logging.getLogger(__name__)


def transform_to_aton(providers: list[PPProv]) -> list[Organization]:
    # log.info(f"Transforming to Aton:{providers}" )
    organizations: list[Organization] = []
    for provider in providers:
        # log_provider(provider)
        effective_date_str = "2023-01-01"
        effective_date = DBUtils.convert_date_to_neo4j_date(effective_date_str)
        organization: Organization = Organization(name=provider.name,
                                                  alias_name=provider.name,
                                                  description=provider.name,
                                                  type=provider.prov_type.type,
                                                   capitated=False,
                                                   pcpAssigment=False)
        organization.identifiers.append(get_tin(provider))
        get_provider_attributes(provider, organization)
        for address in provider.addresses:
            organization.contacts.append(get_contact(address))
        #upsert_organization.create_organization(organization)
        organizations.append(organization)
    return organizations


def get_tin(provider:PPProv):
    # log.info("Getting TIN")
    tin: Identifier = Identifier(identifier_type="TIN",
                                 identifier_label="TIN",
                                 identifier_rel="HAS_TIN",
                                 value=provider.tin.tin,
                                 legal_name=provider.tin.name,
                                 sourced_from="Mock Data")
    return tin

def get_provider_attributes(provider:PPProv, organization: Organization):
    # log.info("Getting Provider Attributes")
    # log.info(f"Getting the attribute structure: {settings.ATTRIBUTE_STRUCTURES}")
    for attribute in provider.attributes:
        log.info(attribute.attribute_id)
        result: Result = get_attribute(attribute)
        if result.kind == "identifier":
            organization.identifiers.append(result.value)
        elif result.kind == "qualification":
            if result.value is not None:
                organization.qualifications.append(result.value)


def get_contact(prov_addr: PPProvAddr) -> Contact:
    address: PPAddr = cast(PPAddr, prov_addr.address)
    contact_use = address.type
    # log.info(f"Contact Use: {contact_use}")
    provider_address: Address = get_address(address)
    # log.info(f"Phones: {address.phones}")
    provider_telecom: Telecom = get_phone(address)
    contact: Contact = Contact(use=contact_use,
                                address=provider_address,
                                telecom=provider_telecom)
    # log.info(f"Contact: {contact}")
    return contact

def get_address(prov_addr: PPAddr) -> Address:
    # log.info(f"Address:{prov_addr}")
    address: Address = Address(street_address=prov_addr.addr1,
                               secondary_address=prov_addr.addr2,
                               city=prov_addr.city,
                               state=prov_addr.state,
                               zip_code=prov_addr.zip,
                               county=prov_addr.county,
                               latitude=prov_addr.latitude,
                               longitude=prov_addr.longitude)
    return address

def get_phone(pp_addr: PPAddr) -> Telecom:
    telecom: Telecom = Telecom()
    for pp_addr_phone in pp_addr.phones:
        # log.info(f"Phone:{pp_addr_phone}")
        # log.info(f"Phone Type:{pp_addr_phone.phone.type}")
        # log.info(f"Phone area:{pp_addr_phone.phone.area_code}")
        # log.info(f"Phone exchange:{pp_addr_phone.phone.exchange}")
        # log.info(f"Phone number:{pp_addr_phone.phone.number}")
        phone_number: str = pp_addr_phone.phone.area_code + pp_addr_phone.phone.exchange +  pp_addr_phone.phone.number
        # log.info(f"Phone Number Full:{phone_number}")
        if pp_addr_phone.phone.type == "CELL":
            telecom.phone = phone_number
        elif pp_addr_phone.phone.type == "FAX":
            telecom.fax = phone_number
        elif pp_addr_phone.phone.type == "TTY":
            telecom.tty = phone_number
        elif pp_addr_phone.phone.type == "AFH":
            telecom.after_hours_number = phone_number
    return telecom

