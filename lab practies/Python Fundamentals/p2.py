# Program to calculate the area of a rectangle

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): Length of the rectangle
    width (float): Width of the rectangle

    Returns:
    float: Area of the rectangle
    """
    area = length * width  # Area = length × width
    return area


# Input section
rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))

# Call the function and store the result
rectangle_area = calculate_area(rectangle_length, rectangle_width)

# Display the result
print("The area of the rectangle is:", rectangle_area)
