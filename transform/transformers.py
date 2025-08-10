from db import DBUtils
from models.portico import PPProv
from models.aton import Organization, Identifier
from aton_writes.service import upsert_organization


def transform_to_aton(providers: list[PPProv]):
    print("Transforming to Aton")
    for provider in providers:
        print(provider)
        print(provider.name)
        print(provider.prov_type.type)
        effective_date_str = "2023-01-01"
        effective_date = DBUtils.convert_date_to_neo4j_date(effective_date_str)
        organization: Organization = Organization(name=provider.name,
                                                  type=provider.prov_type.type,
                                                   effective_date=effective_date,
                                                   capitated=False,
                                                   sourced_from="Mock Data")
        organization.identifiers.append(getNPI(provider))
        organization.identifiers.append(getTIN(provider))
        # for address in provider.addresses:
        #     print(address)
        #     print(address.address.type)
        #     print(address.address.addr1)
        #     for phone in address.address.phones:
        #         print(phone)
        #         print(phone.phone.type)
        #         print(phone.phone.number)
        upsert_organization.create_organization(organization)

def getNPI(provider:PPProv):
    print("Getting NPI")
    start_date_str = "2023-01-01"
    end_date_str = "4000-01-01"
    start_date = DBUtils.convert_date_to_neo4j_date(start_date_str)
    end_date = DBUtils.convert_date_to_neo4j_date(end_date_str)
    npi: Identifier = Identifier(identifierType="NPI",
                                 value="634363562",
                                 start_date=start_date,
                                 end_date=end_date,
                                 sourced_from="Mock Data")
    return npi

def getTIN(provider:PPProv):
    print("Getting TIN")
    start_date_str = "2020-01-01"
    end_date_str = "4000-01-01"
    start_date = DBUtils.convert_date_to_neo4j_date(start_date_str)
    end_date = DBUtils.convert_date_to_neo4j_date(end_date_str)
    tin: Identifier = Identifier(identifierType="TIN",
                                 value="90-35353243",
                                 start_date=start_date,
                                 end_date=end_date,
                                 sourced_from="Mock Data")
    return tin