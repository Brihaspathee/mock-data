
class Telecom:
    """
    Represents a telecommunications contact.

    This class encapsulates various types of telecommunications information,
    including phone numbers, fax, TTY (text telephone), after-hours contact
    numbers, email addresses, and websites. It provides a structured way to
    store and manage telecom-related details.

    :ivar phone: The primary phone number.
    :type phone: str
    :ivar fax: The fax number.
    :type fax: str
    :ivar tty: The TTY (text telephone) number.
    :type tty: str
    :ivar after_hours_number: The contact number for after-hours communications.
    :type after_hours_number: str
    :ivar email: The email address.
    :type email: str
    :ivar website: The website URL.
    :type website: str
    """
    def __init__(self, phone: str = None,
                 fax: str = None,
                 tty: str = None,
                 after_hours_number: str = None,
                 email: str = None,
                 secure_email: str = None,
                 website: str = None):
        self.phone = phone
        self.fax = fax
        self.tty = tty
        self.after_hours_number = after_hours_number
        self.email = email
        self.secure_email = secure_email
        self.website = website

    def __repr__(self):
        """
        Provides a string representation of the Telecom object suitable for debugging
        purposes. The output string includes all main attributes of the Telecom instance
        formatted in a readable manner.

        :return: A string representing the Telecom object with its attribute values.
        :rtype: str
        """
        return (f"<Telecom(phone={self.phone}, "
                f"fax={self.fax}, "
                f"tty={self.tty}, "
                f"after_hours_number={self.after_hours_number}, "
                f"email={self.email}, "
                f"secure_email={self.secure_email},"
                f"website={self.website})>")