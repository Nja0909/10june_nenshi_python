# String slicing examples
text = "PythonProgramming"

print("Original string:", text)

# Slice from index 0 to 5 (excluding 5)
print("First 5 characters:", text[0:5])

# Slice from index 6 to the end
print("From 7th character to end:", text[6:])

# Slice entire string
print("Entire string:", text[:])

# Slice with step
print("Every second character:", text[::2])

# Reverse string using slicing
print("Reversed string:", text[::-1])

# Last 5 characters
print("Last 5 characters:", text[-5:])
