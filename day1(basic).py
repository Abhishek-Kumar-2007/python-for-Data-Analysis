print("hello, world!")
print("hello, Abhishek")
#this is a first python program
"""variables in python"""
# rules variables:-
# 1. Variables are case-sensitive
# 2. Variables must start with a letter or underscore
# 3. Variables can only contain alphanumeric characters and underscores
# 4. Variables cannot be reserved keywords

a1=10
print(a1)    

name="Abhishek"
print(name)


b=20
print(b)

name="Abhishek"
Name="Abhi"
print(name,Name)

#Invalid: 'for' is a resreved keyword

import keyword
print(keyword.kwlist)


age=23
age=30
print("updated age:",age)
#in above only show latest value because variable can only store one value at a time. When we assign a new value to the same variable, it overwrites the previous value.


"""data types in python"""

"""numeric data types: int, float, complex"""
# 1.Integers (int): Whole numbers without a decimal point. Example: 1, -5, 0
# 2.Floats (float): Numbers with a decimal point. Example: 3.14, -0.001, 2.0
# 3.Complex numbers (complex): Numbers with a real and imaginary part. Example: 2 + 3j, -1 - 4j

#a=-4
#a=3
#a=1.4
#a=1+2j where j=-1
#a=1+2(-1)

"""sequence data types: list, tuple, string"""

"""string"""


name="chotu"
print(name)

a2="a"+"b"
print(a2)   
#without space

a1="a"+" "+"b"
print(a1)   
#with space

firstname="Abhishek"
lastname="Kumar"
fullname=firstname+" "+lastname
print(fullname)

#i want to print 10 times "Abhishek"
b=" Abhishek "*10
print(b)


# fun="ha"*100
# print(fun)

# A=" i hate exams"*1000
# print(A)


name="Abhishek"
print("The length of name is:")
print(len(name))

"""list--"""

    #how to create a list in python--
first_list = [1, 2, 3, 4, 5.0,"Abhishek","aman"]
print(first_list)

emp_data=["Abhishek",23,"Python Developer",50000]
print("this is employee data:")
print(emp_data)

#how to add element in list--
my_list1=[1,2,4,"Abhishek","shiva"]
my_list1.append("Aman")
print(my_list1)

#how to remove element from list--
my_list2=[1,2,4,"Abhishek","shiva"]      
my_list2.remove("shiva")
print(my_list2)

#how to update element in list--

my_list3=[1,2,4,"Abhishek","shiva"]
my_list3[3]="Aman"
print(my_list3)  

