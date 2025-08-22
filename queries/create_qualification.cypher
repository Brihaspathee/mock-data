CREATE (qual:Certification:Qualification{type:$type, value:$value,
                         issuer: $issuer,
                         state: $state,
                         status: $status,
                         level: $level,
                         specialty: $specialty,
                         startDate: $start_date,
                         endDate: $end_date
        })
RETURN qual