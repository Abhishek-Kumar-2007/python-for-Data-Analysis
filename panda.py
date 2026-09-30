

"""CHAPTER -01 INTRODUCTION TO PANDAS"""

 # PANDAS IS PYTHON LIBRARY USED FOR DATA MANIPULATION AND ANALYSIS
# WHY USE PANDAS--
# CLEAN MESSY DATA
# ANALYZE LARGE DATASETS
# GROUP WISE INSIGHTS





""" NOW WE SEE HOW TO GET STARTED WITH PANDAS"
#STEP-01 OPEN YOUR TERMINAL BY USING SHORTCUT = WIN + X AND THEN SELECT TERMINAL OR YOU CAN ALSO OPEN BY THE HELP OF SEARCH BAR AND THEN TYPE - CMD OR TERMINAL AND THEN OPEN IT.
#STEP-02 AND THEN WRITE COMMAND --- pip install pandas

"""




# print("hello world")


#open vs code--








# how to import pandas



# import pandas as pd



# import pandas as pd



# print("hello world")






# note here pd is an alias used in indusrtry for short and readable code.









"""NOW WE WILL MOVE TO THE CHAPTER -01 WHERE WE LEARN ABOUT THE KEY DATA STRUCTURE IN PANDAS"""





#  SERIES IN PANDAS- IN PANDAS SERIES IN ONE DIMESIONAL ARRAY WITH AXIS LABLES.IT
# IS A SINGLE COLUMN IN EXCEL.

# A Series in Pandas is a one-dimensional labeled array that can store data like:

# integers
# strings
# float values
# etc.

# It is similar to a single column in Excel or a list in Python, but with index labe
# NOW WE WILL UNDESTAND BY THE HELP OF EXAMPLE--
# """




""" HOW TO INTIALIZE THE SERIES IN PANDAS--"""
 



# import pandas as pd

# print(pd.Series([100,200,300]))

# print(pd.Series([49,93,33]))








# import pandas as pd
# data1=pd.Series([1000,2000,540,222])
# print(data1)


# # pd.Series()





# # # # note- it has a lables (index) and values.


# # # # it can behave like both a list and a dictionary












""" DATAFRAMES."""




# A PANDAS DATAFRAME IS A 2D STRUCTURE THAT CONTAINS ROWS AND COLUMN, WHERE COLUMNS CAN BE OF DIFFERENT DATA TYPES.



# THINK OF IT AS AN EXCEL SHEET OR SQL TABLE...






# """

# # NOW WE WIILL UNDERSTAND BY THE HELP OF EXAMPLE---




import pandas as pd

data={
    'ID':[1,2,3,4,5],
    'Name':['Abhishek','Sagar','Rohit','Aryan','Aditya'],
    'Age':[18,25,26,21,20],
    'City':['Dhanbad','Roorkee','Dehradun','Dhanbad','Bukaro'],
    'job':['Data Analyst','Data Scientist','Data Engineer','Doctor','AI Researcher'],
    'salary':[50000,60000,70000,80000,90000],
    'years_of_experience':[2,1,4,5,4]
}

df1=pd.DataFrame(data)
print(df1)






#  note- it is the most powerful data structure in data analysis.
   
   
   
   
#  it allows filtering,aggregation ,merging,sorting,reshaping and visualization.












""" CHAPTER-02- DATA IMPORT AND EXPORT IN PANDAS"""



# # # DATA IMPORT REFERS TO READING AND LOADING EXTERNAL FILES LIKE-CSV,EXCEL,JSON SQL ) INTO A PANDAS DATAFRAME.


# # # IMPORTING DATA- READING FILES IN PANDAS--






# # # """


""" STEP-01 HOW TO READ THE  excel FILES IN PANDAS"""



# import pandas as pd
# df1=pd.read_excel(r"C:\Users\Tarun Kumar\Downloads\supply_chain_inventory_dataset_15000_rows 2.xlsx")
# print(df1)



# import pandas as pd
# df=pd.read_excel(r"C:\Users\Tarun Kumar\Desktop\python\Cafe_Sales_Data_July_2025.xlsx")
# print(df)


# import pandas as pd
# df1=pd.read_csv("cleansales_data.csv")
# print(df1)



# import pandas as pd
# df1=pd.read_json("cleaned_data.json")
# print(df1)



