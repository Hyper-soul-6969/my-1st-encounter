import pandas as pd

#Topic 1: Pandas Series and DataFrame


"""Q1. Create a Pandas Series from a list of integers [10, 20, 30, 40, 50] and assign it to a variable s.
i)	Change the index of the Series to ['a', 'b', 'c', 'd', 'e'].
ii)	Retrieve the element at index 'c'.
iii)	Calculate the sum of all elements in the Series.
iv)	Print the updated Series and the sum."""

s=pd.Series([10,20,30,40,50])      #name the series
s.index=['a','b','c','d','e']       #Change the index of the Series
element_c=s['c']                     #Retrieve the element at index 'c'
total_sum=s.sum()                     #sum of all elements in the Series
print('updated series')
print(s)
print("\n element at index c:",element_c)
print("sum of all elements:",total_sum)



"""Q2. Create a Pandas Series from a dictionary {'A': 5, 'B': 10, 'C': 15, 'D': 20, 'E': 25}.
i)	Add 5 to each element in the Series.
ii)	Find the maximum value in the Series.
iii)	Filter and display only the elements that are greater than 15.
iv)	Print the final Series and the maximum value."""

data={'A': 5, 'B': 10, 'C': 15, 'D': 20, 'E': 25}
s=pd.Series(data)     
s+=5                #Add 5 to each element 
max_value=s.max()    #maximum value in the Series
filtered_series=s[s>15]
print('updated series')
print(s)
print('\n maximum value:',max_value)
print('\n filtered series:',filtered_series)
print(filtered_series)




"""Q3. Create a Pandas DataFrame from the following data:
“data = {'Product': ['A', 'B', 'C', 'D'], 'Price': [100, 150, 200, 250], 'Quantity': [10, 15, 20, 25]}”
i)	Assign the DataFrame to a variable df.
ii)	Calculate the total sales for each product (Price * Quantity) and add it as a new column TotalSales.
iii)	Find the product with the highest total sales.
iv)	Display the DataFrame sorted by TotalSales in descending order.
v)	Print the updated DataFrame and the product with the highest total sales."""

data = {'Product': ['A', 'B', 'C', 'D'], 
        'Price': [100, 150, 200, 250], 
        'Quantity': [10, 15, 20, 25]}
df=pd.DataFrame(data)      #Assign the DataFrame to a variable df
df['TotalSales']= df['Price']*df['Quantity']    #add a new column
max_product = df.loc[df['TotalSales'].idxmax(), 'Product']   #product with the highest total sales
df_sorted = df.sort_values(by='TotalSales', ascending=False)   #DataFrame sorted by TotalSales in descending order
print('updated DataFrame',df_sorted)
print(f"\n product with highest TotalSales:{max_product}")
print("df_sorted")




"""Q4. Create a Pandas DataFrame from the following data:
“data = {'CustomerID': [1, 2, 3, 4, 5], 'Purchase': [250, None, 150, 300, None]}”
i)	Assign the DataFrame to a variable df.
ii)	Replace the missing values in the Purchase column with the average value of the column.
iii)	Group the DataFrame by CustomerID and calculate the total purchase amount for each customer.
iv)	Print the cleaned DataFrame and the grouped DataFrame with total purchase amounts."""


data = {'CustomerID': [1, 2, 3, 4, 5], 'Purchase': [250, None, 150, 300, None]}
df = pd.DataFrame(data)
average_purchase = df['Purchase'].mean()      #Replace missing values with the average
df['Purchase'].fillna(average_purchase, inplace=True)
grouped_df = df.groupby('CustomerID')['Purchase'].sum().reset_index()    #Group the DataFrame by CustomerID and calculate total purchase
print("Cleaned DataFrame:")
print(df)       
print("\n Grouped DataFrame (Total Purchase by CustomerID):")
print(grouped_df)


#Topic 2: Pandas Grouping and Aggregating


"""Q5. Create a DataFrame df with the following data:
“data = {'Category': ['A', 'B', 'A', 'B', 'A'], 'Values': [10, 20, 30, 40, 50]}”
“df = pd.DataFrame(data)”
i)	Group the data by the 'Category' column.
ii)	Calculate the sum of 'Values' for each category.
iii)Print the resulting grouped DataFrame"""


data = {'Category': ['A', 'B', 'A', 'B', 'A'], 
        'Values': [10, 20, 30, 40, 50]} 
df=pd.DataFrame(data)
grouped_df = df.groupby('Category')['Values'].sum().reset_index()    #Group the data by the 'Category' column
print(grouped_df)



