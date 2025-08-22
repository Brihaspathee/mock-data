from neo4j.time import DateType
from dataclasses import dataclass
from typing import Literal

class Qualification:
    """
    Represents a qualification entity with details about its type, value,
    state, issuer, and other associated metadata.

    This class is designed to encapsulate the details about a qualification
    that might represent credentials, certifications, licenses, or other forms
    of verifiable qualifications. It includes attributes for metadata such as
    the issuing entity, validity period, and additional labels for further
    categorization.

    :ivar qualification_type: Indicates the type or category of the qualification.
    :type qualification_type: str
    :ivar value: The value or unique identifier associated with the qualification.
    :type value: str, optional
    :ivar state: The current state or status of the qualification (e.g., active,
        inactive, revoked).
    :type state: str, optional
    :ivar issuer: The entity or organization that issued the qualification.
    :type issuer: str, optional
    :ivar secondary_labels: A list of additional descriptors or labels providing
        supplementary information about the qualification.
    :type secondary_labels: list[str], optional
    :ivar start_date: Indicates the start date from which the qualification is
        valid.
    :type start_date: DateType, optional
    :ivar end_date: The expiry or end date of the qualification's validity.
    :type end_date: DateType, optional
    :ivar sourced_from: The source organization or platform where the
        qualification information was retrieved or verified.
    :type sourced_from: str, optional
    """
    def __init__(self,
                 qualification_type:str,
                 value:str=None,
                 state:str=None,
                 issuer:str=None,
                 secondary_labels:list[str]=None,
                 start_date:DateType=None,
                 end_date:DateType=None,
                 sourced_from:str=None,):
        self.qualification_type = qualification_type
        self.value = value
        self.state = state
        self.issuer = issuer
        self.secondary_labels = secondary_labels
        self.start_date = start_date
        self.end_date = end_date
        self.sourced_from = sourced_from

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
                f"secondary_labels={self.secondary_labels}, "
                f"start_date={self.start_date}, "
                f"end_date={self.end_date}, "
                f"sourced_from={self.sourced_from})>")


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