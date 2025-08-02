from datetime import datetime
from neo4j.time import Date

class DBUtils:

    @staticmethod
    def convert_date_to_neo4j_date(effective_date_str:str):
        return Date.from_native(datetime.strptime(effective_date_str, "%Y-%m-%d").date())