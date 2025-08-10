MATCH (o:Organization), (n:NPI:Identifier)
WHERE elementId(o) = $org_element_id
  AND elementId(n) = $npi_element_id
MERGE (o)-[:HAS_NPI_ID]->(n)