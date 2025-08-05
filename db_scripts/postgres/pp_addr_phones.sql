-- auto-generated definition
create table pp_addr_phones
(
    id         integer not null
        constraint pp_addr_phones_pk
            primary key,
    address_id integer
        constraint pp_addr_phones_pp_addr_id_fk
            references pp_addr,
    phone_id   integer
        constraint pp_addr_phones_pp_phones_id_fk
            references pp_phones
);

alter table pp_addr_phones
    owner to porticoadmin;

