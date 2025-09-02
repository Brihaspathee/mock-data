CALL apoc.create.node(
  ['MockDataTest', $role_label], $props
) YIELD node
RETURN node