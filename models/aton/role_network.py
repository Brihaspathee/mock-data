from neo4j.time import DateType

from models.aton.network import Network
from models.aton.role_location import RoleLocation

class RoleLocationServes:
    """
    Represents the relationship between a role and the location it serves over a specific period.

    This class is used to track the details of when a role is actively serving a specific location,
    including the start and end dates of the term, as well as the reason for termination, if applicable.

    :ivar start_date: The date when the role begins serving the location.
    :type start_date: DateType
    :ivar end_date: The date when the role terminates serving the location.
    :type end_date: DateType
    :ivar term_reason: The reason why the role stopped serving at the location.
    :type term_reason: str
    """
    start_date: DateType = None
    end_date: DateType = None
    term_reason: str = None

    def __repr__(self):
        """
        Generate the official string representation of the RoleLocationServes object.
        """
        return (f"<RoleLocationServes(start_date={self.start_date}, "
                f"end_date={self.end_date}, term_reason={self.term_reason})>")

class AssociatedLocation:
    """
    Represents an association between a location and roles or services.

    This class is used to define a relationship between a specific location
    and corresponding roles or services it serves. It simplifies managing
    such associations and provides attributes to hold the related data.

    :ivar roleLocation: The primary role or location associated with this instance.
    :type roleLocation: RoleLocation
    :ivar role_location_serves: A list of services or roles associated with
        the primary location.
    :type role_location_serves: list[RoleLocationServes]
    """
    roleLocation: RoleLocation = None
    role_location_serves: list[RoleLocationServes] = []
    def __repr__(self):
        """
        Generate the official string representation of the AssociatedLocation object.
        """
        return (f"<AssociatedLocation(roleLocation={self.roleLocation}, "
                f"role_location_serves={self.role_location_serves})>")

class RoleNetwork:
    """
    Represents a role-based network system managing associated locations.

    This class facilitates the organization and handling of network-specific
    roles and their corresponding locations. It ensures that there is a defined
    network and a list of locations associated with the roles within the
    network. This structure is designed to support operations and logic
    concerning role-based access or relationships.

    :ivar network: The network associated with the role. Represents the main
        network object that this role is tied to.
    :type network: Network
    :ivar associated_locations: List of locations associated with the specific
        role in the network. Each location represents details tied to the role
        in question.
    :type associated_locations: list[AssociatedLocation]
    """
    element_id: str = None
    network: Network = None
    associated_locations: list[AssociatedLocation] = []

    def __repr__(self):
        """
        Generate the official string representation of the RoleNetwork object.
        """
        return (f"<RoleNetwork("
                f"element_id={self.element_id},"
                f"network={self.network}, "
                f"associated_locations={self.associated_locations})>")



