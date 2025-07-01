# Original string
text = "   Hello, Python World!   "

print("Original string:", text)

# strip() - remove leading/trailing whitespace
print("Stripped string:", text.strip())

# lower() - convert to lowercase
print("Lowercase:", text.lower())

# upper() - convert to uppercase
print("Uppercase:", text.upper())

# replace() - replace a substring
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# find() - find the index of substring
print("Position of 'World':", text.find("World"))

# count() - count number of occurrences
print("Count of 'l':", text.count('l'))

# split() - split string into list
print("Split string:", text.strip().split())

# startswith() and endswith()
print("Starts with 'Hello':", text.strip().startswith("Hello"))
print("Ends with 'World!':", text.strip().endswith("World!"))