# df1=pd.read_excel("Cafe_Sales_Data_July_2025.xlsx")
# print(df1)





""" now we read csv files in pandas
# # """

# /



# df.to_excel("table1.xlsx")

# df.to_csv("cleansales_data.csv")


# print(df)



# df.to_excel("table1.xlsx")


"""now we will read the json file"""



# import pandas as pd

# df=pd.read_json(r"C:\Users\Tarun Kumar\Desktop\python\sales_data.json")

# print(df)



# df.to_json("cleaned_data.json")


# import pandas as pd
# df =pd.read_json(r"c:\Users\Tarun Kumar\Downloads\sales_data_1000_rows.json")
# print(df.shape)

# df1=pd.read_excel(r"c:\Users\Tarun Kumar\Downloads\supply_chain_inventory_dataset_15000_rows 2.xlsx")
# print(df1)




""" how to save or export the file--"""




# import pandas as pd

# print(pd.read_json(r"C:\Users\Tarun Kumar\Desktop\python\sales_data.json"))


# pd.to_json("cleaned_data.json",index="false")





# # similary you can save excel or csv files also












""" CHAPTER-03 - DATA EXPLORATION AND BASIC OPERATION IN PANDAS...






# """

# """ DATA EXPLORATION-
# DATA EXPLORATION IS THE PROCESS OF UNDERSTANDING YOUR DATASET BEFORE ANALYSIS OR VISUALIZATION.
# 
# .
# IT INVOLVES CHECKING --

# STRUCTURE OF DATE(ROWS,COLUMNS)

# DATA TYPES(INT,FLOAT,OBJECT)

# MISSING/NULL VALUES

# BASIC STATS(MEAN,MIN,MAX)

# FREQUENCY OF VALUES(LIKE HOW MANY MALES /FEMALES)
# """

# print("Hello World")



"""FIRST WE WILL DISCUSS ABOUT --"""


# # HEAD() AND TAIL()--




# # HEAD()- IT DISPLAY THE TOP(N) ROWS

# # TAIL()- IT DISPLAY THE BOTTOM (N) ROWS.


# import pandas as pd


# df=pd.read_excel("Cafe_Sales_Data_July_2025.xlsx")


# print("top 15 ROWS")

# print(df.head(15))

# print("bottom 15 ROWS")
# print(df.tail(15))


# print("BOTTOM 5 ROWS")

# print(df.tail(12))









# # THIS IS HOW THE TOP AND BOTTOM LIKE HEAD() AND TAIL() FUNCTIONS WORKS..












""" NOW WE WILL MOVE TO THE NEXT OPERATION THAT IS SHAPE AND INFO"""





# # SHAPE--IT PROVIDES THE TOTAL ROWS AND COLUMNS IN A PARTICULAT TABLE...
# import pandas as pd
# df=pd.read_excel(r"C:\Users\Tarun Kumar\Desktop\python\Cafe_Sales_Data_July_2025.xlsx")
# print(df.info())



# # INFO()- IT PROVIDES THE DATA TYPE+NULL VALUE  and overall SUMMARY of data like columns name,no-null count,dtype,
# #  or even that memory usage.




# # SHAPE--





# import pandas as pd

# df=pd.read_excel(r"C:\Users\Tarun Kumar\Desktop\python\Cafe_Sales_Data_July_2025.xlsx")

# print(df.shape)


# import pandas as pd
# df=pd.read_excel(r"c:\Users\Tarun Kumar\Downloads\ecommerce_sales_dataset_15000_rows (2).csv.xlsx")
# print(df)





# # info()





# import pandas as pd

# df=pd.read_excel(r"C:\Users\Tarun Kumar\Desktop\python\Cafe_Sales_Data_July_2025.xlsx")


# print(df.info())











""" now we will move to the very important function that is """





# # DESCRIBE()-- THIS IS BASICALLY USED TO GENERATE A DESCRIPTIVIE SATATISTICS FOR NUMERICAL COLUMNS BY DEFAULT.

# # SYNTAX-DF.DESCRIBE()





# # # WHAT IT RETURNS
# # """


# # COUNT-NUMBER OF NON-NULL ENTRIES

# # MEAN- AVERAGE VALUE OF THE COLUMN

# # STD- STANDARD DEVIATION

# # MIN-MINIMUM VALUE

# # 25%-IST QUARTILE

