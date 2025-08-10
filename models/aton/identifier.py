from neo4j.time import DateType


class Identifier:
    def __init__(self, identifierType: str,
                 value: str=None,
                 legal_name: str=None,
                 start_date:DateType=None,
                 end_date:DateType=None,
                 sourced_from: str = None,):
        self.identifierType = identifierType
        self.value = value
        self.legal_name = legal_name
        self.startDate = start_date
        self.endDate = end_date
        self.sourced_from = sourced_from