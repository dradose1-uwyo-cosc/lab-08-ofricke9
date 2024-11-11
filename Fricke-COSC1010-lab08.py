# Oliver Fricke
# UWYO COSC 1010
# 11-7-24
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def num_converter(num):
    isNeg = False
    if "-" in num:
        isNeg = True
        num = num.replace("-", " ")
    if "." in num:
        num_list = num.split(".")
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():
            if isNeg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit(): 
        if isNeg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slope_intercept(m, b, lowx, upx):
    if lowx > upx:
        return False
    if type(lowx) is not int:
        return False
    if type(upx) is not int:
        return False
    if type(m) is not int:
        return False
    if type(b) is not int:
        return False
    y_range = []
    for i in range(lowx, upx + 1):
        y = (m * i) + b
        y_range.append(y)
    return y_range




while True:
    m_input = input(f"Please enter a value for the slope: ")
    if m_input == 'exit':
        break
    try: 
        m = int(m_input)
    except ValueError:
        print("Invalid")
        continue
    b_input = input(f"Please enter a value for the y-intercept: ")
    if b_input == 'exit':
        break
    try:
        b = int(b_input)
    except ValueError:
        print("Invalid")
        continue
    lowx_input = input(f"Please enter a value for the lower bound of x: ")
    if lowx_input == 'exit':
        break
    try:
        lowx = int(lowx_input)
    except ValueError:
        print("Invalid")
        continue
    upx_input = input(f"Please enter a value for the upper bound of x: ")
    if upx_input == 'exit':
        break
    try:
        upx = int(upx_input)
    except ValueError:
        print("Invalid")
        continue

    y_range = slope_intercept(m, b, lowx, upx)
    if y_range:
        print(f"The values of y for x in the given domain, [{lowx}, {upx}] are: {y_range}")
    else:
        print("Error")



# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


def quad_formula():
    a = float(input("Enter your value of a: "))
    b = float(input("Enter your value of b: "))
    c = float(input("Enter your value of c: "))

    sqrtport = (b ** 2) - (4 * a * c)

    if sqrtport > 0:
        plus = (-b + ((sqrtport) ** .5)) / (2 * a)
        minus = (-b - ((sqrtport) ** .5)) / (2 * a)
        return plus, minus
    
    elif sqrtport == 0:
        ans = (-b) / (2 * a)
        return ans
    
    else:
        return "null"
    

print("The answers to the quadratic formula using your given values are:", quad_formula())