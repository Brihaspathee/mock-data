CREATE (address:Address{streetAddress:$street_address,
          secondaryAddress: $secondary_address,
          city:$city,
          state: $state,
          zip: $zip,
          county: $county,
          fips: $fips,
          latitude: $latitude,
          longitude: $longitude
        })
RETURN address