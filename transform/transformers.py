from functools import singledispatch

from neo4j.time import DateType
from config import settings
from db import DBUtils
from models.aton.product import Product
from models.portico import PPProv, PPProvAttrib, PPProvAddr, PPAddr, PPPhones, PPAddrPhones
from models.aton import Organization, Identifier, Qualification, Person, Telecom, Address, Contact
from aton_writes.service import upsert_organization
from models.portico.pp_net import PPNetDict, PPNet
from utils.log_provider import log_provider
from typing import cast, Any
from transform.attribute_transformer import AttributeStructure, Result, build_node_data, get_attribute
import logging


log = logging.getLogger(__name__)

def transformer(portico_entity_list:list) -> list | None:
    """
    Transforms a list of `portico_entity_list` objects into a list of `Organization`
    or `Product` instances, based on their type. The input list is iterated through
    to determine the type of each entity, and they are converted using specific
    transformation methods.

    :param portico_entity_list: A list of entities containing instances of either
        `PPProv` or `PPNet` type objects to be transformed.
    :type portico_entity_list: list
    :return: A list of transformed `Organization` objects if any `PPProv` entities
        are found, a list of `Product` objects if any `PPNet` entities are found,
        or `None` if no entities are transformed.
    :rtype: list | None
    """
    organizations: list[Organization] = []
    products: list[Product] = []
    is_org: bool = False
    is_net: bool = False
    for porticoEntity in portico_entity_list:
        if isinstance(porticoEntity,PPProv):
            is_org = True
            organization: Organization = transform_to_aton(porticoEntity)
        elif isinstance(porticoEntity, PPNet):
            is_net = True
            product: Product = transform_to_aton(porticoEntity)
        if is_org:
            organizations.append(organization)
        elif is_net:
            products.append(product)
    if organizations:
        return organizations
    elif products:
        return products
    else:
        return None


@singledispatch
def transform_to_aton(arg):
    """
    Transform the given argument into an ATON representation. The behavior of the
    function depends on the specific type of the input argument. If the type is not
    supported, a TypeError is raised. This function serves as a generic dispatch
    mechanism for handling various input types.

    :param arg: Input value to be transformed. The specific behavior is determined
        by the type of this argument.
    :type arg: Any

    :return: Raises an exception by default. Specific dispatch handlers should
        define the appropriate return type based on the input argument type.
    :rtype: NoReturn

    :raises TypeError: If the input type is unsupported by this function.
    """
    raise TypeError(f"Unsupported type: {type(arg)}")

