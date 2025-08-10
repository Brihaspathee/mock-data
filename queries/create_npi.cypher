CREATE (npi:NPI:Identifier{value:$value,
                         startDate: $start_date,
                         endDate: $end_date,
                         sourcedFrom: $sourced_from
        })
RETURN npi