


class Person:
    """
    Represents an individual with basic name attributes.

    This class is designed to store information about a person, including their title,
    first name, last name, and middle name. It provides a clear string representation
    for instances of this class to make debugging and representation straightforward.

    :ivar title: Represents the title of the person, such as "Mr.", "Ms.", or "Dr.".
    :type title: str
    :ivar first_name: Represents the first name of the person.
    :type first_name: str
    :ivar last_name: Represents the last name of the person.
    :type last_name: str
    :ivar middle_name: Represents the middle name of the person, if any.
    :type middle_name: str
    """
    def __init__(self, title: str=None,
                 first_name: str=None,
                 last_name: str=None,
                 middle_name: str=None,):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def __repr__(self):
        """
        Provides a string representation of the Person object, including its title,
        first name, last name, and middle name.

        :return: A formatted string representing the Person instance.
        :rtype: str
        """
        return (f"<Person(title={self.title}, "
                f"first_name={self.first_name}, "
                f"last_name={self.last_name}, "
                f"middle_name={self.middle_name})>")