"""NUMPY INTRODUCTION--"""




#NumPy (Numerical Python) is a powerful Python library used for numerical computations.
"""It provides:

Fast array operations

Mathematical functions

Matrix algebra

Tools to work with large datasets efficiently




Why NumPy is important for Data Analysts?
"""



"""✅ Why use NumPy for Data Analysis?



Feature 	      NumPy	                Python Lists
Speed	             Very Fast                (  C-optimized)	Slower
Memory	          Less memory usage  	   High memory usage
Broadcasting        	Supported	       Not supported
Vectorized Ops       Yes (No loop needed)	No (Use loops)
Integration	Pandas, Scikit-learn, etc.	Less direct com"""







""" HOW TO INSTALL NUMPY-





PIP INSTALL NUMPY WRITE THIS IN YOUR TERMINAL--
"""





# import numpy as np


""" HOW TO IMPORT NUMPY"""



# import numpy as np
# import pandas as pd

# import numpy as np





# print("hello world")



# this is how we import numpy...













"""WHAT IS THE DIFFERENCE BETWEEN NUMPY ARRAY VS PYTHON LIST:-"""



#PYTHON LIST-                   NUMPY ARRAY
#CAN STORED MIXED DATA         STORES ONLY ONE DATA TYPE
#SLOWER COMPUTATION            MUCH FASTER USING
#NO BROADCASTING               SUPPORTS BROADCASTING







"""Broadcasting describes how NumPy automatically expands the smaller array so that it matches the shape 
of the larger one, without actually copying data, 
to perform element-wise operations."

""

# ✅ Why Use Broadcasting?


# To perform operations without writing loops



# To handle arrays of different shapes efficiently



# To make code cleaner and faster





# 🔢 Basic Example:

import numpy as np

a = np.array([1, 2, 3])        # Shape: (3,)
b = 2                          # Scalar value

result = a + b                # Broadcasting adds 2 to each element
print(result)    


             # Output: [3 4 5]


             # ✅ b is a scalar, so NumPy broadcasts it to [2, 2, 2] and then adds it to a.


"""




# import numpy as np

# a = np.array([1, 2, 3])        # Shape: (3,)
# b = 2                          # Scalar value

# result = a + b                # Broadcasting adds 2 to each element
# print(result)  








# HOW TO CREATE YOUR FIRST NUMPY ARRAY 




# FIRST WE WILL CREATE ARRAY FROM A LIST OR WE CAN SAY THAT WE CREATE A 1D ARRAY.
# AND THEN WE WILL CREATE OUR MULTI DIMENSIONAL ARRAY.. 


# """




"""FROM A LIST"""



# import numpy as np


# # a=np.array([1,2,3,4,5,6])
# b=np.array([2,3,4,5,6])
# print(b.ndim)

# print(a)

# b=np.array([2,5,6,7])

# print("FIRST ARRAY:")
# print(a)
# print("second array:")
# print(b)
# import numpy as np
# a=np.array((1,2,3,34,4,5))
# print(a.ndim)





""" MULTI DIMENSIONAL ARRAY---"""



#In NumPy, a multidimensional array is called a ndarray (N-dimensional array). 
# It can store data in 1D, 2D, 3D, or more dimensions.







""" HOW WE CAN CREATE A MULTIDIMENSIONAL ARRAY:"""




# import numpy as np

# print("FIRST 2D ARRAY:")

# arr= np.array([[1,2,4],[3,3,2]])
# print(arr)
# print("number of dimensions:")
# print(arr.ndim)

# import numpy as np
# print("SECOND 2D ARRAY:")
# arr3=np.array([[0,0],[0,0]])
# print(arr3)


# so this is how we can create one or 2d array or we can say that a multi dimensional array by using numpy...








"""BUILT IN FUNCTIONS IN NUMPY"""





"""1. np.zeros((2,3))"""



# Ye function ek 2 rows × 3 columns ka array banata hai, jismein sare elements zero (0) hote hain.
# it create a 2 by 3 arrays where all elements will be zero.



# 🔹 Syntax:np.zeros(shape, dtype=float)

#

# import numpy as np

# print(" first zero array1")

# a=np.zeros((2,3))
# print(a)


# arr1=np.zeros((2,2))
# print("second zero array:")
# print(arr1)


# import numpy as np
# a=np.zeros((4,4))
# print(a)








