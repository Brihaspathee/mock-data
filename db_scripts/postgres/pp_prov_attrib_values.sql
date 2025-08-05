-- auto-generated definition
create table pp_prov_attrib_values
(
    id                integer not null
        constraint pp_prov_attrib_values_pk
            primary key,
    prov_attribute_id integer
        constraint pp_prov_attrib_values_pp_prov_attrib_id_fk
            references pp_prov_attrib,
    field_id          integer
        constraint pp_prov_attrib_values_fmg_attribute_fields_id_fk
            references fmg_attribute_fields,
    value             varchar,
    value_date        date,
    value_number      numeric
);

alter table pp_prov_attrib_values
    owner to porticoadmin;