# # 50%-MIDDLE VALUE

# # 75%-3RD QUARTILE

# # MAX-MAXIMUM VALUE
# # """

# # # LETS UNDERSTAND BY THE HELP OF EXAMPLE--



# # # STEP-01 - WE WILL CREATE A SAMPLE DATA FRAME




# import pandas as pd

# data= {
#     'Name':['ram','shayma','tarun','mohit'],
#     'Age':[10,20,30,40],
#     'Salary':[50000,40000,30000,20000],
#     'Performance':[85,90,75,80]
    
# }
# df=pd.DataFrame(data)


# print("sample dataframe")

# print(df)


# print("descriptive statics")
# print(df.describe())


# print(df.describe())







""" column selection and renaming--"""








# # # basically we used column selection to get a single columns or multiple columns--






# import pandas as pd

# data= {
#     'Name':['ram','shayma','tarun','mohit'],
#     'Age':[10,20,30,40],
#     'Salary':[50000,40000,30000,20000],
#     'Performance':[85,90,75,80]
    
# }

# df=pd.DataFrame(data)

# print("Employees Data:")

# df.rename(columns={'Name':'Emp_Name'},inplace=True)

# df.rename(columns={'Age':'Emp_age'},inplace=True)
# df.rename(columns={'Salary':'Emp_Sl'},inplace=True)
# df.rename(columns={'Performance':'Emp_PP'},inplace=True)
# print(df)






















# # """ FILTER ROWS BY BOOLEAN INDEXING-




# # # FOR EXAMPLE IF YOU WANT TO FILTER ROWS BASED ON A SINGLE CONDITIONS
# # # """




# import pandas as pd

# data= {
#     'Name':['ram','shayma','tarun','mohit'],
#     'Age':[10,20,30,40],
#     'Salary':[50000,60000,70000,80000],
#     'Performance':[85,90,75,80]
    
# }

# df=pd.DataFrame(data)


# print("where salary is more than 50000")



# print(df[df['Performance']>75])




# print("where age is more than 10")

# df2=df[df['Age']>10]

# print(df2)









""" droping columns and rows--




# it is basically used to remove the garbage or useless data from the table or dataset.



# """



# import pandas as pd
# data= {
#     'Name':['ram','shayma','tarun','mohit'],
#     'Age':[10,20,30,40],
#     'Salary':[50000,60000,70000,80000],
#     'Performance':[85,90,75,80]
    
# }
# df1=pd.DataFrame(data)


# df1.drop(0,axis=0,inplace=True)
# print(df1)

# df1.drop('Name', axis=1, inplace=True)
# print(df1)



# df1.drop('Name', axis=1, inplace=True)

# print(df1)






# # difference between axis=0 or axis=1





# # if we use axis=0 then it deletes the  columns horizontally for example it removes the row columns horizontally

# # if we use axis=1 then it deltes the veritically columns--







"""CHECK UNIQUE VALUES AND VALUES COUNTS--"""




# import pandas as pd

# data= {
#     'Name':['ram','shayma','tarun','mohit'],
#     'Age':[10,10,30,40],
#     'Salary':[50000,50000,70000,80000],
#     'Performance':[85,90,75,80]
    



# }
# df=pd.DataFrame(data)


# print("unique value in age column:")





# print("unique value in age:")


# print(df['Age'].value_counts())



# print(df['Salary'].value_counts())












""" CHAPTER-04 DATA CLEANING AND PREPROCESSING"""








# IN REAL WORLD DATASETS ,WE OFTEN DEAL WITH MESSY,INCOMPLETE OR INCONSISTENT DATA.





# THIS MODULE HELPS YOU LEARN HOW TO CLEAN AND PREPARE DATA TO ANALYSIS..





"""  HANDLING MISSING DATA--






MISIING DATA IS COMMON AND MUST BE TREATED BEFORE PERFORMING ANALYSIS--




FUNCTIONS USED-






1. ISNULL()- IT IDENTIFIES THE MISSING VALUES




2.NOTNULL()- IT IDENTIFIES NON MISSING VALUES




3.DROPNA()- DROP MISSING VALUES



4.FILLNA()-FILLS MISSING VALUES



"""






# FIRST WE WILL DISCUSS ABOUT ISNULL()--






# import pandas as pd


