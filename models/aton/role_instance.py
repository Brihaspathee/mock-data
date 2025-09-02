from models.aton.practitioner import Practitioner
from models.aton.role_location import RoleLocation
from models.aton.role_network import RoleNetwork


class RoleInstance:
    element_id: str = None
    practitioner: Practitioner | None = None
    roleLocations: list[RoleLocation] = []
    roleNetworks: list[RoleNetwork] = []

    def __repr__(self):
        """
        Generate the official string representation of the RoleInstance object.
        """
        return (f"<RoleInstance("
                f"element_id={self.element_id},"
                f"practitioner={self.practitioner}, "
                f"roleLocations={self.roleLocations}, "
                f"roleNetworks={self.roleNetworks})>")


