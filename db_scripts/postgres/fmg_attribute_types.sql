-- auto-generated definition
create table fmg_attribute_types
(
    id          integer not null
        constraint fmg_attribute_types_pk
            primary key,
    metatype    varchar not null,
    description varchar
);

alter table fmg_attribute_types
    owner to porticoadmin;