# data= {
#     'Name':['ram','shayma','tarun','mohit'],
#     'Age':[10,None,30,40],
#     'Salary':[50000,None,70000,80000],
#     'Performance':[85,90,None,80]
    
# }


# df=pd.DataFrame(data)


# print(df.notnull())






# note- if there is no null values it will gives you false otherwise true if it have null values














# now we will discuss about notnull()
















""" now we will discuss about fillna (values).










# like we can say that fills missing nan values with a specified value




# """



# import pandas as pd

# data= {
#     'Name':['ram','shayma','tarun','mohit'],
#     'Age':[10,None,None,40],
#     'Salary':[50000,None,70000,80000],
#     'Performance':[85,None,75,80]
    
# }
# df=pd.DataFrame(data)




# print(df['Age'].fillna(0))



# print(df['Performance'].fillna(0))



# print("salary")
# print(df['Salary'].fillna(30000))





 # note- it will replace the none value by the zero or it depend upon you . you can replace with your choice also...









"""now we will move to the next




 - that is dropna()--



 


#  it removes rows and columns that contain missing values





#  syntax-df.dropna(inplace=true)


 
# """



# import pandas as pd


# data = {
#     'Name': ['Ram', 'Shyam', 'Mohan'],
#     'Age': [25, None, 30],
#     'City': ['Delhi', 'Mumbai', 'ROORKEE']
# }

# df = pd.DataFrame(data)


# print(df.dropna())








#note- 🔹 2. dropna() → Kisi row/column me agar NaN (missing values) ho to use hataata hai




# df.dropna()                # NaN wali rows hata do
# df.dropna(axis=1)          # NaN wale columns hata do


# df.dropna(subset=['Age'])  # "Age" me jahan NaN hai, sirf wahi row hatao


# ✅ Use when: Tum missing values (NaN) ko hataana chahte ho










""" now we will discuss about the changing data types--"""










#astype()- it converts a column to a different data type







#syntax-


# import pandas as pd

# data = {
#     'Name': ['Ram', 'Shyam', 'Mohan'],
#     'Age': ['25', '20', '30'],
#     'Salary':['50000','250000','254010'],
#     'City': ['Delhi', 'Mumbai', None]
# }


# df = pd.DataFrame(data)


# print("age in numbers")

# print(df['Age'].astype(float))

# print("salary in numbers:")


# print(df['Salary'].astype(float))








# note- if age is stored as string, i convert it to integer using astype() for mathematical operations.














""" CHAPTER-05 SORTING AND RANKING ------     """









# SORTING AND RANKING ALLOW YOU TO ORGANIZE YOUR DATA BASED ON SPECIFIC COLUMNS EITHER IN ASCENDING OR DESCENDING ORDER.








""" 1.SORT_VALUES()- SORTING A DATAFRAME BY COLUMN VALUES.."""






# DEFINATION-



# the sort _values function iin pandas is used to sort a dataframe  by the values of one or more columns,either in ascending or descending order.





#synatx-  df.sort_value(by='column_name',ascending=true/false)





# lets understand by the help of example---







# import pandas as pd


# data={
#     'Emplyoee':['amit','neha','ravi','priya'],
#     'Salary':[50000,60000,30000,20000]
# }


# df=pd.DataFrame(data)



# sort employee by salary in descending order--


# print(" Sort employee by salary in Descending order")


# a=df.sort_values(by='Salary',ascending=True)

# print(a)




# print(" Sort employee by salary in Aescending order")


# sorted_df1=df.sort_values(by='Salary',ascending=True)
# print(sorted_df1)






# REAL LIFE USE CASE-SUPPOSE YOU ARE ANALYZING A COMPANY'S EMPLOYEE DATABASE AND WANT TO 


#LIST TOP 5 HIGHEST PAID EMPLOYEES--







#THIS IS WHERE SORT_VALUE() IS SUPER POWERFUL













"""2. RANK()- RANKING ROWS BY COLUMNS"""







# THE RANK FUNCTION ASSIGNS RANK VALUES TO ENTRIES BASED ON A NUMERIC COLUMN-



# USEFUL WHEN YOU WANT TO ASSIGN A POSTION OR PRIORITY TO EACH ROW..









#SYNTAX--df['column_name'].rank(method='average',ascending=true/false)





# lets understand by the help of example--





# import pandas as pd

