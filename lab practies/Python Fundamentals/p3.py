# Practical Example 1: Python code structure
# Python code is organized using indentation (4 spaces), not braces

def greet_user(name):
    # Function to greet the user
    print("Hello,", name)

# Practical Example 2: Creating variables in Python
# Variables are dynamically typed — no need to declare type

age = 20               # Integer
height = 5.8           # Float
name = "Nenshi"        # String
is_student = True      # Boolean

# Practical Example 3: Taking user input
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

# Practical Example 4: Check variable types dynamically
print("\nVariable Types:")
print("Name:", type(user_name))
print("Age:", type(user_age))
print("Static age variable:", type(age))
print("Height:", type(height))
print("Is Student:", type(is_student))

# Calling the function
greet_user(user_name)
