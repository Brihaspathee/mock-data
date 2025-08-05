-- auto-generated definition
create table pp_spec
(
    id             integer not null
        constraint pp_spec_pk
            primary key,
    type           varchar not null,
    description    varchar not null,
    site_visit_req varchar not null
);

alter table pp_spec
    owner to porticoadmin;
