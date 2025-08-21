from neo4j.time import DateType
from dataclasses import dataclass
from typing import Literal

class Qualification:

    def __init__(self,
                 qualification_type:str,
                 value:str=None,
                 state:str=None,
                 issuer:str=None,
                 secondary_labels:list[str]=None,
                 start_date:DateType=None,
                 end_date:DateType=None,
                 sourced_from:str=None,):
        self.qualification_type = qualification_type
        self.value = value
        self.state = state
        self.issuer = issuer
        self.secondary_labels = secondary_labels
        self.start_date = start_date
        self.end_date = end_date
        self.sourced_from = sourced_from

    def __repr__(self):
        return (f"<Qualification(qualification_type={self.qualification_type}, "
                f"value={self.value}, "
                f"state={self.state}, "
                f"issuer={self.issuer}, "
                f"secondary_labels={self.secondary_labels}, "
                f"start_date={self.start_date}, "
                f"end_date={self.end_date}, "
                f"sourced_from={self.sourced_from})>")

@dataclass
class QualificationResult:
    kind: Literal["qualification"]
    value: Qualification | None