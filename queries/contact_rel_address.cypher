MATCH (contact:Contact), (address:Address)
WHERE elementId(contact) = $contact_element_id
  AND elementId(address) = $address_element_id
MERGE (contact)-[:ADDRESS_IS]->(address)