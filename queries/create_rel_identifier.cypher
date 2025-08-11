CALL apoc.cypher.doIt(
  'MATCH (o:' + $parent_labels + '), (n:' + $identifier_labels + ')
   WHERE elementId(o) = $parent_element_id AND elementId(n) = $identifier_element_id
   CALL apoc.create.relationship(o, $rel_type, {}, n) YIELD rel
   RETURN type(rel) AS rel_type,
          labels(o) AS from_labels,
          id(o) AS from_element_id,
          labels(n) AS to_labels,
          id(n) AS to_element_id,
          rel',
  {
    parent_labels: $parent_labels,
    parent_element_id: $parent_element_id,
    identifier_labels: $identifier_labels,
    identifier_element_id: $identifier_element_id,
    rel_type: $rel_type
  }
) YIELD value
RETURN value