# """ 2.np.ones((2,2))"""




# # 🔹 Definition:
# # Ye ek 2×2 array return karta hai, jismein har element 1 hota hai.
# #it will create a 2by 2 array where all elements will be one.




# # 🔹 Syntax:np.ones(shape, dtype=float)



# #example-


# import numpy as np

# arr=np.ones((3,3))

# print(arr)








""" 3. np.arange(0, 10, 2)"""



# 🔹 Definition:
# Ye np.arange(start, stop, step) ka use karke 0 se lekar 10 ke beech tak 


# 2 ke step size se values generate karta hai. (Note: 10 include nahi hota)

# actually it is basically used to generate for a specfic criteria where you have to mention start,stop.step.

# 🔹 Syntax:np.arange(start, stop, step)





#example-


# import numpy as np

# print("array3")

# arr = np.arange(0, 20, 3)

# print(arr)







""" 4. np.linspace(1, 5, 5)"""




# 🔹 Definition:

# Ye function 1 se 5 ke beech mein 5 equally spaced values generate karta hai.
# this function is bascially used to generate a sequence range based on your input or 
# user input



# 🔹 Syntax:np.linspace(start, stop, num)



#example--



# import numpy as np

# print("array4")

# arr = np.linspace(1, 100, 10)

# print(arr)







""" np.eye().."""




# if you want to create a identity matrix then we wil use np.eye() function.

"""IDENTITY MATRIX"""

# ✅ What is an Identity Matrix?
# An Identity Matrix is a special type of square matrix (same number of rows and columns) in which:

# All diagonal elements are 1

# All non-diagonal elements are 0

# 📘 Example: Identity Matrix of Size 3×3

# I = [[1, 0, 0],
#      [0, 1, 0],
#      [0, 0, 1]]



# ✅ Notice that only the elements from top-left to bottom-right (diagonal) are 1, rest are 0.



""" NOW WE SEE HOW WE CAN WE CREATE THE IDENTITY MATRIX"""



# import numpy as np 

# identity_matrix=np.eye(3)

# print(identity_matrix)









"""
    4.np.full()"""

#np.full() is a NumPy function used to create a new array of a given shape, 
# where every element is filled with a specified constant value.

# It is very useful when you want to initialize an array with
#  the same value across all elements, instead of zeros or ones.


""" NOW WE WILL SEE HOW WE CAN CREATE A FILLED ARRAY"""



# import numpy as np


# a=np.full((2,2),8)
# print(a)

# B=np.full((3,3),5)
# print(B)
# a=np.full((4,4),4)
# print(a)

# print(filled_array)













""" What Are Data Types in NumPy?"""




# NumPy is type-safe, meaning:

# Once you create an array with a specific data type (like int, float, bool),
#  each element in the array must be of that same type.





"""🔶 What is dtype?



In NumPy, every array has a fixed data type (dtype). 


This defines the type of elements stored (e.g., integer, float, string) 
and how much memory each element takes."""




# 📘 Common Data Types in NumPy

# Data Type	Description	Example Code

# int / int32/int64	                                  Integer values	               np.array([1, 2, 3], dtype='int')
# float / float32/float64	                          Decimal numbers        	       np.array([1.5, 2.7], dtype='float')
# bool	Boolean values                                (True / False)	               np.array([True, False], dtype='bool')
# str / U	                                          Unicode (string) data	           np.array(['apple', 'banana'], dtype='str')
# complex	                                          Complex numbers (a + bj)	       np.array([1+2j, 3+4j])
# object	                                          Mixed Python objects 	           np.array(["1", "a", "3.5"], dtype='obj





""" Example 1: Create array with specific dtype"""

# import numpy as np

# arr1 = np.array([1, 0, 3],dtype='bool')
# print(arr1)        
# print(arr1.dtype) 





"""
 Example 2: Create boolean and string arrays"""



# import numpy as np

# bool_arr = np.array([0, 1, 2], dtype='bool')
# print(bool_arr)                                # [False  True  True]





#ANOTHER EXAPLE FOR STRING DATA TYPE--





# import numpy as np

# str_arr = np.array([1, 2, 3], dtype='U')

# print(str_arr)  
# print(str_arr.dtype)                               # ['1' '2' '3']








"""Type Conversion (astype())"""


