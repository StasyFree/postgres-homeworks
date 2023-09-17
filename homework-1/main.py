"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from dotenv import load_dotenv
import csv
import os

if __name__ == "__main__":

    # Получение абсолютного пути к папке с файлами CSV
    csv_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "north_data"))

    # Получение путей к CSV-файлам с данными
    csv_files = {
        "customers": os.path.join(csv_folder, "customers_data.csv"),
        "employees": os.path.join(csv_folder, "employees_data.csv"),
        "orders": os.path.join(csv_folder, "orders_data.csv")
    }
    load_dotenv()

    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()

    for table, csv_file in csv_files.items():
        with open(csv_file, "r", encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                columns = ", ".join(row.keys())
                values = ", ".join(["%s"] * len(row))
                insert_query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
                cursor.execute(insert_query, list(row.values()))

    connection.commit()
    cursor.close()
    connection.close()
