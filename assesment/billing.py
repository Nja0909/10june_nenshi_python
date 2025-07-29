# logic/billing.py
import datetime
from db_connection import get_connection

class Billing:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS bills (
            bill_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(100),
            mobile VARCHAR(20),
            amount FLOAT,
            bill_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def insert_bill(self, name, mobile, amount):
        query = "INSERT INTO bills (customer_name, mobile, amount) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, mobile, amount))
        self.conn.commit()
        return self.cursor.lastrowid

    def generate_bill_file(self, name, mobile, amount):
        bill_id = self.insert_bill(name, mobile, amount)
        filename = f"bills/Bill_{bill_id}.txt"
        with open(filename, "w") as file:
            file.write("-------- BILL RECEIPT --------\n")
            file.write(f"Bill ID: {bill_id}\n")
            file.write(f"Customer: {name}\n")
            file.write(f"Mobile: {mobile}\n")
            file.write(f"Amount: ₹{amount}\n")
            file.write(f"Date: {datetime.datetime.now()}\n")
            file.write("-----------------------------\n")
        return filename

    def delete_bill(self, bill_id):
        self.cursor.execute("DELETE FROM bills WHERE bill_id = %s", (bill_id,))
        self.conn.commit()