# You can convert from one dtype to another data type by using astype().



# now we will understand by the helpof example---




# import numpy as np

# arr = np.array([1.5, 2.8, 3.9])
# # print(arr)

# int_arr = arr.astype('int64')


# print(int_arr)                       # [1 2 3]







# ✅ Interview Insight: astype() creates a new array; original remains unchanged.







""" Array Attributes in NumPy"""

# Array attributes in NumPy are built-in properties of a NumPy array object (ndarray) that 
# give important information about the array — such as its shape, size, dimensions, and data type.

# These attributes help you understand the structure and optimize the use of arrays in your program



# 🧠 Why Use Array Attributes?
# To inspect array structure without printing full data

# To debug errors due to shape mismatch

# To write dynamic and efficient code







'''
1.shape'''
# .shape is an attribute of a NumPy array that returns a tuple representing the dimensions (rows, columns, etc.) of the array.

# It tells you how many elements exist along each axis of the array.




""" now how we will see how  can we use  the shape to find the arr length by row or column wise"""


# import numpy as np
# arr = np.array([[1, 2, 3]])
# print(arr.shape)           # Output: (2, 3)







'''
 2.arr.ndim'''



#  Definition:
# arr.ndim is a NumPy array attribute that tells you the number of dimensions (or axes) of an array.



# 🔍 Why is it important?


# It helps you understand the structure of your array:

# 1D → Vector

# 2D → Matrix

# 3D → Cube (layered matrices)

# nD → Higher-dimensional arrays



"""lets understand by the help of example-"""



# import numpy as np

# arr = np.array([1, 2, 3])

# print(arr.ndim)  # Output: 2








'''3️. arr.size--'''

# 🔹 Definition:
# arr.size is a NumPy array attribute that returns the total number of elements in the array,
#  regardless of its shape or dimensions.



"""Meaning: Array mein total elements ki sankhya (rows × columns).

Yahan: 2 x 3 = 6 elements

➕ Use: Jab aapko array ke andar total data count karna ho.



🔍 Interview Tip: size ≠ shape. Shape structure batata hai, size total elements."""








""" NOW LET'S UNDERSTAND HOW WE CAN USE THIS"""





# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6],[3,4,5]])
# print("total elements:")
# print(arr.size)  # Output: 6







# 4.arr.dtype

# arr.dtype is an attribute in NumPy that tells you the data type of the elements stored in the array.


#  This tells you what type of values the array contains (e.g., int32, float64, bool, etc.)




"""Meaning: Array ke elements ka data type.


Yahan int64 → 64-bit integer type


➕ Use: Memory optimization ke liye data types ka kaafi bada role hota hai.

🔍 Interview Tip: Data analytics mein float32, float64, int32, 
object types etc. ka use hota hai, so understanding dtype is essential PART FOR THIS ROLE
IF YOU REALLY WANT TO BECOME A DATA ANALYST.

"""






"""NOW LETS SEE THE EXAMPLE HOW WE CAN USE THE ARR.DTYPE"""





# import numpy as np
# arr = np.array([1, 2, 3])


# print(arr.dtype)  # Output: int64



"""| Attribute|      Use                       | Output   | Explanation                  |
| --------- | -------------------------    | -------- | ---------------------------- |
| `shape`   |    Rows × Columns            | `  (2, 3)`   |    Array ka dimension structure |
| `ndim`    |    Number of dimensions      | `   2`       |   2D array                     |
| `size`    |   Total number of elements   |     `6`       |   Total data points            |
| `dtype`   |   Data type of each element  |   `int64`     |    Type of numbers stored       |
"""
# import numpy as np
# a=np.array([1,2,3])
# print(a+100)

# import numpy as np


# marks=np.array([80,90,75,85,60])
# print("average marks:", np.mean(marks))
# print("highest  marks:", np.max(marks))
# print("lowest marks:", np.min(marks))
# print("passed students:", np.sum(marks>60))





""" Array Operations in NumPy"""





""" 1. Arithmetic Operations"""



# ✅ Definition:
# You can perform element-wise arithmetic operations directly on NumPy arrays: +, -, *, /


# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# print(arr1 + arr2)  # [5 7 9]
# print(arr1 * arr2)  # [4 10 18]
# print(arr2 - arr1)  # [3 3 3]
# print(arr2 / arr1)  # [4.0 2.5 2.0]




