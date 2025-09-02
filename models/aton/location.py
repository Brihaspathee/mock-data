class Location:
    element_id: str = None
    location_name: str = None
    street_address: str = None
    secondary_address: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    county: str = None
    fips: str = None
    latitude: str = None
    longitude: str = None
    smarty_key: str = None

    def __repr__(self):
        """
        Generate the official string representation of the Location object.
        """
        return (f"<Location(element_id={self.element_id}, "
                f"location_name={self.location_name}, "
                f"street_address={self.street_address}, "
                f"secondary_address={self.secondary_address}, "
                f"city={self.city}, "
                f"state={self.state}, "
                f"zip_code={self.zip_code}, "
        )