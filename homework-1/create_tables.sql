-- SQL-команды для создания таблиц
CREATE TABLE IF NOT EXISTS customers(
	customer_id VARCHAR(5) PRIMARY KEY,
	company_name VARCHAR(100),
	contact_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS employees(
	employee_id INT PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	title VARCHAR(100),
	birth_date DATE,
	notes TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(5) REFERENCES customers(customer_id) ON DELETE CASCADE,
    employee_id INT REFERENCES employees(employee_id) ON DELETE CASCADE,
    order_date DATE,
    ship_city VARCHAR(50)
);