# ✅ Use Case:
# Fast mathematical computations (element-wise)

# Used in data transformation, feature engineering.

# 🔍 Interview Tip:
# NumPy uses vectorized operations, making it 10x faster than Python loops.



"""BROADCASTING """



# ✅ Definition:
# Broadcasting allows NumPy to perform operations between arrays of different shapes by automatically stretching the smaller array.

# ✅ Example:
# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])     # shape (2,2)
# arr2 = np.array([10, 20])             # shape (2,)

# print(arr1 + arr2)



# Output:
# [[11 22]
#  [13 24]]



# ✅ Why We Use It:
# Saves memory and computation



# Avoids need for manual looping or reshaping


# 🔍 Interview Tip:


# Broadcasting follows alignment rules from the last dimension and works if one of the dimensions is 1.




"""🔹 3. Comparison Operations"""




# ✅ Definition:
# Used to compare two arrays element-wise and return a Boolean array.




# ✅ Example:


# import numpy as np
# arr = np.array([1, 4, 3, 4])
# print(arr > 2)                           # [False False  True  True]
# print(arr == 4)                            #     [False False  True False]



                     
# ✅ Use Case:
# Useful in filtering, conditions, Boolean indexing



"""
4. Aggregation Functions"""



# ✅ Definition:
# Aggregation means summarizing values — like total, average, standard deviation, min, max etc.




# ✅ Functions:


# sum() → total of all elements



# mean() → average
  

# std() → standard deviation  


# min(), max() → smallest/largest value


# ✅ Example:

# import numpy as np


# arr = np.array([10, 20, 30, 40])

# print(arr.sum())        # 100
# print(arr.mean())       # 25.0
# print(arr.std())        # 11.18...
# print(arr.min())        # 10
# print(arr.max())        # 40



# ✅ Use Case:
# Core part of data analysis (summary statistics)







"""🔷 Topic: axis in NumPy Aggregation"""





# ✅ Definition of axis:
# In NumPy, axis refers to the dimension along which a particular operation is performed:



# axis=0 → Column-wise operation (down the rows)

# axis=1 → Row-wise operation (across the columns)



# 🔹 Example Code:


# import numpy as np

# arr = np.array([[1, 2, 3],
#                 [4, 5, 6]])

# print(arr.sum(axis=0))  # [5 7 9]
# print(arr.sum(axis=1))  # [6 15]







# 📊 Let's Visualize the Array:




#      Column 0  Column 1  Column 2
#      ---------------------------
# Row0 |   1   |    2    |    3   |
# Row1 |   4   |    5    |    6   |
# 🔍 Explanation:



# 👉 arr.sum(axis=0): Column-wise sum


# It adds elements column-wise (↓ vertical):



# Column 0: 1 + 4 = 5

# Column 1: 2 + 5 = 7

# Column 2: 3 + 6 = 9

# ➡️ Output: array([5, 7, 9])








# 👉 arr.sum(axis=1): Row-wise SUM


# It adds elements row-wise (→ horizontal): 
  
# Row 0: 1 + 2 + 3 = 6

# Row 1: 4 + 5 + 6 = 15

# ➡️ Output: array([6, 15])      




  

# 💡 Why use axis operations?


# ✅ Performance Optimization – Fast operations over rows/columns using C-based backend.

# ✅ Data Summary – Easy to compute row-wise or column-wise stats (like total marks per student or per subject).

# ✅ Required in Data Analysis – You often need to calculate:



# Total sales per day (axis=1)

# Average product price per category (axis=0)



#  Summary Table-

# Operation	         Description	                          Example
# Arithmetic	     +, -, *, / between arrays	              arr1 + arr2
# Broadcasting	     Operate between different shapes	      arr2 + arr1
# Comparison	     Compare values element-wise	          arr > 5
# Aggregation	     Sum, mean, min, max, std	              arr.sum(), arr.mean()
# Axis-wise	         Row/column-wise operations	              arr.sum(axis=1)




""" Reshaping and Manipulating Arrays"""



# 🔹 1. reshape()


# Definition:
# Changes the shape of an array without changing its data.



# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# reshaped = arr.reshape(2, 3)
# print(reshaped)




# Output:
# [[1 2 3]
#  [4 5 6]]
# 🎯 Note: Total elements must remain same (6 = 2×3)




