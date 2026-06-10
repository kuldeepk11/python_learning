# ##ESCAPE SEQUENCES CHARACTER

# # str1 = "This is a string."
# # str2 = 'This is also a string.'
# # str3 = """This is a string """
# # str4 = '''This is also a string.'''

# # "this is India's world"

# #\n - new line
# str1 = "This is string. \nWe are learning python."
# print(str1)


# # CONATINATION OF STRINGS
# str1 = "Hello"
# str2 = "World"
# str3 = str1 + " " + str2
# print(str3)


# # LENGTH OF A STRING
# str1 = "Hello World"
# print(len(str1))


# # Indexing
# str = "Hello World"
# print(str[0])  # H
# print(str[6])  # W
# print(str[-1])  # d
# print(str[-7])  # W



# # SLICING
# #str[ startingindex : ending index]
# str = "Hello World"

# var1 = str[6:11]
# print(var1) # World

# var2 = str[6 : len(str)]
# print(var2) # World

# var3 = str[0 : ]
# print(var3) # Hello World

# var4 = str[-5: -1]
# print(var4) # Worl


# # STRING FUNCTIONS
# str = "i am learning python from youtube."

# print(str.endswith("ube"))  # True

# print(str)
# print(str.capitalize()) # I am learning python from youtube.

# str = str.capitalize()
# print(str) # I am learning python from youtube.

# str = str.replace("am" , "was")
# print(str) # I was learning python from youtube.

# print(str.find("from"))
# print(str.find("java"))

# print(str.count("a")) # 2
# print(str.count("n")) # 3




# # PRACTICE PROBLEMS
# # 1. Write a program to input user's name and print its length.
# name = input("Enter your Full Name: ")
# print("Length of your name" , name , "is" , len(name))


# # CONDITIONAL STATEMENTS
# age = float(input("Enter your age:"))
# if(age >= 18):
#     print("Your are eligilble for applying for a driving license.")
#     print("You are also eligible for voting.")
# else: 
#     print("Your are not eligilble for applying for a driving license.")
#     print("You are also not eligible for voting.")
#     print("wait for" , 18 - age , "years to apply for driving licesense and voter id.")

# # difference between if and elif is that if is used for the first condition and elif is used for the subsequent conditions. If the first condition is true, the code block under if will be executed and the rest of the conditions will be ignored. If the first condition is false, the code will check the next condition under elif and so on until it finds a true condition or reaches the end of the conditions.
# # Indentation : space or tab before a line of code is called indentation. It is used to define the scope of loops, functions, and other code blocks. In Python, indentation is crucial as it indicates which statements belong to which blocks of code. For example, in an if statement, the code block that should be executed if the condition is true must be indented under the if statement. If the indentation is not correct, it will result in an IndentationError.

# # Grade Calculation Program
# marks = float(input("Enter your marks:"))

# if(marks >= 90):
#     grade = "A"
# elif(90 > marks >= 80):
#     grade = "B"
# elif(80 > marks >= 70):
#     grade = "C"
# elif(70 > marks >= 60):
#     grade = "D"
# elif(marks<60):
#     grade = "F"
# print("Your grade is:" , grade)



# # NESTING OF CONDITIONAL STATEMENTS

# age = float(input("Enter your age: "))

# if(age >= 18):
#     if (age >= 80):
#         print("You cannot drive the vehicle.")
#     else:
#         print("you can drive your vehicle.")
# else:
#     print("You cannot drive your vehicle until you turn 18.")



# WAP to check if a number is a multiple of 7 or not.
num = float(input("Enter your number: "))
rem = num % 7
if(rem == 0):
    print("Yes, your number is divisible by 7.")
else:
    print("Your number is not divisible by 7.")


