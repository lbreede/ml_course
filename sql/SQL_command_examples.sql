--SQL

CREATE DATABASE users;
--

CREATE TABLE users_table (
	id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL
);


SELECT * FROM users_table;

INSERT INTO users_table (username, email) VALUES ('user1', 'user1@example.com');
INSERT INTO users_table (username, email) VALUES ('user2', 'user2@example.com');

pg_dump -U felipepesantez -d users > somefile.sql
pg_dumpall > checkpoint1_.sql


pg_restore -U felipepesantez -d users checkpoint1_.sql


ALTER TABLE users_table
ADD COLUMN phone VARCHAR(25);

DROP TABLE IF EXISTS somename CASCADE;

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR(25)
);

ALTER TABLE customers
ADD COLUMN phone VARCHAR(25);



ALTER TABLE customers
ADD COLUMN address VARCHAR(25),
ADD COLUMN email VARCHAR(100);


INSERT INTO
	customers (customer_name)
VALUES
	('customer1'),
	('customer2'),
	('customer3')
RETURNING *;

ALTER TABLE customers
ADD COLUMN country VARCHAR(255);

UPDATE customers
SET country = 'USA'
WHERE id = 1;

UPDATE customers
SET country = 'UK'
WHERE id = 2;

UPDATE customers
SET country = 'Spain'
WHERE id = 3;

CREATE TABLE bills (
	bill_id SERIAL PRIMARY KEY,
	customer_name VARCHAR(25) NOT NULL,
	amount NUMERIC NOT NULL,
	date DATE NOT NULL,
	is_paid BOOLEAN DEFAULT FALSE
);


CREATE OR REPLACE PROCEDURE create_bill(
	IN customer_name VARCHAR,
	IN amount NUMERIC,
	IN date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
	INSERT INTO bills (customer_name, amount, date)
	VALUES (customer_name, amount, date);
END;
$$;

CREATE OR REPLACE PROCEDURE mark_bill_paid(
	IN bill_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
	UPDATE bills
	SET is_paid = TRUE
	WHERE bills.bill_id = mark_bill_paid.bill_id;
END;
$$;

CALL create_bill('Customer 1', 60, '2024-02-16');
CALL create_bill('Customer 2', 20, '2024-01-16');
CALL create_bill('Customer 3', 10, '2024-04-18');
CALL create_bill('Customer 4', 100, '2022-11-16');
CALL create_bill('Customer 5', 34, '2024-01-22');

CALL create_bill('Peter', 34, '2024-01-22');
CALL create_bill('Amy', 34, '2024-01-22');
CALL create_bill('Ashley', 34, '2024-01-22');














