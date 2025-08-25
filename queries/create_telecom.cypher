CREATE (telecom:Telecom:MockDataTest{phone:$phone,
          fax: $fax,
          tty:$tty,
          afterHoursNumber: $after_hours_number,
          email: $email,
          secureEmail: $secure_email,
          website: $website
        })
RETURN telecom