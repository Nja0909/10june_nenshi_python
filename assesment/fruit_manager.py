import os
import datetime

stock_file = "stock.txt"
log_file = "transaction_log.txt"

def log_transaction(action):
    with open(log_file, "a") as log:
        timestamp = datetime.datetime.now()
        log.write(f"{timestamp} - {action}\n")

def add_fruit_stock():
    fruit = input("Enter fruit name: ").strip().capitalize()
    quantity = input("Enter quantity: ")
    price = input("Enter price per unit: ")

    with open(stock_file, "a") as f:
        f.write(f"{fruit},{quantity},{price}\n")
    
    log_transaction(f"Added {quantity} of {fruit} at {price} per unit")
    print("Fruit added successfully!")

def view_fruit_stock():
    if not os.path.exists(stock_file):
        print("No stock found.")
        return
    print("\n Current Fruit Stock:")
    with open(stock_file, "r") as f:
        for line in f:
            fruit, qty, price = line.strip().split(",")
            print(f" {fruit} - Qty: {qty}, Price: ₹{price}")

def update_fruit_stock():
    fruit_name = input("Enter fruit name to update: ").strip().capitalize()
    updated_lines = []
    found = False

    if not os.path.exists(stock_file):
        print(" No stock file found.")
        return

    with open(stock_file, "r") as f:
        for line in f:
            fruit, qty, price = line.strip().split(",")
            if fruit == fruit_name:
                new_qty = input(f"Enter new quantity for {fruit}: ")
                new_price = input(f"Enter new price for {fruit}: ")
                updated_lines.append(f"{fruit},{new_qty},{new_price}\n")
                log_transaction(f"Updated {fruit} to Qty: {new_qty}, Price: {new_price}")
                found = True
            else:
                updated_lines.append(line)

    with open(stock_file, "w") as f:
        f.writelines(updated_lines)

    if found:
        print(" Fruit stock updated!")
    else:
        print(" Fruit not found in stock.")