# data={
#     'Emplyoee':['amit','neha','ravi','priya'],
#     'Age':[20,40,30,50],
#     'Salary':[20000,30000,40000,50000]
# }


# df=pd.DataFrame(data)


# # df['Age_rank']=df['Age'].rank(ascending=False)
# df['sl_rank']=df['Salary'].rank(ascending=True)
# print(df)





#note-real life use case-



# in a sales dashboard ,you can assign a rank to each salesperson based on monthly sales..






















""" CHAPTER-06 GROUPING AND AGGREGATION IN PANDAS"""










# Grouping in pandas means organizing data based on the values in one or more columns and 




#then applying  a function like(sum,mean,count)to each group.








#this is useful for summarzing or analyzing data category wise.






# syntax-of groupby():







# df.groupby('column_name')['target_column'].function()


# example--



# import pandas as pd



# data={
#     'employee':['A','B','C','D','E'],
#     'department':['HR','IT','HR','FINANCE','HR'],
#     'salary':[50000,60000,70000,80000,90000]
# }


# df=pd.DataFrame(data)


# # group by department salary


# salary = df[df['department'] == 'HR']['salary'].max()

# print("HR salary total:", salary)








""" AGGREGATION--"""


#AGGREGATION MEANS APPLYING A SUMMARY FUNCTION TO GROUPED DATA LIKE-



#SUM()- TOTAL

#MEAN()-AVERAGE

#COUNT()-NUMBER OF 

#MAX(),MIN()




# EXAMPLE- AVERAGE SALARY BY DEPARTMENT--









# import pandas as pd


# data={
#     'employee':['A','B','C','D','E'],
#     'department':['HR','IT','HR','FINANCE','HR'],
#     'salary':[50000,60000,70000,80000,90000]
# }


# df=pd.DataFrame(data)



# # group by department salary

# print("SALARY AVERAGE:")


# salary1 = df.groupby('department')['salary'].mean()
# print(salary1)


# print("SALARY SUM")

# salary2 = df.groupby('department')['salary'].sum()
# print(salary2)

# print("Maximum value:")
# salary3 = df.groupby('department')['salary'].max()
# print(salary3)


# print("Minimum value:")



# salary4 = df.groupby('department')['salary'].min()
# print(salary4)


# print("Salary Count")
# salary5 = df.groupby('department')['salary'].count()
# print(salary5)














# AGGREGATING WITH MULTIPLE COLUMNS--







# import pandas as pd


# data={
#     'employee':['A','B','C','D','E'],
#     'department':['HR','IT','HR','FINANCE','HR'],
#     'salary':[50000,60000,70000,80000,90000]
# }



# df=pd.DataFrame(data)



# result=df.groupby('department').agg({
#     'salary':['mean','max','min'],'employee':'count'
# })


# print(result)






# this return multiple stats(mean,max,min) for salary and count of employees in each department..






""" CHAPTER-07  MERGING JOINING AND CONCATENATION"""





# THESE ARE TECHNIQUES USED TO COMBINE MULTIPLE DATASETS INTO ONE --



# THINK OF IT LIKE COMBINING EXCEL SHEETS BASED ON A COMMON COLUMN- LIKE EMPLOYEE ID ) OR 




# STACKING THEM ONE OVER ANOTHER(LIKE ADDING NEW ROWS)










# 1. MERGE()-- 


# 
# 
# JUST LIKE SQL JOINS






# THIS FUNCTION COMBINES TWO DATAFRAMES USING A COMMON COLUMN(KEY).







#SYNTAX-pd.merge(df1,df2,on='employee_id',how='inner)



# # ALL THE HOW OPTION--



# #1. INNER - ONLY MATCHING ROWS IN BOTH--

# #2. LEFT- ALL ROWS FROM LEFT , MATCHING FROM RIGHT

# #3. RIGHT-ALL ROWS FROM RIGHT, MATCHING FROM LEFT

# #4.OUTER-ALL ROWS FROM BOTH (FILL NAN FOR UNMATCHED)




# # EXAMPLE--



# import pandas as pd



# employees info--


# df1=pd.DataFrame({
#     'employee_id':[1,2,3],
#     'name':['tarun','swati','apsara']
# })



# #salary info--



# df2=pd.DataFrame({
#     'employee_id':[2,3,4],
#     'salary':[20000,30000,45000]
# })