"""Q6. Create a DataFrame df with the following data:
“data = {'Product': ['X', 'Y', 'X', 'Y', 'X'], 'Sales': [200, 150, 250, 300, 100]}”
“df = pd.DataFrame(data)”
i)	Group the data by the 'Product' column.
ii)	Apply multiple aggregation functions (mean, sum, and count) to the 'Sales' column.
iii)	Print the resulting aggregated DataFrame."""

data = {'Product': ['X', 'Y', 'X', 'Y', 'X'], 
        'Sales': [200, 150, 250, 300, 100]}
df=pd.DataFrame(data)
agg_df=df.groupby('Product')['Sales'].agg(['mean','sum','count'])   #Group by 'Product' and apply multiple aggregation functions
print('aggregrated DataFrame:')
print(agg_df) 




"""Q7. Create a DataFrame df with the following data:
“data = {'Department': ['HR', 'IT', 'HR', 'IT', 'HR'], 'Salary': [50000, 70000, 60000, 80000, 55000]}”
“df = pd.DataFrame(data)”
i)	Group the data by the 'Department' column.
ii)	Define a custom aggregation function that calculates the range (max - min) of the 'Salary' column for each department.
iii)	Apply the custom aggregation function and print the resulting DataFrame."""

data = {'Department': ['HR', 'IT', 'HR', 'IT', 'HR'], 
        'Salary': [50000, 70000, 60000, 80000, 55000]}
df=pd.DataFrame(data)
def salary_range(x):
    return x.max() - x.min() 
grouped_df=df.groupby('Department')['Salary'].agg(salary_range).reset_index()
grouped_df.rename(columns={'Salary': 'Salary_Range'}, inplace=True)
print('grouped dataframe with salary range')
print(grouped_df)



"""Q8. Create a DataFrame df with the following data:
“data = {'Region': ['North', 'South', 'North', 'South', 'North'], 'Product': ['A', 'A', 'B', 'B', 'A'], 'Sales': [100, 150, 200, 250, 300]}”
“df = pd.DataFrame(data)”
i)	Group the data by both 'Region' and 'Product' columns.
ii)	Calculate the total sales for each group.
iii)	Print the resulting grouped DataFrame""" 

data = {'Region': ['North', 'South', 'North', 'South', 'North'], 
        'Product': ['A', 'A', 'B', 'B', 'A'], 
        'Sales': [100, 150, 200, 250, 300]}
df=pd.DataFrame(data)
grouped_df=df.groupby(['Region','Product'])['Sales'].sum().reset_index()
print('grouped dataframe with total sales')
print(grouped_df)


#Topic3: Pandas Merging and Joining

"""Q9. Create two DataFrames df1 and df2 with the following data:
DataFrame 1:
“data1 = {'ID': [1, 2, 3, 4], 'Name': ['Alice', 'Bob', 'Charlie', 'David']}”
“df1 = pd.DataFrame(data1)”
DataFrame 2:
“data2 = {'ID': [3, 4, 5, 6], 'Score': [85, 90, 75, 80]}”
“df2 = pd.DataFrame(data2)”
i)	Perform an inner join on df1 and df2 using the 'ID' column.
ii)	Print the resulting DataFrame."""


data1 = {'ID': [1, 2, 3, 4], 'Name': ['Alice', 'Bob', 'Charlie', 'David']}
df1 = pd.DataFrame(data1)

data2 = {'ID': [3, 4, 5, 6], 'Score': [85, 90, 75, 80]}
df2 = pd.DataFrame(data2)

result=pd.merge(df1,df2,on='ID',how='inner')
print('result on inner join:')
print(result)



"""Q10. Create two DataFrames df1 and df2 with the following data:
DataFrame 1:
“data1 = {'EmployeeID': [101, 102, 103, 104], 'EmployeeName': ['John', 'Jane', 'Jim', 'Jack']}”
“df1 = pd.DataFrame(data1)”
DataFrame 2”
“data2 = {'EmployeeID': [103, 104, 105, 106], 'Department': ['HR', 'IT', 'Finance', 'Marketing']}”
“df2 = pd.DataFrame(data2)”
i)	Perform a left join on df1 and df2 using the 'EmployeeID' column.
ii)	Print the resulting DataFrame"""


data1 = {'EmployeeID': [101, 102, 103, 104], 'EmployeeName': ['John', 'Jane', 'Jim', 'Jack']}
df1 = pd.DataFrame(data1)

