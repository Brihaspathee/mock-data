MATCH (o:Organization), (contact:Contact)
WHERE elementId(o) = $org_element_id
  AND elementId(contact) = $contact_element_id
MERGE (o)-[:HAS_ORGANIZATIONAL_CONTACT]->(contact)