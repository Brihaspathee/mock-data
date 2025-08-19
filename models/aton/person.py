from models.aton import Telecom


class Person:

    def __init__(self, title: str=None,
                 first_name: str=None,
                 last_name: str=None,
                 middle_name: str=None,):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def __repr__(self):
        return (f"<Person(title={self.title}, "
                f"first_name={self.first_name}, "
                f"last_name={self.last_name}, "
                f"middle_name={self.middle_name})>")