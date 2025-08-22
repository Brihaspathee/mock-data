from neo4j.time import Date

from models.aton import Qualification, Contact
from models.aton.identifier import Identifier


class Organization:
    """
    Represents an organization entity.

    This class is used to encapsulate information about an organization,
    including its unique identifier, name, alias, description, and whether
    it operates under a capitated model. The `Organization` class provides
    a way to store and manage this information within an application.

    :ivar element_id: The unique identifier of the organization.
    :type element_id: str
    :ivar name: The name of the organization.
    :type name: str
    :ivar alias_name: The alias or alternative name of the organization.
    :type alias_name: str
    :ivar description: A brief description of the organization.
    :type description: str
    :ivar capitated: Indicates whether the organization operates under
        a capitated payment model. Defaults to False.
    :type capitated: bool
    """
    def __init__(self, name: str,
                 alias_name: str=None,
                 description: str=None,
                 type: str=None,
                 capitated: bool = False,
                 pcpAssigment: bool = False,
                 identifiers=None,
                 qualifications: list[Qualification] | None =None,
                 contacts: list[Contact] | None =None,):
        if identifiers is None:
            self.identifiers = []
        if qualifications is None:
            self.qualifications = []
        if contacts is None:
            self.contacts = []
        self.element_id = ""
        self.name = name
        self.alias_name = alias_name
        self.description = description
        self.type = type
        self.capitated = capitated
        self.pcpAssigment = pcpAssigment