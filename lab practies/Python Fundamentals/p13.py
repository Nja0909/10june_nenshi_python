# Generator function to yield first 10 even numbers

def even_numbers():
    num = 2
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1

# Using the generator
for even in even_numbers():
    print(even)
