-- auto-generated definition
create table pp_prov
(
    id           integer not null
        constraint pp_prov_pk
            primary key,
    name         varchar not null,
    tin_id       integer not null
        constraint pp_prov_pp_prov_tin_id_fk
            references pp_prov_tin,
    prov_type_id integer not null
        constraint pp_prov_pp_prov_type_id_fk
            references pp_prov_type,
    address_id   integer not null
        constraint pp_prov_pp_addr_id_fk
            references pp_addr,
    specialty_id integer not null
        constraint pp_prov_pp_spec_id_fk
            references pp_spec
);

alter table pp_prov
    owner to porticoadmin;

