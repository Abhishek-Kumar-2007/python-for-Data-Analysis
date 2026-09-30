
"""list"""

#1. append
#adds a value to the end of the list. It takes a single argument, which is the value to be added.
fruits = ["apple", "banana"]
fruits.append("orange")
print("this is updated list:")
print(fruits)


#2.reverse() -> reverses the order of the elements in the list

number=[1, 2, 3, 4, 5]
number.reverse()
print("This is a reverse:")
print(number)

#3.clear() -> removes all the elements from the list and makes it empty

students=["Abhishek","Aman","Shiva"]
students.clear()
print("This is an empty list:")
print(students)

#4.sort() -> sorts the elements of the list in ascending order
#sorting means  ascending order for numbers and alphabetical order for strings

marks=[90,45,70,20]
marks.sort()
print("This is a sorted list:")
print(marks)


#5.insert() -> inserts an element at a specific position in the list. It takes two arguments: the index where the element should be inserted and the element itself.

colors=["red","blue","yellow"]
colors.insert(1,"green")
print("This is the updated list:")
print(colors)    

#6.pop() -> removes the last element from the list and returns it

cars=["BMW","Audi","Mercedes"]
cars.pop()
print("This is the popped element:")
print(cars)


#7.copy() -> creates a copy of the list
original_list=[1,2,3]
new_list=original_list.copy()
print("This is the copy list:")
print(new_list)


"""TUPLE"""
# a tuple is a collection data type in python that is used to store multiple items in a single variable. It is similar to a list, but unlike lists, tuples are immutable, meaning that their elements cannot be changed after they are created. Tuples are defined using parentheses () and can contain elements of different data types.
#tuple is ordered
#tuple is immutable(cannot be changed after creation)
#ttupple allows duplicate values
#tupple is writeen with round brackets()

#how to create a tuple in python--

my_tuple=(1,2,3,4,5,6,7,8)
print("this is a tuple:")
print(my_tuple)

#1. type() function
# the type() function is used to determine the type of a variable or value in Python. It returns the type of the object passed as an argument.

print(type(my_tuple))
first_tuple=(1,2,4)
print(first_tuple)

#2. indexing in tuple
#indexing in tuple is used to access individual elements of a tuple. The index starts from 0 for the first element, 1 for the second element, and so on. You can use negative indexing to access elements from the end of the tuple, where -1 refers to the last element, -2 refers to the second last element, and so on.
#index always starts from 0
#first element -> index 0
#second element -> index 1


my_tuple=(1,3,4,5,6,7,8)
print(my_tuple)
print(my_tuple[4])

#example 2

fruits=("apple","banana","orange")
print(fruits[0])
print(fruits[2])

# negative indexing in tuple
# -1 -> last value
# -2 -> second last value
 
fruits=("apple","banana","orange")  
print(fruits[-2])

#3. slicing in tuple

#slicing is used to access multiple elements
#from a tuple using a range of indexes

# syntax:

# tuple_name[start:end]

#start index included
#end index excluded

#example 01
numbers=(10,20,30,40,50,60)
print(numbers[0:3])

#example 02

#from begining to specific index

fruits=("apple","banana","orange","grape")
print(fruits[:3])

#example 03

# from specific index to end    

numbers=(10,20,30,40,50,60)
print(numbers[3:])

#length--

my_tuple=(1,2,3,4,5,6,7,8)
print(len(my_tuple))


#difference

#| indexing                  | slicing          |
#|-------------------        |------------------|
#| Accesses a single element | Accesses a multiple elements |
#| Uses a single index       | Uses a range of indexes |
#|example: data[1]           | example: data[1:4] |


#difference between list and tuple

#| List                      | Tuple            |
#|---------------------------|------------------|
#| Mutable (can be changed)  | Immutable (cannot be changed) |
#| Uses square brackets []   | Uses parentheses () |
#|faster modification        | faster access     |
#|more memory usage          | less memory usage |


"""boolean---true/false"""

#there is no use of boolean in day to day life but it is used in programming to represent the truth value of an expression. It can have two possible values: True or False. Boolean values are often used in conditional statements and loops to control the flow of a program based on certain conditions.

"""dictionary---"""

# a dictionary is a collection data type in Python that is used to store key-value pairs. It is an unordered, mutable, and indexed collection. Dictionaries are defined using curly braces {} and consist of key-value pairs separated by a colon (:). Each key in a dictionary must be unique, and the values can be of any data type.
#dictionary is unordered
#dictionary is mutable(can be changed after creation)
#dictionary does not allow duplicate keys
#dictionary is written with curly brackets {}

#step -01 how to create dict--

print("welcome to python restro:")

menu={}
print("this is menu:")

# how to add element--

menu["Gulab Jamun"]=40
menu["Ras Malai"]=60
menu["pasta"]=120
menu["burger"]=80
print("there are four items in the menu")
print(menu)

# how to remove element from dict--
print("pasta and burger are not available today")
del menu["pasta"]
del menu["burger"]
print(menu)

# how to access value from dict--

print(menu["Gulab Jamun"])

#how to clear dict--

menu.clear()
print("restro is closed today:")
print(menu)

# manually creating a dictionary using key-value pairs
person={"name":"Abhishek","age":25,"city":"Delhi"}
print("this is a person dictionary:")
print(person)

"""set---"""

# a set is a collection data type in Python that is used to store unique elements. It is an unordered, mutable, and iterable collection. Sets are defined using curly braces {} or the built-in set() function. The elements in a set are not indexed, and they cannot contain duplicate values.
# set is unordered
# set is mutable(can be changed after creation)
# set does not allow duplicate values
# set is written with curly brackets {}

my_set={1,2,3,4,5}
print("this is a set:") 
print(my_set)

resturant_menu={}
print("welcome to resturant:")
print("this is resturant menu:")
menu["1.pizza"]=150
menu["2.burger"]=80   
menu["3.pasta"]=120
menu["4.veg sandwich"]=60
menu["5.french fries"]=50
menu["6.coke"]=30
menu["7.ice cream"]=40
menu["8.coffee"]=20
menu["9.tea"]=15
menu["10.veg soup"]=70
print(menu)