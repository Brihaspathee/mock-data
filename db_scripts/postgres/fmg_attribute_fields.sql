-- auto-generated definition
create table fmg_attribute_fields
(
    id           integer not null
        constraint fmg_attribute_fields_pk
            primary key,
    attribute_id integer not null
        constraint fmg_attribute_fields_fmg_attribute_types_id_fk
            references fmg_attribute_types,
    fmgcode      varchar,
    field_name   varchar not null,
    datatype     varchar not null
);

alter table fmg_attribute_fields
    owner to porticoadmin;

