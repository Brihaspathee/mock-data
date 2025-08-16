from neo4j.time import DateType

from db import DBUtils
from models.aton.qualification import Qualification
from models.portico import PPProv, PPProvAttrib
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

def getProviderAttributes(provider:PPProv):
    print("Getting Provider Attributes")
    for attribute in provider.attributes:
        print(attribute.attribute_id)
        if attribute.attribute_id == 102:
            if canLoadQualification(attribute):
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
                                                             secondary_labels=["Certification"])


def canLoadQualification(pprovAttribute:PPProvAttrib) -> bool:
    print("Checking if can load qualification")
    print("Attribute ID: ", pprovAttribute.attribute_id)
    for value in pprovAttribute.values:
        print("Field ID: ", value.field_id)
        print("Value: ", value.value)
        if value.field_id == 1005 and value.value == "YES":
            print("Found field 1005 with value YES")
            return True
    return False