# # merge on'employee_id'



# print("inner join:")

# merged=pd.merge(df1,df2,on='employee_id',how='inner')
# print(merged)



# print("left join:")

# merged1=pd.merge(df1,df2,on='employee_id',how='left')

# print(merged1)





# print("right join:")


# merged2=pd.merge(df1,df2,on='employee_id',how='right')

# print(merged2)




# print("fullouter join:")

# merged3=pd.merge(df1,df2,on='employee_id',how='outer')

# print(merged3)










"""CONCAT()-STACK VERTICALLY OR HORIZONTALLY"""





#USED WHEN YOU WANT TO COMBINE MULTIPLE DATAFRAMES EITHER ROW WISE OR COLUMN WISE--



# EXAMPLE-01--




# #  employees info--\

# import pandas as pd



# df1=pd.DataFrame({
#     'employee_id':[1,2,3],
#     'name':['tarun','swati','apsara'],
#     'SALARY':[20000,30000,50000]
# })





# df2=pd.DataFrame({
#     'employee_id':[4,5,6],
#     'name':['raghav','misra','sara'],
#     'SALARY':[20000,30000,50000]
# })




# combined=pd.concat([df1,df2])
# print(combined)









""" CHAPTER-08 WORKING WITH DATES AND TIMES IN PANDAS"""





# DATES AND TIMES ARE VERY COMMON IN REAL-WORLD DATASETS-SUCH AS SALES DATA,EMPLOYEES RECORDS,OR WEB LOGS.



# PANDAS PROVIDES POWERFUL TOOLS TO CONERT FILTER AND EXTRACT DATE RELATED INFORMATION--




# 1, CONVERT COLUMN TO DATETIME----



# WE USE THE --  pd.to_datetime() function.


# it is used to convert a string /object column to proper datetime format..





# example-01






# import pandas as pd



# df=pd.DataFrame({
#     'order_date':['2024-01-10','2024-03-15','2025-06-15']
# })


# df['order_date']=pd.to_datetime(df['order_date'])



# # ITR CONVERT TGHE STRING OR OBJECT INTO A REAL WORLD DATE TIME FORMAT---


# print(df.dtypes)


# print("EXTRACT THE YEAR:")

# print(df['order_date'].dt.year)    


# print("EXTRACT THE MONTH:")  
#                                             # to extract the year from date
# print(df['order_date'].dt.month)

# print("EXTRACT THE DAY:")                                      # to extract the month from date
# print(df['order_date'].dt.day)                       # to extract the day from date









#note-      it helps in time based analysis like -monthly sales ,daywise orders.......





# """DATE FILTERING"""




# # YOU CAN FILTER ROWS BASED ON A SPECIFIC DATE OR RANGE..







# import pandas as pd



# df = pd.DataFrame({
#     'order_date': ['2024', '2025', '2025'],


#     'orders': [10000, 20000, 25000]
# })




# # Convert order_date to datetime

# df['order_date'] = pd.to_datetime(df['order_date'])




# # Filter for 2024 and sum orders





# df_2024 = df[df['order_date'].dt.year == 2025]['orders'].max()

# print("TOTAL ORDERS OF 2025:")


# print(df_2024)










""" CREATE DATE RANGE"""



# PANDAS CAN GENERATE SEQUENCES OF DATES USING--




# pd.date_range()



# example---



# import pandas as pd




# data_range = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')


# print(data_range)











#⚠️ Explanation:


"""    Frequency Code	Meaning	Example Use
'D'-      	Day	         Daily records


'M'	-    Month End	    Month-end dates


'MS' -   Month Start	Month-start dates

'H'	-    Hourly	        Hourly timestamps

'T'-     Minutes	        Minute intervals

'S' -	 Seconds	    Second-wise intervals"""






#CHAPTER-10 




"""EDA ka full form hota hai – Exploratory Data Analysis.


Ye Data Analysis ka pehla aur sabse important step hota hai, jisme hum data ko achhe se samajhne ki koshish karte hain visualizations, summary statistics aur patterns ke through.







🔍 EDA Kyu Zaroori Hota Hai?







EDA karne se hum yeh samajh paate hain:



Data me kya kya columns hain?



Missing values kitne hain?



Outliers hain ya nahi?



Columns ke beech relationship kya hai?


Kis column ka target variable ke saath relation strong hai?"""









