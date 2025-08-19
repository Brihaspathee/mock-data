CALL apoc.cypher.doIt(
  'MATCH (o:' + $source_label + '), (n:' + $target_label + ')
   WHERE elementId(o) = $source_element_id AND elementId(n) = $target_element_id
   CALL apoc.create.relationship(o, $rel_type, {}, n) YIELD rel
   RETURN type(rel) AS rel_type,
          labels(o) AS from_labels,
          id(o) AS from_element_id,
          labels(n) AS to_labels,
          id(n) AS to_element_id,
          rel',
  {
    source_label: $source_label,
    source_element_id: $source_element_id,
    target_label: $target_label,
    target_element_id: $target_element_id,
    rel_type: $rel_type
  }
) YIELD value
RETURN value