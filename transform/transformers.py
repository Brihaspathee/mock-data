from neo4j.time import DateType

from db import DBUtils
from models.portico import PPProv
from models.aton import Organization, Identifier
from aton_writes.service import upsert_organization
from utils.log_provider import log_provider


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
        print(f"NPI value: {npi.value}")
        print(f"NPI start date: {npi.start_date}")
        organization.identifiers.append(npi)
        organization.identifiers.append(getTIN(provider))
        upsert_organization.create_organization(organization)

def getNPI(provider:PPProv):
    print("Getting NPI")
    npi: Identifier = Identifier()
    for attribute in provider.attributes:
        print(attribute.attribute_id)
        if attribute.attribute_id == 101:
            npi.identifier_type = "NPI"
            npi.sourced_from = "Mock Data"
            for value in attribute.values:
                print(value.field_id)
                print(value.field)
                if value.field_id == 1001:
                    npi_value = value.value
                    npi.value = npi_value
                elif value.field_id == 1002:
                    start_date: DateType = value.value_date
                    # start_date = DBUtils.convert_date_to_neo4j_date(start_date_str)
                    print(start_date)
                    npi.start_date = start_date
                elif value.field_id == 1003:
                    end_date = value.value_date
                    # end_date = DBUtils.convert_date_to_neo4j_date(end_date_str)
                    print(end_date)
                    npi.end_date = end_date
    # npi: Identifier = Identifier(identifierType="NPI",
    #                              value="634363562",
    #                              start_date=start_date,
    #                              end_date=end_date,
    #                              sourced_from="Mock Data")
    print(f"NPI Start Date {npi.start_date}")
    return npi

def getTIN(provider:PPProv):
    print("Getting TIN")
    tin: Identifier = Identifier(identifier_type="TIN",
                                 value=provider.tin.tin,
                                 legal_name=provider.tin.name,
                                 sourced_from="Mock Data")
    return tin