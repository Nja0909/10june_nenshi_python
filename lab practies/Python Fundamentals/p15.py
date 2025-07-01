# Printing a string directly
print("Hello")
# Assigning string to a variable
greeting = "Hello, World!"
print(greeting)
# Using triple quotes for multi-line string
message = """Welcome to Python Programming.
This is a multi-line string example."""
print(message)
# Accessing the first character of a string using index
name = "Python"
print("The first character is:", name[0])
text1 = "Python Programming"
# Start slicing from index 1 (second character)
print("From second position onwards:", text1[1:])
text2 = "Python Programming"
# Slice from index 0 to 5 (not including index 5)
print("Up to fifth character:", text2[:5])
text3 = "Python"
# Slice from index 1 to 4 (excluding index 4)
print("Substring (index 1 to 4):", text3[1:4])
text4 = "Hello"
# Access last character using negative indexing
print("Last character:", text4[-1])
text5 = "Programming"
# Start from index 1, step by 2
print("Alternate characters from index 1:", text5[1::2])
