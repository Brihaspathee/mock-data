from neo4j.time import DateType
from dataclasses import dataclass
from typing import Literal

class Qualification:
    """
    Represents a qualification with information about its type, value, issuer, status, and relevant
    details such as level, specialty, and validity period.

    This class is designed to encapsulate various attributes of a qualification. It is intended
    to store information about the type of qualification, its current status, the entity or organization
    that issued the qualification, and other optional metadata such as level, specialty, and
    applicable dates.

    :ivar qualification_type: Specifies the type of qualification (e.g., certification, license).
    :type qualification_type: str
    :ivar value: Optional value associated with the qualification (e.g., ID or unique identifier).
    :type value: str or None
    :ivar state: Optional state or region for which the qualification is relevant.
    :type state: str or None
    :ivar issuer: Optional issuer or organization responsible for issuing the qualification.
    :type issuer: str or None
    :ivar status: Optional current status of the qualification (e.g., active, expired).
    :type status: str or None
    :ivar level: Optional level or rank of the qualification (e.g., beginner, expert).
    :type level: str or None
    :ivar specialty: Optional area of specialization associated with the qualification.
    :type specialty: str or None
    :ivar secondary_labels: Optional secondary attributes or labels to group or categorize
        the qualification.
    :type secondary_labels: list[str] or None
    :ivar start_date: Optional start date indicating the validity start of the qualification.
    :type start_date: DateType or None
    :ivar end_date: Optional end date indicating the validity end of the qualification.
    :type end_date: DateType or None
    """
    def __init__(self,
                 qualification_type:str,
                 value:str=None,
                 state:str=None,
                 issuer:str=None,
                 status:str=None,
                 level:str=None,
                 specialty:str=None,
                 secondary_labels:list[str]=None,
                 start_date:DateType=None,
                 end_date:DateType=None):
        self.qualification_type = qualification_type
        self.value = value
        self.state = state
        self.issuer = issuer
        self.status = status
        self.level = level
        self.specialty = specialty
        self.secondary_labels = secondary_labels
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        """
        Provides a string representation of the Qualification object, summarizing its key attributes.
        This method returns a concise description that can be useful during debugging or logging.

        :return: A string representation of the Qualification object.
        :rtype: str
        """
        return (f"<Qualification(qualification_type={self.qualification_type}, "
                f"value={self.value}, "
                f"state={self.state}, "
                f"issuer={self.issuer}, "
                f"status={self.status}, "
                f"level={self.level}, "
                f"specialty={self.specialty},"
                f"secondary_labels={self.secondary_labels}, "
                f"start_date={self.start_date}, "
                f"end_date={self.end_date})>")


@dataclass
class QualificationResult:
    """
    Represents the result of a qualification process.

    This data class is used to model the outcome of a qualification process
    with details about the kind of result and the associated qualification
    value. It serves as a structured way to capture and work with
    qualification-related information in a system.

    :ivar kind: The type of the result, indicating a qualification.
    :type kind: Literal["qualification"]
    :ivar value: The qualification obtained or None if no qualification is
        present.
    :type value: Qualification or None
    """
    kind: Literal["qualification"]
    value: Qualification | None