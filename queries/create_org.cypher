CREATE (org:Organization{name:$org_name,
            aliasName:$alias_name, type: $type,
                         description: $description, effectiveDate: $effective_date,
                         capitated: $capitated,
                         sourcedFrom: $sourced_from
        })
RETURN org