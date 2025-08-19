MATCH (contact:Contact), (telecom:Telecom)
WHERE elementId(contact) = $contact_element_id
  AND elementId(telecom) = $telecom_element_id
MERGE (contact)-[:TELECOM_IS]->(telecom)