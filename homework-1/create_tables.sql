-- SQL-команды для создания таблиц
CREATE TABLE customers_data
(
	customer_id varchar PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes varchar
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar REFERENCES customers_data(customer_id),
	employee_id int REFERENCES employees_data(employee_id),
	order_date date,
	ship_city varchar(100)
)
