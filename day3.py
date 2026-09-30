"""string manipulation in python"""
# language = "python"
# print(language)

 #indexing---

# print(language[0:3])
# print(language[4])

 # how to replace string--

# sentence = "i love java"
# print(sentence)
# new=sentence.replace("java","python")
# print("sentence after replacement")
# print(new)

# # how to convert into string--
# #we cant add integer and string so we have to convert into string

# name="abhishek"
# age=19
# print(str(age))
# print(name + ", " + "age is" + " " + str(age))

# name= "language"
# print(len(name))

# a=" haa "*5
# print(a)

"""input function"""

#the input() function is used to take input from the user. it always returns a string value.
# whatever the user enters is stored  as a string by default

#by default, input()  takess data as a string.
#to convert it into an integer, we can use the int() function.


#syntax--
#var_name=input()

#example--


# name = input("enter your name: ")

# print(name)

# age = int(input("enter your age: "))
# print(age)


# example 03 how to add two numbers taken as input from user

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# print(a + b)

"""operator"""
#operators are special symbols used to perform operations on variables and values. They are used to perform various operations such as arithmetic, comparison, logical, and assignment operations.
#types of operators in python
#1. arithmetic operators

# a=5
# b=6
# print(a+b) #addition
# print(a-b) #subtraction
# print(a*b) #multiplication
# print(a/b) #division
# print(a%b) #modulus 

#2. comparison operators
"""==
!=
>
< 
>=
<=
"""

#3.assignment operators
#=
#+=
#-=
#*=
# /=    
#//=
#%=

#a=10
#a=-5
#print(a)

#4.logical operators
# and
# or    
#not
#1. and operator
# age=20
# citizen=True
# if age>=18 and citizen ==False:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")
# #2. or operator
# age=20
# citizen=True
# if age>=18 or citizen ==False:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")
# #3. not operator
# x=10
# print(not(x>5)) #not operator negates the condition. if the condition is true, it returns false and if the condition is false, it returns true.

"""conditional statements in python"""
#if statement
#if elif statement
#if elif else statement

#if statement---

# age=int(input("enter your age: "))
# if age>=18:
#     print("you are eligible to vote")

#if elif else statement---

# print("welcome to the grade system")
# num=int(input("enter your marks: "))
# if num>=90:
#     print("grade A")
# elif num>=75:
#     print("grade B")
# elif num>=60:
#     print("grade C")
# elif num>=50:            
#     print("grade D")
# else:
#     print("fail")

#program to check wheteher a number is positive, negative 

# num=int(input("enter a number: "))
# if num>0:
#     print(num,"is a positive number")
# elif num<0:
#     print(num,"is a negative number")
# else:
#     print(num,"is zero")


"""loops--"""
#  a loop is used to repeat a block of code multiple times. it helps to automate repetitive tasks and makes the code more efficient and easier to read.
# types of loops in python  
#1. for loop
#2. while loop  

#1. while loop---
# a while loop is used to execute a block of code as long as a specified condition is true. it is useful when the number of iterations is not known beforehand.
#when the condition becomes false, the loop will stop executing and the program will continue with the next line of code after the loop.

#syntax of while loop
# while condition:
#     # code to be code

#example

# count=2
# while count<=10:
#     print(count)
#     count=count+1

#for loop---
# for i in range(start, end, step):
#conditions--

#example
# for i in range(7):
#     print(i)

# for i in range(2,22,2):
#     print(i)

#looping through a collection--

# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# we can also use  loop  through string--

# for char in "12345":
#     print(char)

# for char in "python":
#     print(char)




