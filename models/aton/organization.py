from neo4j.time import Date


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
                 alias_name: str, description: str,
                 type: str,
                 capitated: bool = False,
                 effective_date: Date = None,
                 sourced_from: str = None):
        self.element_id = ""
        self.name = name
        self.alias_name = alias_name
        self.description = description
        self.type = type
        self.effective_date = effective_date
        self.capitated = capitated
        self.sourced_from = sourced_from