CREATE (telecom:Telecom{phone:$phone,
          fax: $fax,
          tty:$tty,
          afterHoursNumber: $after_hours_number,
          email: $email,
          website: $website
        })
RETURN telecom