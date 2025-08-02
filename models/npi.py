import neo4j.time


class NPI:
    """
    Represents a National Provider Identifier (NPI) entity.

    This class encapsulates the details of an NPI, including its value,
    validity period, and source information. It is designed for use in
    representing healthcare providers or organizations with unique identification
    numbers.

    :ivar value: The unique identifier representing the NPI.
    :ivar startDate: The start date of the NPI's validity period.
    :ivar endDate: The end date of the NPI's validity period.
    :ivar sourced_from: The source from which the NPI data was obtained.
        This information is optional and may be None.
    """
    def __init__(self, value: str,
                 start_date: neo4j.time.DateType,
                 end_date: neo4j.time.DateType,
                 sourced_from: str = None):
        self.value = value
        self.startDate = start_date
        self.endDate = end_date
        self.sourced_from = sourced_from