"""🛠️ EDA me Kya Kya Steps Hote Hain?




Data Load Karna







import pandas as pd
df = pd.read_csv('file.csv')








Basic Information Check Karna







df.head()T TOP N ROWS 



# 
df.info()   OVERLL SUMMARY 


df.describe()  


df.shape






Missing Values Check






df.isnull().sum()




Duplicates Check





df.duplicated().sum()





Value Counts / Unique Values













df['column_name'].value_counts()




df['column_name'].nunique()


Outliers Check (boxplot se)






import seaborn as sns
sns.boxplot(df['column_name'])


Correlation Matrix






df.corr()


sns.heatmap(df.corr(), annot=True)

Histograms / Distribution

df['column_name'].hist()





sns.histplot(df['column_name'])


Pairplots for Multi-variable Relationships


sns.pairplot(df)






# """



# """



# 🧠 Final Output of EDA:



# Data ki understanding clear hoti hai



# Cleaning steps samajh aate hain



# Feature engineering ideas milte hain



# Model training ke liye data ready hota hai


# """









# """CHAPTER-09  PIVOT TABLES AND CROSS TAB IN PANDAS--"""



# # PIVOT TABLES HELP YOU TO SUMMARIZE LARGE DATASETS BY GROUPING AND AGGREGATING DATA IN COMPACT ,READABLE FORMAT..

# # IT IS SIMILAR TO HOW EXCEL PIVOT TABLES WORK






# """KEY CONCEPTS COVERERD"""





# #1. PIVOT TBLES--pd.pivot_table- a pivot table reshaped data and provides a  



# # summary by grouping rows and applying an aggregation function(like-sum ,mean,max,min) to one or more columns...




# import pandas as pd




# data = {
#     'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
#     'Salesperson': ['Amit', 'Raj', 'Priya', 'Neha', 'Amit', 'Raj', 'Priya', 'Neha'],
#     'Product': ['Laptop', 'Laptop', 'Mobile', 'Tablet', 'Tablet', 'Mobile', 'Laptop', 'Mobile'],
#     'Units_Sold': [5, 8, 10, 7, 4, 6, 9, 3],
#     'Revenue': [50000, 80000, 60000, 35000, 30000, 45000, 72000, 27000]
# }




# df = pd.DataFrame(data)


# print(df)

# print("FILTER BY PRODUCT ON THE BASIS OF REVENUE:")
# pivot1 = pd.pivot_table(df, index='Region', columns='Product', values='Units_Sold', aggfunc='sum', fill_value=0)


# print(pivot1)






#📘 What it shows:


# index='Region': Row-wise grouping by region.



# columns='Product': Each product becomes a column.



# values='Revenue': We want to analyze revenue.



# aggfunc='sum': Total revenue per region-product combo.


# fill_value=0: If no sale, show 0 instead of NaN.



# 🧠 Insight: East region earned ₹72K from Laptop, ₹60K from Mobile; no Tablet sale





# print(pivot1)




# pivot2 = pd.pivot_table(df, index='Salesperson', columns='Product', values='Units_Sold', aggfunc='sum', fill_value=0)

# print(pivot2)


"""📘 What it shows:



index='Salesperson': Each salesperson in a row.

columns='Product': Product-wise columns.

values='Units_Sold': Count of units sold.

aggfunc='sum': Total units sold.



fill_value=0: No sale = 0.



🧠 Insight: Priya sold 9 laptops and 10 mobiles, but no tablets.

"""

# print(pivot2)



# pivot3 = pd.pivot_table(df, index='Region', values='Revenue', aggfunc='mean')


"""📘 What it shows:
index='Region': Group by each region.

# values='Revenue': Column to aggregate.

# aggfunc='mean': Show average revenue per region.

# 🧠 Insight: East had the highest average revenue at ₹66K.

# """



# # print(pivot3)





# """ MULTIPLE AGGREGATION IN PIVOT TABLE--"""





# import pandas as pd



# data = {
#     'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
#     'Salesperson': ['Amit', 'Raj', 'Priya', 'Neha', 'Amit', 'Raj', 'Priya', 'Neha'],
#     'Product': ['Laptop', 'Laptop', 'Mobile', 'Tablet', 'Tablet', 'Mobile', 'Laptop', 'Mobile'],
#     'Units_Sold': [5, 8, 10, 7, 4, 6, 9, 3],
#     'Revenue': [50000, 80000, 60000, 35000, 30000, 45000, 72000, 27000]
# }



