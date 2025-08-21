CALL apoc.create.node(
  ['Identifier', $identifier_label],
  {
    value: $value,
    startDate: coalesce($start_date, null),
    endDate: coalesce($end_date, null),
    legalName: coalesce($legal_name, null)
  }
) YIELD node
RETURN node