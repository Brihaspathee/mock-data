MATCH (o:Organization), (qual:Certification:Qualification)
WHERE elementId(o) = $org_element_id
  AND elementId(qual) = $qual_element_id
MERGE (o)-[:HAS_QUALIFICATION]->(qual)