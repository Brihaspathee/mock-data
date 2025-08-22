
from models.aton import Address, Telecom, Person


class Contact:
    """
    Represents a contact with associated details.

    This class is used to define and manage contact information, including its
    use case, associated address, telecom details, and an optional person entity.
    It is designed to store and represent compact and structured data for contact
    purposes.

    :ivar use: Describes the purpose or type of the contact (e.g., home, work).
    :type use: str
    :ivar address: Represents the address associated with the contact. Defaults to
        None.
    :type address: Address
    :ivar telecom: Represents the telecom details (e.g., phone, fax) associated
        with the contact. Defaults to None.
    :type telecom: Telecom
    :ivar person: Represents the person associated with the contact. Defaults to
        None.
    :type person: Person
    """
    def __init__(self, use: str,
                 address: Address=None,
                 telecom: Telecom=None,
                 person: Person=None):
        self.use = use
        self.address = address
        self.telecom = telecom
        self.person = person

    def __repr__(self):
        """
        Provides a string representation of the Contact object for debugging and logging
        purposes. The returned string includes details of the Contact's use, address,
        telecom, and associated person in a readable format.

        :return: A string representation of the Contact object containing its use,
            address, telecom, and person information.
        :rtype: str
        """
        return (f"<Contact(use={self.use}, "
                f"address={self.address}, "
                f"telecom={self.telecom}, "
                f"person={self.person})>")