from models.portico import PPProv


def log_providers(providers: list[PPProv]):
    for provider in providers:
        log_provider(provider)

def log_provider(provider: PPProv):
    print(provider)
    print(provider.name)
    print(provider.prov_type.type)
    print(provider.tin.tin)
    for address in provider.addresses:
        print(address)
        print(address.address.type)
        print(address.address.addr1)
        for phone in address.address.phones:
            print(phone)
            print(phone.phone.type)
            print(phone.phone.number)
    for attribute in provider.attributes:
        print(f"Provider Attribute:{attribute.attribute_type}")
        print(attribute)
        print(attribute.attribute_type)
        for value in attribute.values:
            print(value)
            print(value.field)
            print(value.value)
            print(value.value_date)