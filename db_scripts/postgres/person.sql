-- auto-generated definition
create table person
(
    id   integer default nextval('person_id_seq'::regclass) not null
        constraint person_pk
            primary key,
    name varchar                                            not null,
    age  integer                                            not null
);

alter table person
    owner to porticoadmin;

