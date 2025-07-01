# List of fruits
list1 = ['apple', 'banana', 'mango']

# Fruit to find
search_fruit = input("Enter the fruit to search: ")

# Search using for loop
found = False
for fruit in list1:
    if fruit == search_fruit:
        found = True
        print(f"{search_fruit} is in the list.")
        break

if not found:
    print(f"{search_fruit} is not in the list.")
