"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

file_cust = '/Users/berez/PycharmProjects/postgres_homework/postgres-homeworks/homework-1/north_data/customers_data.csv'
file_employ = '/Users/berez/PycharmProjects/postgres_homework/postgres-homeworks/homework-1/north_data/employees_data.csv'
file_order = '/Users/berez/PycharmProjects/postgres_homework/postgres-homeworks/homework-1/north_data/orders_data.csv'

with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='root'
) as conn:
    with conn.cursor() as cur:
        with open(file_cust) as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                query = """INSERT INTO customers_data
                VALUES (%s, %s, %s)"""

                cur.execute(query, row)
    with conn.cursor() as cur:
        with open(file_employ) as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                query = """INSERT INTO employees_data
                VALUES (%s, %s, %s, %s, %s, %s)"""

                cur.execute(query, row)
    with conn.cursor() as cur:
        with open(file_order) as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                query = """INSERT INTO orders_data
                VALUES (%s, %s, %s, %s, %s)"""

                cur.execute(query, row)
# close cursor and connection
conn.close()
