
# #BASIC COMMANDS
# print("Hello world.")
# print("Welcome to Python programming.")


# #VARIABLES
# name = "Kuldeep"
# age = 21
# time = 09.33 
# yes = True
# nah = None
# print("My name is", name, ", my age is ", age, "and this is written at time:" , time)


# #DATA TYPES
# """
# Integers - Whole numbers
# String - Text
# Float - Decimal numbers
# Boolean - True and False
# None - Absence of a value
# """
# print(type(name))
# print(type(age))
# print(type(time))
# print(type(yes))
# print(type(nah))


# #KEYWORDS
# """
# and, as, assert, break, class, continue, def, del, 
# elif, else, except, finally, False, for, from, global, if, 
# import, in, is, lambda, nonlocal, None, not, or, pass, 
# raise, return, True, try, while, with, yield

# (we cannot use these keywords as variable names and they have special meaning in Python)
# """


# #TYPES OF OPERATORS
# """An operator is a symbol that performs a specific operation on one or more operands."""

# #1.Arithmetic Operators
# a = 10
# b = 5
# sum = a + b
# difference = a - b
# product = a * b
# quotient = a / b
# modulus = a % b
# power = a ** b
# print("Sum:", sum)
# print("Difference:", difference)
# print("Product:", product)
# print("Quotient:", quotient)
# print("Modulus:", modulus) #gives the remainder of the division
# print("Power:", power) #gives the result of a raised to the power of b

# #2. Relational Operators
# x = 10
# y = 5
# print(x > y)  # True
# print(x < y)  # False
# print(x == y) # False
# print(x != y) # True
# print(x >= y) # True
# print(x <= y) # False

# #3. Assignment Operators
# num = 10
# num = num + 10 #10+10=20
# num += 10 #20+10=30       #this is a shorthand for num = num + 10

# #4. Logical Operators
# """not, and, or"""
# print(not True) #False
# print(not False) #True
# p = 50
# q = 30
# print(p > q and p < 100) #True and True = True
# print(p < q or p < 100) #False or True = True
# print(not(p > q)) #not True = False

# val1 = True
# val2 = False
# print(val1 and val2) #False
# print(val1 or val2) #True


# #Type Conversion
# """
# conversion - automatic conversion of one data type to another
# casting - manual conversion of one data type to another
# """
# x = 2
# y = 4.25
# sum = x + y# automatic conversion of integer to float. 2.0 + 4.25 = 6.25
# print(sum)


# x = "2"
# y = 4.25
# sum = x + y
# print(sum) #this will give an error because we cannot add a string and a float together. We need to convert the string to a float first.
# z = float(x) #this will convert the string "2" to the float 2.0
# sum = z + y # now we can add the float and the float together. 2.0+ 4.25 = 6.25
# print(sum)



# # INPUT IN PYTHON
# name = input("enter your name:")
# print("Welcome ", name)

# val1 = input("Enter value:")
# print(type(val1), val1) #this will give us the type of the input and the value of the input. By default, the input is always a string.

# val2 = float(input("Enter some value: "))
# print(type(val2), val2) #this will convert the input to a float and then print the type and value of the input.


# # Practive Questions
# # 1. Write a Python program to calculate the area of a circle given its radius.
# rad = float(input("Enter the radius of the circle:"))
# area = 3.14 * rad ** 2
# print("Radius of the circle is ", rad)
# print("Area of the circle is" , area)

# # 2. Write a Python program to input 2 floating numbers & print their average.
# no1 = float(input("Enter the first value: "))
# no2 = float(input("Enter the second value:"))
# avg = (no1 + no2) / 2
# print("The average of given values is :", avg)

# #3. Write a Python program to input two int numbers. Print True if one is greater than other, oterwise print false.
# input1 = float(input("first value:"))
# input2 = float(input("second value:"))
# print(input1 >= input2, ", 20" "Value 1 is greater than or equal to value 2")






