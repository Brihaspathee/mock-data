-- 1. Create FMG_ATTRIBUTE_TYPES table
create table portown.fmg_attribute_types
(
    id          integer not null
        constraint fmg_attribute_types_pk
            primary key,
    metatype    varchar not null,
    description varchar
);

alter table portown.fmg_attribute_types
    owner to porticoadmin;

-- 2. Create FMG_ATTRIBUTE_FIELDS table
create table portown.fmg_attribute_fields
(
    id           integer not null
        constraint fmg_attribute_fields_pk
            primary key,
    attribute_id integer not null
        constraint fmg_attribute_fields_fmg_attribute_types_id_fk
            references portown.fmg_attribute_types,
    fmgcode      varchar,
    field_name   varchar not null,
    datatype     varchar not null
);

alter table portown.fmg_attribute_fields
    owner to porticoadmin;

-- 3. Create PP_PROV_TIN table
create table portown.pp_prov_tin
(
    id   integer not null
        constraint pp_prov_tin_pk
            primary key,
    name varchar not null,
    tin  varchar not null
);

alter table portown.pp_prov_tin
    owner to porticoadmin;


-- 4. Create PP_PROV_TYPE table
create table portown.pp_prov_type
(
    id       integer not null
        constraint pp_prov_type_pk
            primary key,
    type     varchar not null,
    category varchar not null
);

alter table portown.pp_prov_type
    owner to porticoadmin;

-- 5. Create PP_SPEC table
create table portown.pp_spec
(
    id             integer not null
        constraint pp_spec_pk
            primary key,
    type           varchar not null,
    description    varchar not null,
    site_visit_req varchar not null
);

alter table portown.pp_spec
    owner to porticoadmin;

-- 6. Create PP_ADDR table
create table portown.pp_addr
(
    id         integer not null
        constraint id
            primary key,
    type       varchar,
    addr1      varchar not null,
    addr2      varchar,
    city       varchar not null,
    state      varchar not null,
    zip        varchar not null,
    county     varchar,
    latitude   varchar,
    longitude  varchar,
    start_date date,
    end_date   date,
    fips       varchar
);

alter table portown.pp_addr
    owner to porticoadmin;

-- 7. Create PP_PHONES table
create table portown.pp_phones
(
    id        integer not null
        constraint pp_phones_pk
            primary key,
    type      varchar not null,
    area_code varchar not null,
    exchange  varchar not null,
    number    varchar not null
);

alter table portown.pp_phones
    owner to porticoadmin;

-- 8. Create PP_PROV table
create table portown.pp_prov
(
    id           integer not null
        constraint pp_prov_pk
            primary key,
    name         varchar not null,
    tin_id       integer not null
        constraint pp_prov_pp_prov_tin_id_fk
            references portown.pp_prov_tin,
    prov_type_id integer not null
        constraint pp_prov_pp_prov_type_id_fk
            references portown.pp_prov_type,
    address_id   integer not null
        constraint pp_prov_pp_addr_id_fk
            references portown.pp_addr,
    specialty_id integer not null
        constraint pp_prov_pp_spec_id_fk
            references portown.pp_spec
);

alter table portown.pp_prov
    owner to porticoadmin;

-- 9. Create PP_ADDR_PHONES table
create table portown.pp_addr_phones
(
    id         integer not null
        constraint pp_addr_phones_pk
            primary key,
    address_id integer
        constraint pp_addr_phones_pp_addr_id_fk
            references portown.pp_addr,
    phone_id   integer
        constraint pp_addr_phones_pp_phones_id_fk
            references portown.pp_phones
);

alter table portown.pp_addr_phones
    owner to porticoadmin;

-- 10. Create PP_PROV_ADDR table
create table portown.pp_prov_addr
(
    id         integer not null
        constraint pp_prov_addr_pk
            primary key,
    prov_id    integer
        constraint pp_prov_addr_pp_prov_id_fk
            references portown.pp_prov,
    address_id integer
        constraint pp_prov_addr_pp_addr_id_fk
            references portown.pp_addr
);

alter table portown.pp_prov_addr
    owner to porticoadmin;

-- 11. Create PP_PROV_ATTRIB table
create table portown.pp_prov_attrib
(
    id           integer not null
        constraint pp_prov_attrib_pk
            primary key,
    prov_id      integer
        constraint pp_prov_attrib_pp_prov_id_fk
            references portown.pp_prov,
    attribute_id integer
        constraint pp_prov_attrib_fmg_attribute_types_id_fk
            references portown.fmg_attribute_types
);

alter table portown.pp_prov_attrib
    owner to porticoadmin;

-- 12. Create PP_PROV_ATTRIB_VALUES table
create table portown.pp_prov_attrib_values
(
    id                integer not null
        constraint pp_prov_attrib_values_pk
            primary key,
    prov_attribute_id integer
        constraint pp_prov_attrib_values_pp_prov_attrib_id_fk
            references portown.pp_prov_attrib,
    field_id          integer
        constraint pp_prov_attrib_values_fmg_attribute_fields_id_fk
            references portown.fmg_attribute_fields,
    value             varchar,
    value_date        date,
    value_number      numeric
);

alter table portown.pp_prov_attrib_values
    owner to porticoadmin;


