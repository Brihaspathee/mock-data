from neo4j.time import Date

from models.aton import Qualification, Contact
from models.aton.identifier import Identifier
from models.aton.role_instance import RoleInstance


class Organization:
    """
    Represents an organization and its related attributes.

    This class provides a structure to encapsulate the details of an organization,
    along with its associated attributes like identifiers, qualifications, and
    contacts. It allows tracking of basic details such as name, type, and
    popularity, while also managing additional information such as whether the
    organization is capitated or has specific practitioner requirements.

    :ivar element_id: A unique identifier for the organization element.
    :type element_id: str
    :ivar name: The name of the organization.
    :type name: str
    :ivar alias_name: An alternative name or alias for the organization.
    :type alias_name: str | None
    :ivar description: A detailed description of the organization.
    :type description: str | None
    :ivar type: The type of the organization.
    :type type: str | None
    :ivar capitated: Indicates whether the organization is capitated.
    :type capitated: bool
    :ivar pcp_practitioner_required: States if a Primary Care Practitioner (PCP)
        is required for the organization.
    :type pcp_practitioner_required: bool
    :ivar atypical: Indicates if the organization is considered atypical.
    :type atypical: bool
    :ivar popularity: The popularity metric of the organization.
    :type popularity: float
    :ivar identifiers: A list of identifiers associated with the organization.
    :type identifiers: list
    :ivar qualifications: A list of qualifications associated with the organization.
    :type qualifications: list[Qualification] | None
    :ivar contacts: A list of contacts associated with the organization.
    :type contacts: list[Contact] | None
    """
    def __init__(self, name: str,
                 alias_name: str=None,
                 description: str=None,
                 type: str=None,
                 capitated: bool = False,
                 pcp_practitioner_required: bool = False,
                 atypical: bool = False,
                 popularity: float = 0.0,
                 identifiers=None,
                 qualifications: list[Qualification] | None =None,
                 contacts: list[Contact] | None =None,):
        if identifiers is None:
            self.identifiers = []
        else:
            self.identifiers = identifiers
        if qualifications is None:
            self.qualifications = []
        else:
            self.qualifications = qualifications
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts
        self.name = name
        self.alias_name = alias_name
        self.description = description
        self.type = type
        self.capitated = capitated
        self.pcp_practitioner_required = pcp_practitioner_required
        self.atypical = atypical
        self.popularity = popularity

    roleInstances: list[RoleInstance] = []

    def __repr__(self):
        """
        Generate the official string representation of the Organization object.

        This method returns a string that provides a formal representation of the Organization
        object, including its main attributes, in a structured format. The returned string is
        helpful for debugging and administrative purposes, offering a clear and concise overview
        of the object's state.

        :return: A string representing the Organization object with its detailed attributes and
                 current state.
        :rtype: str
        """
        return (f"<Organization( "
                f"name={self.name}, "
                f"alias_name={self.alias_name}, "
                f"description={self.description},"
                f"type={self.type}, "
                f"capitated={self.capitated}, "
                f"pcp_practitioner_required={self.pcp_practitioner_required}, "
                f"atypical={self.atypical}, "
                f"popularity={self.popularity})>")