# db_connection.py
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # Replace with your MySQL password
        database="billing_db"
    )
