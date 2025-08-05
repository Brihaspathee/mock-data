-- auto-generated definition
create table pp_prov_attrib
(
    id           integer not null
        constraint pp_prov_attrib_pk
            primary key,
    prov_id      integer
        constraint pp_prov_attrib_pp_prov_id_fk
            references pp_prov,
    attribute_id integer
        constraint pp_prov_attrib_fmg_attribute_types_id_fk
            references fmg_attribute_types
);

alter table pp_prov_attrib
    owner to porticoadmin;