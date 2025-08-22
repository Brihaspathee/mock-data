from neo4j.time import DateType
from dataclasses import dataclass
from typing import Literal

class Identifier:
    """
    Represents an identifier with associated attributes and metadata.

    This class encapsulates various attributes of an identifier, such as its type,
    label, relationship, value, state, and more. It is designed to store and
    provide a standardized format for identity-related information, making it
    useful in contexts where such details need to be managed or exchanged.

    Instances of this class can include additional attributes like the legal name
    associated with the identifier, its valid duration (start and end dates),
    and the source from which the identifier is obtained.

    :ivar identifier_type: Specifies the type of the identifier.
    :type identifier_type: str
    :ivar identifier_label: Label associated with the identifier.
    :type identifier_label: str
    :ivar identifier_rel: Relationship context of the identifier.
    :type identifier_rel: str
    :ivar value: The value of the identifier.
    :type value: str
    :ivar state: State or status of the identifier.
    :type state: str
    :ivar legal_name: Legal name related to the identifier.
    :type legal_name: str
    :ivar start_date: The starting date of the identifier's validity.
    :type start_date: DateType
    :ivar end_date: The ending date of the identifier's validity.
    :type end_date: DateType
    :ivar sourced_from: Source information of the identifier.
    :type sourced_from: str
    """
    def __init__(self, identifier_type: str=None,
                 identifier_label: str=None,
                 identifier_rel:str=None,
                 value: str=None,
                 state: str=None,
                 legal_name: str=None,
                 start_date:DateType=None,
                 end_date:DateType=None,
                 sourced_from: str = None,):
        self.identifier_type = identifier_type
        self.identifier_label = identifier_label
        self.identifier_rel = identifier_rel
        self.value = value
        self.state = state
        self.legal_name = legal_name
        self.start_date = start_date
        self.end_date = end_date
        self.sourced_from = sourced_from

    def __str__(self):
        """
        Provides a string representation of the object including its identifier type,
        value, state, label, relationship, legal name, start date, and end date.

        :return: A string containing the formatted details of the object's attributes.
        :rtype: str
        """
        return (f"Identifier Type: {self.identifier_type}, "
                f"Identifier Value: {self.value},"
                f"Identifier State: {self.state},"
                f"Identifier Label: {self.identifier_label},"
                f"Identifier Relationship: {self.identifier_rel},"
                f"Identifier Legal Name: {self.legal_name},"
                f"Identifier Start Date: {self.start_date}, "
                f"Identifier End Date: {self.end_date}")


@dataclass
class IdentifierResult:
    """
    Represents the result of an identifier found during some processing.

    This class is used to encapsulate the information about an identifier, including
    its kind and value. It provides a standard way to store and access the result
    related to identifiers.

    :ivar kind: Specifies the type of result. This value is always "identifier".
    :type kind: Literal["identifier"]
    :ivar value: The value of the identifier found.
    :type value: Identifier
    """
    kind: Literal["identifier"]
    value: Identifier
