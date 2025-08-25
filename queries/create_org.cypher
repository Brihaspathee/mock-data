CREATE (org:Organization:MockDataTest{name:$org_name,
            aliasName:$alias_name, type: $type,
                         description: $description,
                         capitated: $capitated,
                         pcpPractitionerRequired: $pcp_practitioner_required,
                         atypical: $atypical, popularity: $popularity
        })
RETURN org