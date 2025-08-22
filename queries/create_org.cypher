CREATE (org:Organization{name:$org_name,
            aliasName:$alias_name, type: $type,
                         description: $description,
                         capitated: $capitated,
                         pcpAssigment: $pcp_assignment
        })
RETURN org