from neo4j.time import DateType
from dataclasses import dataclass
from typing import Literal

class Identifier:
    def __init__(self, identifier_type: str=None,
                 identifier_label: str=None,
                 identifier_rel:str=None,
                 value: str=None,
                 state: str=None,
                 legal_name: str=None,
                 start_date:DateType=None,
                 end_date:DateType=None,
                 sourced_from: str = None,):
        self.identifier_type = identifier_type
        self.identifier_label = identifier_label
        self.identifier_rel = identifier_rel
        self.value = value
        self.state = state
        self.legal_name = legal_name
        self.start_date = start_date
        self.end_date = end_date
        self.sourced_from = sourced_from

    def __str__(self):
        return (f"Identifier Type: {self.identifier_type}, "
                f"Identifier Value: {self.value},"
                f"Identifier State: {self.state},"
                f"Identifier Label: {self.identifier_label},"
                f"Identifier Relationship: {self.identifier_rel},"
                f"Identifier Legal Name: {self.legal_name},"
                f"Identifier Start Date: {self.start_date}, "
                f"Identifier End Date: {self.end_date}")

@dataclass
class IdentifierResult:
    kind: Literal["identifier"]
    value: Identifier
