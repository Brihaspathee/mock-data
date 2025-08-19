class Address:

    def __init__(self, street_address: str,
                 secondary_address: str=None,
                 city: str=None,
                 state: str=None,
                 zip_code: str=None,
                 county: str=None,
                 fips: str=None,
                 latitude: str=None,
                 longitude: str=None,):
        self.street_address = street_address
        self.secondary_address = secondary_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.county = county
        self.fips = fips
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return (f"<Address(street_address={self.street_address}, "
                f"secondary_address={self.secondary_address}, "
                f"city={self.city}, "
                f"state={self.state}, "
                f"zip_code={self.zip_code}, "
                f"county={self.county}, "
                f"fips={self.fips}, "
                f"latitude={self.latitude}, "
                f"longitude={self.longitude})>")