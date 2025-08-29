from neo4j.time import DateType
from config import settings
from db import DBUtils
from models.portico.pp_prov import PPProv
from models.portico.pp_prov_attrib import PPProvAttrib
from models.portico.pp_prov_addr import PPProvAddr
from models.portico.pp_addr import PPAddr
from models.portico.pp_phones import PPPhones
from models.portico.pp_addr_phones import PPAddrPhones
from models.aton import Organization, Identifier, Qualification, Person, Telecom, Address, Contact
from aton_writes.service import upsert_organization
from utils.log_provider import log_provider
from typing import cast, Any
from transform.attribute_transformer import AttributeStructure, Result, build_node_data, get_attribute
from transform.transformers import transform_to_aton
import logging


log = logging.getLogger(__name__)

@transform_to_aton.register(PPProv)
def _(provider:PPProv) -> Organization:
    """
    Transforms a list of PPProv providers into a list of Aton organizations.

    This function takes a list of `PPProv` provider objects and performs a transformation to produce
    a list of `Organization` objects that are compliant with the Aton data model.
    Relevant attributes and relationships are extracted from each provider and appropriately mapped
    to the organization object. It processes identifiers, addresses, and other provider attributes
    required by the Aton organization format.

    :param provider:
        A list of `PPProv` instances representing the source provider data.
    :return:
        A list of `Organization` instances representing the transformed provider information in
        the Aton format.
    """
    # log.info(f"Transforming to Aton:{providers}" )
    # for provider in providers:
        # log_provider(provider)
    organization: Organization = Organization(name=provider.name,
                                              alias_name=provider.name,
                                              description=provider.name,
                                              type=provider.prov_type.type,
                                              capitated=False,
                                              pcp_practitioner_required=False,
                                              atypical=False,
                                              popularity=0.0)
    organization.identifiers.append(get_tin(provider))
    get_provider_attributes(provider, organization)
    for address in provider.addresses:
        organization.contacts.append(get_contact(address))
        #upsert_organization.create_organization(organization)
        # organizations.append(organization)
    return organization


def get_tin(provider: PPProv) -> Identifier:
    """
    Gets the Tax Identification Number (TIN) information for the provided
    provider and encapsulates it within an `Identifier` object.

    :param provider: The provider object containing the TIN and associated
        legal name.
        :type provider: PPProv
    :return: An `Identifier` object representing the TIN information,
        including its type, label, relationship, value, and associated
        legal name.
    :rtype: Identifier
    """
    # log.info("Getting TIN")
    tin: Identifier = Identifier(identifier_type="TIN",
                                 identifier_label="TIN",
                                 identifier_rel="HAS_TIN",
                                 value=provider.tin.tin,
                                 legal_name=provider.tin.name)
    return tin

def get_provider_attributes(provider:PPProv, organization: Organization):
    """
    Retrieve and process attributes from a given provider and populate the organization's
    identifiers and qualifications based on the attribute kinds.

    This function iterates through the attributes of a provider and, depending on the
    attribute kind, performs the following actions:
    - If the attribute kind is "identifier", the attribute value is appended to the
      organization's list of identifiers.
    - If the attribute kind is "qualification" and the value is not None, it is appended
      to the organization's list of qualifications.

    :param provider: A provider object that contains attributes to be processed.
    :type provider: PPProv
    :param organization: An organization object where identifiers and qualifications
        derived from the provider's attributes are stored.
    :type organization: Organization
    :return: None
    """
    # log.info("Getting Provider Attributes")
    # log.info(f"Getting the attribute structure: {settings.ATTRIBUTE_STRUCTURES}")
    for attribute in provider.attributes:
        # log.info(attribute.attribute_id)
        result: Result = get_attribute(attribute)
        if result.kind == "identifier":
            organization.identifiers.append(result.value)
        elif result.kind == "qualification":
            if result.value is not None:
                organization.qualifications.append(result.value)


def get_contact(prov_addr: PPProvAddr) -> Contact:
    """
    Create a Contact object based on the provided provider address.

    The function extracts the necessary information such as address type,
    physical address, and phone information from the given provider address
    to construct and return a Contact object.

    :param prov_addr: The provider address from which the contact information
        is to be retrieved and processed. Must be of type ``PPProvAddr``.
    :return: A ``Contact`` object containing the use type, physical address,
        and telecommunication details derived from the provider address.
    """
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
    """
    Extracts and formats phone-related information from the provided PPAddr object into a Telecom object.

    This function iterates over the list of phone entries in the provided ``PPAddr``
    object, extracting phone details based on their types (e.g., CELL, FAX, TTY, AFH).
    It then populates the corresponding attributes in the ``Telecom`` object and
    returns it.

    :param pp_addr: The ``PPAddr`` object containing phone-related information.
    :type pp_addr: PPAddr

    :return: A ``Telecom`` object populated with phone number details categorized
        by type (e.g., phone, fax, tty, after-hours number).
    :rtype: Telecom
    """
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

