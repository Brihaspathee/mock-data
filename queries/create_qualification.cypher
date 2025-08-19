CREATE (qual:Certification:Qualification{type:$type, value:$value,
                         startDate: $start_date,
                         endDate: $end_date,
                         sourcedFrom: $sourced_from
        })
RETURN qual