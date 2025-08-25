-- 0. Insert data into PP_NET table
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (37564,'GP','Medicaid - SC',1,NULL),
	 (28,'Centene','Centene',2,NULL),
	 (29,'TX','Texas',3,28),
	 (6236,'IL','Illinois',3,28),
	 (30,'GA','Georgia',3,28),
	 (6336,'CA','California',3,28),
	 (6237,'NLH','NextLevelHealth',4,6236),
	 (6337,'MediCal','Medical',4,6337),
	 (14068,'SUPVEN','Superior Vendors',4,29),
	 (32,'SUP','Superior',4,29);
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (7719,'CENSUP','Cenpatico Superior',4,29),
	 (33,'PS','Peach State',4,30),
	 (7676,'CENPS','Cenpatico Peach State',4,30),
	 (35,'GP','START',5,32),
	 (2441,'GPC','CHIP',5,32),
	 (2442,'GPR','CHIP RSA',5,32),
	 (38,'FC','Star Health',5,32),
	 (37,'PSHP','Peach State Health Plan',5,33),
	 (14629,'DNULVLGA','DNU Legacy VL GA',5,33),
	 (7677,'BH','Cenpatico Peach State Health Plan',5,7676);
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (7722,'BHK','Cenpatico STAR Kids',5,7719),
	 (7726,'KD','Cenpatico CHIP',5,7719),
	 (7728,'KDBH','Cenpatico STAR',5,7719),
	 (14837,'DLIB','DNU LIBNXT',5,6237),
	 (6238,'EN','NextLevel Health Medicaid',5,6237),
	 (7017,'CV','Cal Viva',5,6337),
	 (7018,'CM','Cal Molina',5,6337),
	 (7019,'CD','Cal Dental',5,6337),
	 (14097,'SHSE','Superior Health plan - Starkids ESI',5,14068),
	 (14089,'SHCE','Superior Health plan - CHIPRSA ESA',5,14068);
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (14087,'SHCR','Superioc Health plan - CHIP ESI',5,14068),
	 (14776,'TXDQMD','DentaQuest - Star Medicaid TX - VAL',6,35),
	 (14342,'ACCUSMTX','Accu Reference Star Medicaid TX',6,35),
	 (13899,'CMKMDTX','Caremark Star Medicaid - TX',6,35),
	 (14552,'CPLSMTX','CPL Star Medicaid TX',6,35),
	 (14549,'CPLCIPTX','CPL CHIP TX - VAL',6,2441),
	 (14337,'ACCUCHIPTX','AccuReference CHIP TX - VAL',6,2441),
	 (14339,'BIOCHIPTX','BioReference CHIP TX - VAL',6,2441),
	 (14421,'QSTCHIPTX','Quest CHIP TX - VAL',6,2441),
	 (14518,'LCCCHIPTX','Labcorp CHIP TX - VAL',6,2441);
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (46,'FC','TX Star Health Foster Care',6,38),
	 (3258,'USFCTX','US Script - Star Health Foster Care TX',6,38),
	 (13900,'CMKFCTX','Caremark - Star Health Foster Care TX',6,38),
	 (14341,'ACCUUSHFCTX','Accu Reference Star health Foster Care TX',6,38),
	 (47,'MD','Medicaid GA',6,37),
	 (331,'CCPSHP','Care Centrix PSHP',6,37),
	 (332,'DDPSHP','Denta Quest PSHP',6,37),
	 (334,'USPSHP','US Script PSHP',6,37),
	 (14600,'OPTPSHP','Opticare PSHP GA - VAL',6,37),
	 (333,'OCPSHP','Opticare PSHP',6,14629);
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (14045,'ESIGA','ESI PSHP',6,14629),
	 (3781,'CPLPSHP','Clinical Pathology Lan - PSHP',6,14629),
	 (6408,'LCPPSHP','Labcorp PSHP',6,14629),
	 (8417,'ACCUPSHP','Accu Reference PSHP',6,14629),
	 (6406,'QUPSHP','Quest PSHP',6,14629),
	 (7678,'MD','Cenpatico Medicaid GA',6,7677),
	 (7723,'KD','Cenpatico TX CHIP',6,7722),
	 (6257,'MD','NextLevel Health Medicaid',6,6238),
	 (6577,'NIANXT','NIA Next Level Health',6,6238),
	 (6579,'ENVVSNNXT','Envolve Vision Next Level Health',6,6238);
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (6796,'LIBNXT','Liberty Dental Next Level Health',6,6238),
	 (14764,'LIBDNEXTIL','Liberty Dental Next Level Health - VAL',6,6238),
	 (7727,'MD','Cenpatico TX Star',6,7726),
	 (7729,'FC','Cenpatico TX Foster Care',6,7728),
	 (14698,'STARKD','ESI Superior Health Plan - STARKID - VAL',6,14069),
	 (7039,'CV','CV CalViva Standard',6,7017),
	 (7040,'VE','CV CalViva Expansion',6,7017),
	 (7056,'VK','CV CalViva Kaiser',6,7017),
	 (14595,'OPTCVCA','Opticare Calviva CA - VAL',6,7017),
	 (15043,'ASHCA','Ash Calviva CA - VAL',6,7017);
