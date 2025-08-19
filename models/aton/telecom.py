class Telecom:

    def __init__(self, phone: str = None,
                 fax: str = None,
                 tty: str = None,
                 after_hours_number: str = None,
                 email: str = None,
                 website: str = None):
        self.phone = phone
        self.fax = fax
        self.tty = tty
        self.after_hours_number = after_hours_number
        self.email = email
        self.website = website

    def __repr__(self):
        return (f"<Telecom(phone={self.phone}, "
                f"fax={self.fax}, "
                f"tty={self.tty}, "
                f"after_hours_number={self.after_hours_number}, "
                f"email={self.email}, "
                f"website={self.website})>")