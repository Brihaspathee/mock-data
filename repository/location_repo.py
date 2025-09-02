from neo4j.graph import Node
from db.aton_graph_db import get_session
import logging
from repository.validation_repo import create_validation
from models.aton.location import Location
from models.aton.validation import Validation

log = logging.getLogger(__name__)

def get_location_by_smarty_key(smarty_key: str) -> Node | None:
    with open("queries/match_location.cypher", "r") as f:
        query = f.read()

    with get_session() as session:
        result = session.run(query, smarty_key=smarty_key)
        record = result.single()
        if record:
            log.info(f"location matched for smarty key {smarty_key}: {record["location"]}")
            return record["location"]
        else:
            # log.info(f"location not found for smarty key: {smarty_key}")
            return None

def create_location(transaction, location: Location):
    with open("queries/create_location.cypher", "r") as f:
        query = f.read()
    result = transaction.run(query, loc_name=location.location_name,
                             street_address=location.street_address,
                             secondary_address=location.secondary_address,
                             city=location.city,
                             state=location.state,
                             zip_code=location.zip_code,
                             county=location.county,
                             county_fips=location.fips,
                             latitude=location.latitude,
                             longitude=location.longitude)
    record = result.single()
    if record:
        location_node = record["location"]
        log.info(f"Location {location.location_name} smarty key is {location.smarty_key}")
        if location.smarty_key:
            log.info(f"About to create the validation for location")
            validation: Validation = Validation(type="Address", source="Smarty", key=location.smarty_key)
            create_validation(transaction, location_node, validation)
        return location_node
    else:
        return None
