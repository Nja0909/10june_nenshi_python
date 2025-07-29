# main.py

from controller import fruit_manager, customer

def show_menu():
    print("\n=======  Fruit Store Menu  =======")
    print("1. Add Fruit Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    print("4. Customer Menu")
    print("5. Exit")
    print("=====================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            fruit_manager.add_fruit_stock()
        elif choice == '2':
            fruit_manager.view_fruit_stock()
        elif choice == '3':
            fruit_manager.update_fruit_stock()
        elif choice == '4':
            customer.customer_menu()
        elif choice == '5':
            print("Exiting the application. Thank you!")
            break
        else:
            print(" Invalid input! Please choose from the menu.")

if __name__ == "__main__":
    main()
