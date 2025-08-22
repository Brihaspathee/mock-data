class Address:
    """
    Represents a physical address including details like street address, city, state, and more.

    This class is used to store detailed information about a physical address. It can capture
    complete address details such as street address, secondary address, city, state, zip code,
    county, FIPS code, latitude, and longitude. This can be helpful for storing and managing
    addresses in applications like logistics, e-commerce, or mapping services.

    :ivar street_address: The primary street address.
    :type street_address: str
    :ivar secondary_address: An additional address line (e.g., apartment or suite number).
    :type secondary_address: str, optional
    :ivar city: The city where the address is located.
    :type city: str, optional
    :ivar state: The state where the address is located.
    :type state: str, optional
    :ivar zip_code: The ZIP/postal code of the address.
    :type zip_code: str, optional
    :ivar county: The county where the address is located.
    :type county: str, optional
    :ivar fips: The FIPS (Federal Information Processing Standards) code of the location.
    :type fips: str, optional
    :ivar latitude: The latitude coordinate of the address.
    :type latitude: str, optional
    :ivar longitude: The longitude coordinate of the address.
    :type longitude: str, optional
    """
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
        """
        Provides a string representation of the Address object by including all of its
        attributes in a formatted string. This method is primarily for debugging and
        logging purposes, aiding in visualization of the object's values.

        :return: A string representation of the Address object, including the values
            of its attributes.
        :rtype: str
        """
        return (f"<Address(street_address={self.street_address}, "
                f"secondary_address={self.secondary_address}, "
                f"city={self.city}, "
                f"state={self.state}, "
                f"zip_code={self.zip_code}, "
                f"county={self.county}, "
                f"fips={self.fips}, "
                f"latitude={self.latitude}, "
                f"longitude={self.longitude})>")