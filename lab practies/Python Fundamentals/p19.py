# Using map() to square numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print("Original list:", numbers)
print("Squared list:", squared)


from functools import reduce

# Using reduce() to multiply all elements
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

print("List:", numbers)
print("Product:", product)

# Using filter() to remove even numbers
numbers = [10, 15, 22, 33, 40, 51]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Original list:", numbers)
print("Odd numbers:", odd_numbers)
