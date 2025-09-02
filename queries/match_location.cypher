MATCH (location:Location)-[:VALIDATED]->(validation:Validation {smarty_key: $smarty_key})
RETURN location, validation