
from models.aton import Address, Telecom, Person


class Contact:

    def __init__(self, use: str,
                 address: Address=None,
                 telecom: Telecom=None,
                 person: Person=None):
        self.use = use
        self.address = address
        self.telecom = telecom
        self.person = person

    def __repr__(self):
        return (f"<Contact(use={self.use}, "
                f"address={self.address}, "
                f"telecom={self.telecom}, "
                f"person={self.person})>")