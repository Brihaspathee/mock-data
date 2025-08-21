-- 1. Insert data into FMG_ATTRIBUTE_TYPES table
INSERT INTO portown.fmg_attribute_types (id,metatype,description) VALUES
	 (101,'PROV_NPI','Provider NPI'),
	 (102,'PROV_AASM_CERT','Provider AASM Certification'),
     (103,'PROV_MEDICARE_ID','Provider Medicare Id');;


-- 2. Insert data into FMG_ATTRIBUTE_FIELDS table
INSERT INTO portown.fmg_attribute_fields (id,attribute_id,fmgcode,field_name,"datatype") VALUES
	 (1001,101,NULL,'number','string'),
	 (1002,101,NULL,'effectiveDate','date'),
	 (1003,101,NULL,'endDate','date'),
	 (1004,101,NULL,'type','string'),
	 (1005,102,NULL,'AASM Certification','string'),
	 (1006,102,NULL,'effectiveDate','date'),
	 (1007,102,NULL,'endDate','date'),
     (1008,103,NULL,'number','string');;


-- 3. Insert data into PP_PROV_TIN table
INSERT INTO portown.pp_prov_tin (id,name,tin) VALUES
	 (1,'Kaptured Inc','43-5343234');

-- 4. Insert data into PP_PROV_TYPE table
INSERT INTO portown.pp_prov_type (id,"type",category) VALUES
	 (1,'HOSP','Medical');

-- 5. Insert data into PP_SPEC table
INSERT INTO portown.pp_spec (id,"type",description,site_visit_req) VALUES
	 (1,'Multi-Specialty','Multi Specialty Institution','No');

-- 6. Insert data into PP_ADDR table
INSERT INTO portown.pp_addr (id,"type",addr1,addr2,city,state,zip,county,latitude,longitude,start_date,end_date,fips) VALUES
	 (1,'BILLING','13377 Batten Lane',NULL,'Odessa','FL','33556','Pasco',NULL,NULL,'2020-01-01',NULL,'12101'),
	 (2,'MAILING','P.O.8433',NULL,'Odessa','FL','33556','Pasco',NULL,NULL,'2020-01-01',NULL,'12101');

-- 7. Insert data into PP_PHONES table
INSERT INTO portown.pp_phones (id,"type",area_code,exchange,"number") VALUES
	 (1,'CELL','813','357','9150');


-- 8. Insert data into PP_PROV table
INSERT INTO portown.pp_prov (id,name,tin_id,prov_type_id,address_id,specialty_id) VALUES
	 (1,'Kaptured Hospital',1,1,1,1);

-- 9. Insert data into PP_ADDR_PHONES table
INSERT INTO portown.pp_addr_phones (id,address_id,phone_id) VALUES
	 (1,1,1),
	 (2,2,1);

-- 10. Insert data into PP_PROV_ADDR table
INSERT INTO portown.pp_prov_addr (id,prov_id,address_id) VALUES
	 (1,1,1);

-- 11. Insert data into PP_PROV_ATTRIB table
INSERT INTO portown.pp_prov_attrib (id,prov_id,attribute_id) VALUES
	 (1,1,101),
	 (2,1,102),
	 (3,1,103);;


-- 12. Insert data into PP_PROV_ATTRIB_VALUES table
INSERT INTO portown.pp_prov_attrib_values (id,prov_attribute_id,field_id,value,value_date,value_number) VALUES
	 (1,1,1001,'235625546',NULL,NULL),
	 (2,1,1002,NULL,'2019-01-01',NULL),
	 (3,1,1004,'type 1',NULL,NULL),
	 (4,2,1005,'YES',NULL,NULL),
	 (5,2,1006,'','2020-07-01',NULL),
	 (6,3,1007,'FL34634359',NULL,NULL);
