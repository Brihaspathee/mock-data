from neo4j.time import DateType

class Qualification:
    """
    Represents a qualification with details about its type, status, issuer,
    and related duration, as well as optional secondary labels.

    Qualifications serve to categorize or detail expertise or credentials,
    often given by an issuing authority. This class is designed to encapsulate
    related metadata while supporting optional details like secondary labels,
    date ranges, and the state of validity.

    :ivar qualification_type: The type or category of the qualification.
    :type qualification_type: str
    :ivar value: An optional value representing the specific details of the
        qualification.
    :type value: str or None
    :ivar state: Describes the current state or status of the qualification.
    :type state: str or None
    :ivar issuer: The name of the issuer or body that granted the qualification.
    :type issuer: str or None
    :ivar secondary_labels: Additional labels or tags associated with the
        qualification.
    :type secondary_labels: list[str] or None
    :ivar start_date: The starting date when the qualification became effective.
    :type start_date: DateType or None
    :ivar end_date: The date when the qualification is no longer effective.
    :type end_date: DateType or None
    """
    def __init__(self,
                 qualification_type:str,
                 value:str=None,
                 state:str=None,
                 issuer:str=None,
                 secondary_labels:list[str]=None,
                 start_date:DateType=None,
                 end_date:DateType=None):
        self.qualification_type = qualification_type
        self.value = value
        self.state = state
        self.issuer = issuer
        self.secondary_labels = secondary_labels
        self.start_date = start_date
        self.end_date = end_date