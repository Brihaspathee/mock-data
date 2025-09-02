from models.aton import Contact
from models.aton.location import Location


class RoleLocation:
    element_id: str = None
    location: Location = None
    contacts: list[Contact] = []

    def __repr__(self):
        """
        Provides a string representation of the RoleLocation object. This is primarily for
        debugging and logging purposes, offering a clear and human-readable summary of the
        location attribute of the RoleLocation instance.

        :return: A string representation of the RoleLocation object in the format
                 "<RoleLocation(location=...)>".
        :rtype: str
        """

        return (f"<RoleLocation("
                f"element_id={self.element_id},"
                f"location={self.location})>")