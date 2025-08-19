from neo4j.time import DateType

from db import DBUtils
from models.portico import PPProv, PPProvAttrib, PPProvAddr, PPAddr, PPPhones, PPAddrPhones
from models.aton import Organization, Identifier, Qualification, Person, Telecom, Address, Contact
from aton_writes.service import upsert_organization
from utils.log_provider import log_provider
from typing import cast
import logging

log = logging.getLogger(__name__)


def transform_to_aton(providers: list[PPProv]):
    print(f"Transforming to Aton:{providers}" )
    for provider in providers:
        log_provider(provider)
        effective_date_str = "2023-01-01"
        effective_date = DBUtils.convert_date_to_neo4j_date(effective_date_str)
        organization: Organization = Organization(name=provider.name,
                                                  type=provider.prov_type.type,
                                                   effective_date=effective_date,
                                                   capitated=False,
                                                   sourced_from="Mock Data")
        npi = getNPI(provider)
        log.info(f"NPI value: {npi.value}")
        log.info(f"NPI start date: {npi.start_date}")
        organization.identifiers.append(npi)
        organization.identifiers.append(getTIN(provider))
        organization.qualifications = get_provider_attributes(provider)
        for address in provider.addresses:
            organization.contacts.append(get_contact(address))
        # for contact in organization.contacts:
        #     log.info(f"Contacts in Org: {contact}")
        upsert_organization.create_organization(organization)

def getNPI(provider:PPProv):
    log.info("Getting NPI")
    npi: Identifier = Identifier()
    for attribute in provider.attributes:
        log.info(attribute.attribute_id)
        if attribute.attribute_id == 101:
            npi.identifier_type = "NPI"
            npi.sourced_from = "Mock Data"
            for value in attribute.values:
                log.info(value.field_id)
                log.info(value.field)
                if value.field_id == 1001:
                    npi_value = value.value
                    npi.value = npi_value
                elif value.field_id == 1002:
                    start_date: DateType = value.value_date
                    # start_date = DBUtils.convert_date_to_neo4j_date(start_date_str)
                    log.info(start_date)
                    npi.start_date = start_date
                elif value.field_id == 1003:
                    end_date = value.value_date
                    # end_date = DBUtils.convert_date_to_neo4j_date(end_date_str)
                    log.info(end_date)
                    npi.end_date = end_date
    # npi: Identifier = Identifier(identifierType="NPI",
    #                              value="634363562",
    #                              start_date=start_date,
    #                              end_date=end_date,
    #                              sourced_from="Mock Data")
    log.info(f"NPI Start Date {npi.start_date}")
    return npi

def getTIN(provider:PPProv):
    log.info("Getting TIN")
    tin: Identifier = Identifier(identifier_type="TIN",
                                 value=provider.tin.tin,
                                 legal_name=provider.tin.name,
                                 sourced_from="Mock Data")
    return tin

def get_provider_attributes(provider:PPProv) -> list[Qualification]:
    log.info("Getting Provider Attributes")
    qualifications: list[Qualification] = []
    for attribute in provider.attributes:
        log.info(attribute.attribute_id)
        if attribute.attribute_id == 102:
            if can_load_qualification(attribute):
                type: str  = "AASM Certification"
                start_date: DateType | None = ""
                end_date: DateType | None = None
                for value in attribute.values:
                    if value.field_id == 1006:
                        start_date = value.value_date
                    if value.field_id == 1007:
                        end_date = value.value_date
                qualification: Qualification = Qualification(qualification_type=type,
                                                             start_date=start_date,
                                                              end_date=end_date,
                                                             secondary_labels=["Certification"],
                                                             sourced_from="Mock Data")
                qualifications.append(qualification)
        log.info(f"Qualifications: {qualifications}")
    return qualifications


def can_load_qualification(pprovAttribute:PPProvAttrib) -> bool:
    log.info("Checking if can load qualification")
    log.info(f"Attribute ID: {pprovAttribute.attribute_id}")
    for value in pprovAttribute.values:
        log.info(f"Field ID: {value.field_id}")
        log.info(f"Value: {value.value}")
        if value.field_id == 1005 and value.value == "YES":
            log.info("Found field 1005 with value YES")
            return True
    return False

def get_contact(prov_addr: PPProvAddr) -> Contact:
    address: PPAddr = cast(PPAddr, prov_addr.address)
    contact_use = address.type
    log.info(f"Contact Use: {contact_use}")
    provider_address: Address = get_address(address)
    log.info(f"Phones: {address.phones}")
    provider_telecom: Telecom = get_phone(address)
    contact: Contact = Contact(use=contact_use,
                                address=provider_address,
                                telecom=provider_telecom)
    log.info(f"Contact: {contact}")
    return contact

def get_address(prov_addr: PPAddr) -> Address:
    log.info(f"Address:{prov_addr}")
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
        log.info(f"Phone:{pp_addr_phone}")
        log.info(f"Phone Type:{pp_addr_phone.phone.type}")
        log.info(f"Phone area:{pp_addr_phone.phone.area_code}")
        log.info(f"Phone exchange:{pp_addr_phone.phone.exchange}")
        log.info(f"Phone number:{pp_addr_phone.phone.number}")
        phone_number: str = pp_addr_phone.phone.area_code + pp_addr_phone.phone.exchange +  pp_addr_phone.phone.number
        log.info(f"Phone Number Full:{phone_number}")
        if pp_addr_phone.phone.type == "CELL":
            telecom.phone = phone_number
        elif pp_addr_phone.phone.type == "FAX":
            telecom.fax = phone_number
        elif pp_addr_phone.phone.type == "TTY":
            telecom.tty = phone_number
        elif pp_addr_phone.phone.type == "AFH":
            telecom.after_hours_number = phone_number
    return telecom

