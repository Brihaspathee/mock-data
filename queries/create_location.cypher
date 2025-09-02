CREATE (location:Location:MockDataTest{name:$loc_name,
            street_address: $street_address, secondary_address: $secondary_address,
            city: $city, state: $state, zip_code: $zip_code, county: $county,
            county_fips: $county_fips, latitude: $latitude, longitude: $longitude
        })
RETURN location