# df = pd.DataFrame(data)


# print(df)


# print("SUM OR AVERGARE BY PRODUCT WISE ON THE BEHALF ORF REGION")
# pivot1 = pd.pivot_table(df, index='Region', columns='Product', values='Revenue', aggfunc=['sum','max','min','count'],fill_value=0)

# print(pivot1)


# this is how you can apply multiple aggregation in pivot tables...








""" CROSSTAB(pd.crosstab)"""


#crosstab is similar to pivot tables but is used to count occurences(frequency)of values between two or more columns.


#example-





# import pandas as pd

# data={
#     'gender':['male','female','male','female','male'],
#     'department':['HR','IT','IT','HR','IT']
# }

# df=pd.DataFrame(data)

# ct=pd.crosstab(df['gender'],df['department'])


# print(ct)




# note- it helps understand how many males/females are in each department.











# """PROJECT-01 Online Shopping Orders Dataset"""




# import pandas as pd



# Data dictionary


# data = {
#     'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
#     'customer_id': ['C001', 'C002', 'C003', 'C001', 'C004', 'C002', 'C005'],
#     'customer_name': ['Tarun Kumar', 'Swati Sharma', 'Aman Kapoor', 'Tarun Kumar', 'Apsara Roy', 'Swati Sharma', 'Ravi Yadav'],
#     'gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
#     'product_category': ['Electronics', 'Fashion', 'Home Decor', 'Fashion', 'Electronics', 'Home Decor', 'Books'],
#     'order_date': ['2024-01-05', '2024-01-07', '2024-01-10', '2024-02-14', '2024-03-01', '2024-03-05', '2024-03-10'],
#     'order_amount': [25000, 5000, 12000, 4000, 30000, 10000, 1500],
#     'payment_method': ['Credit Card', 'UPI', 'Cash', 'Debit Card', 'Credit Card', 'UPI', 'Cash'],
#     'city': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Kolkata', 'Mumbai', 'Cash']  # NOTE: Last city is wrong, fix below
# }







# # Convert to DataFrame




# df = pd.DataFrame(data)



# # Convert order_date to datetime


# df['order_date'] = pd.to_datetime(df['order_date'])  # it coverts the order date into real time ---








# Fixing the wrong city value (Cash should be a payment method, not city)



# df.loc[df['order_id'] == 1007, 'city'] = 'Lucknow'     # Replace with actual city




# Total Sales (order_amount ka sum)



# print("Total Sales (order_amount ka sum):")


# total_sales=df['order_amount'].sum()

# total_sales1=df['order_amount'].max()

# total_sales2=df['order_amount'].min()

# total_sales3=df['order_amount'].count()



# print(total_sales,total_sales1,total_sales2,total_sales3) 





# #🔍 2. Monthly Sales Trend (Month-wise total sales)








# 3. Top-Selling Product Categorie----


# print("top selling products")


# product_category=df.groupby('product_category')['order_amount'].sum().sort_values(ascending=False)

# print(product_category)






# # #City-wise Total Sales



# print("city wise data:")


# city=df.groupby('city')['order_amount'].sum()


# print(city)





#Payment Method Preference



# print("payment mode options:")


# paymentmode=df['payment_method'].value_counts()


# print(paymentmode)





# # 6. Gender-wise Total Orders



# print("total genders:")



# total_gender=df['gender'].value_counts()


# print(total_gender)






# #🔍 7. Repeat Customers



# print("total repeat customers:")



# repeat_customers=df['customer_id'].value_counts()


# print(repeat_customers)
 




 
# #Average Order Value (AOV)



# print("Average Order Value (AOV)")


# order_value=df['order_amount'].mean()


# print(order_value)





# # 9. Most Loyal Customer (Max Orders or Amount)







# print(" 9. Most Loyal Customer (Max Orders or Amount)")


# mostloyalcustomer=df.groupby('customer_name')['order_amount'].sum().sort_values(ascending=False)


# print(mostloyalcustomer)





# # Category-wise Sales by Gender



# print(" Category-wise Sales by Gender")


# categorywise=df.pivot_table(index='product_category', columns='gender', values='order_amount', aggfunc='sum')


# print(categorywise)