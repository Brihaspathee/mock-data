from sqlalchemy.orm import joinedload, Session

from db import PorticoDB
from models.portico import PPProv, PPAddr, PPProvAddr, PPAddrPhones
from typing import cast

"""
This module contains the ProviderRead class, which is responsible for reading provider data from the database.
"""

class ProviderRead:
    """
    Handles operations related to reading provider data from the database.

    This class is designed to interface with a database using SQLAlchemy sessions.
    It initializes a database connection, allows reading of provider information,
    and ensures proper session and connection management.

    :ivar portico_db: Instance of `PorticoDB` used for managing database connections.
    :type portico_db: PorticoDB
    :ivar db_session: The SQLAlchemy session used for database operations.
    :type db_session: Session
    """
    def __init__(self):
        """
        A class responsible for initializing and managing the connection to the Portico database.

        The class is designed to handle the setup process for database communication, including
        instantiating a database object, establishing a connection, and retrieving a session
        for database interactions.

        Attributes
        ----------
        portico_db : PorticoDB
            Initializes and manages the database connection.
        db_session : Session
            Provides a session object for database operations.
        """
        print("Initializing ProviderRead")
        self.portico_db: PorticoDB = PorticoDB()
        self.portico_db.connect()
        self.db_session: Session = self.portico_db.get_session()


    def read_provider(self) -> list[PPProv] | None:
        """
        Reads the providers from the database, returns a list of providers, or
        None if there are issues during the execution. The method also ensures
        that related data (addresses, phones, and provider types) are pulled
        using efficient joined loading techniques.

        :return: A list of `PPProv` instances containing detailed provider
            information, or None if an error occurs during the process.
        :rtype: list[PPProv] | None
        """
        # db_session: Session = connect_to_portico_db()
        print("Reading providers")
        providers: list[type[PPProv]] = []
        try:
            providers: list[PPProv] = cast(list[PPProv],
                self.db_session.query(PPProv)
                .options(
                    joinedload(PPProv.addresses)
                        .joinedload(PPProvAddr.address)
                        .joinedload(PPAddr.phones)
                        .joinedload(PPAddrPhones.phone),
                    joinedload(PPProv.prov_type)
                )
                .all()
            )
            return providers

        except Exception as e:
            self.db_session.rollback()
            print("Error: ", e, "\n")

        finally:
            print("Closing DB connections")
            self.db_session.close()
            self.portico_db.close()
