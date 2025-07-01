# Program to check blood donation eligibility

age = int(input("Enter your age: "))
weight = int(input("Enter your weight in kg: "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood due to low weight.")
else:
    print("You must be at least 18 years old to donate blood.")
