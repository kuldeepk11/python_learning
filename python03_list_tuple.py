# # LIST (is mutbale in python)

# rec = ["Kuldeep", 95.4 , 20, "Bhavnagar", "Arjun", 90.6, 20, "Bhavanagar"]
# print(rec)

# print(rec[0])

# rec [0] = "Cristiano"
# print(rec)

# rec1 = rec[0:3]
# print(rec1)

# rec2 = rec[-4 : -1]
# print(rec2)


# # LIST METHODS

# marks = [80, 85, 69, 36, 96]
# word = ["Banana", "Apple", "Litchi", "Mango"]

# marks.append(83)
# print(marks)

# marks.sort()
# word.sort()
# print(marks)
# print(word)

# marks.sort(reverse=True)
# word.sort(reverse=True)
# print(marks)
# print(word)

# marks.reverse()
# word.reverse()
# print(marks)
# print(word)

# marks.insert(1,45)
# print(marks)
# word.insert(3, "Jamun")
# print(word)

# marks.remove(85)
# print(marks)
# word.remove("Mango")
# print(word)

# marks.pop(1)
# print(marks)
# word.pop(3)
# print(word)




# # TUPPLE (IMMUTABLE SEQUENCES OF VALUES)

# tup = (6, 3, 8, 9, 5, 3)
# print(type(tup))
# print(tup[0:3])
# #tup[0] = 6 # TypeError: 'tuple' object does not support item assignment

# print(tup.index(8))
# print(tup.count(1))
# print(tup.count(3))

# # PRACTICE QUESTIONS

# #1. WAP to ask a user to enter names of their 3 favorite movies & store them in a list.

# movies = []
# mov1 = input("Enter your 1st Movie: ")
# mov2 = input("Enter your 2nd Movie: ")
# mov3 = input("Enter your 3rd Movie: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print("Your favorite movies are: ", movies)

# movies = []
# movies.append(input("Enter your first movie: "))
# movies.append(input("enter your second movie: "))
# movies.append(input("Enter your third movie: "))
# print("Your favorite movies are: ", movies)



# # 2. WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)

# list1 = [1, 2, 1, 2, 1]

# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1 == list1):
#     print(list1, "Palindrome")
# else:
#     print(list1, "Not a Palindrome")



# # 3. WAP to count the number of students with the "A" grade in the following tuple.

# grade = ("A", "D", "C", "A", "B", "A")
# print(grade.count("A"))


# # 4. WAP to store the values in a list & sort them from "A" to "D".

# grade = ["A", "D", "C", "A", "B", "A"]
# grade.sort()
# print(grade)

