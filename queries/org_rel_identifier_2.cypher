MATCH (o:Organization), (n:TIN:Identifier)
WHERE elementId(o) = $org_element_id
  AND elementId(n) = $tin_element_id
MERGE (o)-[:HAS_TIN]->(n)