data2 = {'EmployeeID': [103, 104, 105, 106], 'Department': ['HR', 'IT', 'Finance', 'Marketing']}
df2 = pd.DataFrame(data2)

result = pd.merge(df1, df2, on='EmployeeID', how='left')
print('result on Left join:')
print(result)



"""Q11. Create two DataFrames df1 and df2 with the following data:
DataFrame 1: 
“data1 = {'StudentID': [201, 202, 203, 204], 'StudentName': ['Sam', 'Sara', 'Sue', 'Scott']}
“df1 = pd.DataFrame(data1)”
DataFrame 2:
“data2 = {'StudentID': [202, 204, 205, 206], 'Grade': ['A', 'B', 'C', 'D']}”
“df2 = pd.DataFrame(data2)”
i)	Perform a right join on df1 and df2 using the 'StudentID' column.
ii)	Print the resulting DataFrame"""

data1 = {'StudentID': [201, 202, 203, 204], 'StudentName': ['Sam', 'Sara', 'Sue', 'Scott']}
df1 = pd.DataFrame(data1)

data2 = {'StudentID': [202, 204, 205, 206], 'Grade': ['A', 'B', 'C', 'D']}
df2 = pd.DataFrame(data2)

result=pd.merge(df1,df2,on='StudentID',how='right')
print('result on right join:')
print(result)



"""Q12. Create two DataFrames df1 and df2 with the following data:
DataFrame 1:
“data1 = {'OrderID': [301, 302, 303], 'Product': ['Laptop', 'Tablet', 'Smartphone']}”
“df1 = pd.DataFrame(data1)”
DataFrame 2:
“data2 = {'OrderID': [302, 304, 305], 'Quantity': [3, 2, 5]}”
“df2 = pd.DataFrame(data2)”

i)	Perform an outer join on df1 and df2 using the 'OrderID' column.
ii)	Print the resulting DataFrame."""

data1 = {'OrderID': [301, 302, 303], 'Product': ['Laptop', 'Tablet', 'Smartphone']}
df1 = pd.DataFrame(data1)

data2 = {'OrderID': [302, 304, 305], 'Quantity': [3, 2, 5]}
df2 = pd.DataFrame(data2)

result=pd.merge(df1,df2,on='OrderID',how='outer')
print('result on outer join:')
print(result)



"""Q13. Create two DataFrames df1 and df2 with the following data:
DataFrame 1: 
“data1 = {'FirstName': ['Tom', 'Jerry', 'Mickey', 'Donald'], 'LastName': ['Smith', 'Brown', 'Mouse', 'Duck'],'Age': [25, 30, 35, 40]}”
“df1 = pd.DataFrame(data1)”
DataFrame 2:
“data2 = {'FirstName': ['Jerry', 'Mickey', 'Tom', 'Donald'], 'LastName': ['Brown', 'Mouse', 'Smith', 'Duck'], 'Salary': [70000, 60000, 50000, 80000]}”
“df2 = pd.DataFrame(data2)”
i)	Merge df1 and df2 on both 'FirstName' and 'LastName' columns.
ii)	Print the resulting DataFrame."""

data1 = {'FirstName': ['Tom', 'Jerry', 'Mickey', 'Donald'], 'LastName': ['Smith', 'Brown', 'Mouse', 'Duck'],'Age': [25, 30, 35, 40]}
df1 = pd.DataFrame(data1)

data2 = {'FirstName': ['Jerry', 'Mickey', 'Tom', 'Donald'], 'LastName': ['Brown', 'Mouse', 'Smith', 'Duck'], 'Salary': [70000, 60000, 50000, 80000]}
df2 = pd.DataFrame(data2)

result=pd.merge(df1,df2,on=['FirstName','LastName'],how='inner')
print('merged DataFrame')
print(result)


#Topic 4: Error Handling

"""Q14. Write a Python function divide(a, b) that takes two arguments a and b and returns the result of dividing a by b.
i)	Implement error handling to manage the case when b is zero, and display an appropriate error message.
ii)	Test the function with different values of a and b (including zero)"""

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

print(divide(10, 2))  # Valid division
print(divide(10, 0))  # Division by zero



"""Q15. Write a Python function get_integer_input() that prompts the user to enter an integer.
i)	Implement error handling to manage the case when the user enters a non-integer value, and prompt the user to enter a valid integer until they do so.
ii)	Test the function with different types of user input"""

def get_integer_input():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Test the function
value = get_integer_input()
print(f"You entered: {value}")