INSERT INTO portown.pp_net (id,ds,dsl,net_level_id,parent_net_id) VALUES
	 (14694,'CHIPRSA','ESI Superior Health Plan - CHIPRSA - VAL',6,14089),
	 (14693,'ESICHIP','ESI Superior Health Plan - CHIP - VAL',6,14087),
	 (7037,'CM','CM Molina Standard',6,7018),
	 (7038,'CG','CM Molina Expansion',6,7018),
	 (7036,'TL','Medi-Cal Dental',6,7019);

-- 1. Insert data into FMG_ATTRIBUTE_TYPES table
INSERT INTO portown.fmg_attribute_types (id,metatype,description) VALUES
	 (100640,'PROV_ACR_ACCRED','ACR Accreditation'),
	 (101277,'PROV_AAAASF_ACCRED','AAAASF Accreditation'),
	 (100638,'PROV_AAAHC_ACCRED','AAAHC Accreditation'),
	 (101278,'PROV_AASM_ACCRED','Provider AASM Accred'),
	 (502,'PROV_NPI','Provider NPI'),
	 (100073,'PROV_MEDICARE_ID','Provider Medicare Id');


-- 2. Insert data into FMG_ATTRIBUTE_FIELDS table
INSERT INTO portown.fmg_attribute_fields (id,attribute_id,fmgcode,field_name,"datatype") VALUES
	 (101143,100640,'YES_NO','ACR Accred?','string'),
	 (102935,100640,NULL,'Validation Date','date'),
	 (101141,100640,NULL,'Effective Date','date'),
	 (102915,100640,NULL,'Expiration Date','date'),
	 (104380,100640,'ACR_ACCRED_LEVEL','Accred level','string'),
	 (101955,101277,'YES_NO','AAAASF Accreditation','string'),
	 (102775,101277,NULL,'Validation Date','date'),
	 (101956,101277,NULL,'Effective Date','date'),
	 (102795,101277,NULL,'Expiration Date','date'),
	 (101136,100638,'YES_NO','AAAHC Accreditation','string');
INSERT INTO portown.fmg_attribute_fields (id,attribute_id,fmgcode,field_name,"datatype") VALUES
	 (102835,100638,NULL,'Validation Date','date'),
	 (101137,100638,NULL,'Effective Date','date'),
	 (102815,100638,NULL,'Expiration Date','date'),
	 (104381,100638,'AAHC_ACCRED_LEVEL','Accred level','string'),
	 (102856,101278,NULL,'endDate','date'),
	 (101957,101278,NULL,'AASM Accreditation','string'),
	 (101958,101278,NULL,'effectiveDate','date'),
	 (709,502,NULL,'endDate','date'),
	 (706,502,NULL,'number','string'),
	 (708,502,NULL,'effectiveDate','date');
INSERT INTO portown.fmg_attribute_fields (id,attribute_id,fmgcode,field_name,"datatype") VALUES
	 (707,502,NULL,'type','string'),
	 (100283,100073,NULL,'number','string');


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
	 (4,1,100640),
	 (5,1,101277),
	 (6,1,100638),
	 (2,1,101278),
	 (1,1,502),
	 (3,1,100073);


-- 12. Insert data into PP_PROV_ATTRIB_VALUES table
INSERT INTO portown.pp_prov_attrib_values (id,prov_attribute_id,field_id,value,value_date,value_number) VALUES
	 (7,4,101143,'Y',NULL,NULL),
	 (8,4,101141,NULL,'2021-05-01',NULL),
	 (9,4,104380,'Breast MRI',NULL,NULL),
	 (10,5,101955,'Y',NULL,NULL),
	 (11,5,101956,NULL,'2022-10-01',NULL),
	 (13,6,101137,NULL,'2018-08-01',NULL),
	 (12,6,101136,'Y',NULL,NULL),
	 (14,6,104381,'Medicare Deemed Status',NULL,NULL),
	 (5,2,101958,'','2020-07-01',NULL),
	 (4,2,101957,'YES',NULL,NULL);
INSERT INTO portown.pp_prov_attrib_values (id,prov_attribute_id,field_id,value,value_date,value_number) VALUES
	 (1,1,706,'235625546',NULL,NULL),
	 (2,1,708,NULL,'2019-01-01',NULL),
	 (3,1,707,'type 1',NULL,NULL),
	 (6,3,100283,'FL34634359',NULL,NULL);

