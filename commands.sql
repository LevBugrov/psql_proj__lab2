CREATE OR REPLACE FUNCTION create_tab_clients
() RETURNS void AS $$
create table if not exists "clients"(
id_client integer primary key,
name text not null,
surname text not null,
telephone integer,
total_money integer
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION create_tab_branches
() RETURNS void AS $$
create table if not exists "branches"(
id_branches integer primary key,
name_br text not null,
address text not null,
telephone integer
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION create_tab_types_of_services
() RETURNS void AS $$
create table if not exists "type_of_services"(
id_tos integer primary key,
name_tos text not null,
type text not null,
price integer
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION create_tab_services
() RETURNS void AS $$
create table if not exists "services"(
branch_id INTEGER,
tos_id INTEGER,
client_id INTEGER,
date_of_receipt text,
FOREIGN KEY(branch_id)
    REFERENCES branches (id_branches)
	ON DELETE CASCADE,
FOREIGN KEY(tos_id)
    REFERENCES type_of_services (id_tos)
	ON DELETE CASCADE,
FOREIGN KEY(client_id)
    REFERENCES clients (id_client)
	ON DELETE CASCADE
);
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_clients ()
    RETURNS TABLE(id_client integer, name text, surname text, telephone integer, total_money integer)
    AS $$
    select * from clients;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_branches ()
    RETURNS TABLE(id_branches integer, name_br text, address text, telephone integer)
    AS $$
    select * from branches;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_tos ()
    RETURNS TABLE(id_tos integer, name_tos text, type text, price integer)
    AS $$
    select * from type_of_services;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION get_services ()
    RETURNS TABLE(branch_id integer, tos_id integer, client_id integer, date_of_receipt text)
    AS $$
    select * from services;
$$ LANGUAGE sql;

-- ADD

create OR REPLACE function add_to_clients(id integer, name text, surname text, telephone integer)
	returns void language sql as $$
		insert into "clients"(id_client, name, surname, telephone) values (id, name, surname, telephone)
	$$;

create OR REPLACE function add_to_branches(id integer, name text, address text, telephone integer)
	returns void language sql as $$
		insert into "branches"(id_branches, name_br, address, telephone) values (id, name, address, telephone)
	$$;

create OR REPLACE function add_to_tos(id integer, name text, type text, price integer)
	returns void language sql as $$
		insert into "type_of_services"(id_tos, name_tos, type, price) values (id, name, type, price)
	$$;

create OR REPLACE function add_to_services(br_id integer, tos_id integer, cl_id integer, date_ text)
	returns void language sql as $$
		insert into "services"(branch_id, tos_id, client_id, date_of_receipt) values (br_id, tos_id, cl_id, date_)
	$$;

--DELETE

CREATE OR REPLACE FUNCTION delete_clients ()
    RETURNS void
    AS $$
    delete from clients;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_branches ()
    RETURNS void
    AS $$
    delete from branches;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_tos ()
    RETURNS void
    AS $$
    delete from type_of_services;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_services ()
    RETURNS void
    AS $$
    delete from services;
$$ LANGUAGE sql;

-- SEARCH BY

CREATE OR REPLACE FUNCTION search_clients_by_name (name_ text)
    RETURNS TABLE(id_client integer, name text, surname text, telephone integer, total_money integer)
    AS $$
    select * from clients where name = name_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION search_branches_by_name (name_ text)
    RETURNS TABLE(id_branches integer, name_br text, address text, telephone integer)
    AS $$
    select * from branches where name_br = name_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION search_tos_by_type (type_ text)
    RETURNS TABLE(id_tos integer, name_tos text, type text, price integer)
    AS $$
    select * from type_of_services where type = type_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION search_services_by_date (date_ text)
    RETURNS TABLE(branch_id integer, tos_id integer, client_id integer, date_of_receipt text)
    AS $$
    select * from services where date_of_receipt = date_;
$$ LANGUAGE sql;

-- UPDATE

CREATE OR REPLACE FUNCTION update_clients (id_ integer, name_ text, surname_ text, telephone_ integer)
	RETURNS void as $$
        UPDATE clients SET id_client = id_, name = name_,
                surname = surname_, telephone = telephone_
        WHERE id_client = id_;
	$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION update_branches (id_ integer, name_ text, address_ text, telephone_ integer)
	RETURNS void as $$
        UPDATE branches SET name_br = name_, address = address_,
            telephone = telephone_
        WHERE id_branches = id_;
	$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION update_tos (id_ integer, name_ text, type_ text, price_ integer)
	RETURNS void as $$
        UPDATE type_of_services SET name_tos = name_, type = type_,
            price = price_
        WHERE id_tos = id_;
	$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION update_services (id_b integer, id_t integer, id_c integer, date_ text)
	RETURNS void as $$
        UPDATE services SET date_of_receipt = date_
        WHERE branch_id = id_b AND tos_id = id_t AND client_id = id_c;
	$$ LANGUAGE sql;

-- DELETE BY

CREATE OR REPLACE FUNCTION delete_clients_by_name (name_ text)
    RETURNS void
    AS $$
    delete from clients where name = name_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_branches_by_name (name_ text)
    RETURNS void
    AS $$
    delete from branches where name_br = name_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_tos_by_type (type_ text)
    RETURNS void
    AS $$
    delete from type_of_services where type = type_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_services_by_date (date_ text)
    RETURNS void
    AS $$
    delete from services where date_of_receipt = date_;
$$ LANGUAGE sql;

--DELETE STR

CREATE OR REPLACE FUNCTION delete_clients_by_str (id_ integer)
    RETURNS void
    AS $$
    delete from clients where id_client = id_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_branches_by_str (id_ integer)
    RETURNS void
    AS $$
    delete from branches where id_branches = id_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_tos_by_str (id_ integer)
    RETURNS void
    AS $$
    delete from type_of_services where id_tos = id_;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION delete_services_by_str (id_b integer, id_t integer, id_c integer)
    RETURNS void
    AS $$
    delete from services where branch_id = id_b AND tos_id = id_t AND client_id = id_c;
$$ LANGUAGE sql;

CREATE OR REPLACE FUNCTION update_total_money ()
RETURNS trigger AS $$
BEGIN
    UPDATE clients
    SET total_money = (SELECT SUM(type_of_services.price)
                       FROM services, type_of_services
                       WHERE services.tos_id = type_of_services.id_tos
                       AND clients.id_client = services.client_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


DROP TRIGGER IF EXISTS count_total_money
  ON services;
CREATE TRIGGER count_total_money AFTER INSERT ON services
FOR EACH ROW EXECUTE PROCEDURE update_total_money();
