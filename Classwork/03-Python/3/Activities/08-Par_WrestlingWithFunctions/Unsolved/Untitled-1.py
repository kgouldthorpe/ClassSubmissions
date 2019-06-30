#%% [markdown]
# # <span style="color:blue">Introduction to Pandas</span>
# 
# Pandas is a Python module that contains structures and functions useful for data exploration and analysis.
# The two main data structures Pandas introduces are **Series** and **DataFrames**.
#%% [markdown]
# ---
# ## <span style="color:blue">Pandas Series</span>
# - 1-D data structure (similar to Python lists, or an Excel column)
# - Can contain multiple data types, but usually should contain data of one type
# - Create a Pandas Series by passing in a **list** to **pd.Series()**
# - By default, a Pandas Series will have an index that starts at 0; can access specific values using this index
# - Learn more: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html

#%%
# Import Pandas module

import pandas as pd


#%%
# Creating a Pandas Series

my_list = [100, 200, 400, 600, 900]
my_series = pd.Series(my_list)
my_series


#%%
# Accessing specific values within Series

print(my_series[1]) # will print 200
print(my_series[3]) # will print 600

#%% [markdown]
# ---
# ## <span style="color:blue">Pandas DataFrames</span>
# - 2-D data structure with labeled rows and columns (similar to tables in Excel)
#     - For example: if we were looking at traffic violations data for NYC, each row could represent a violation instance, and each column could represent a specific attribution of a violation (date, amount of fine, location, etc.)
# - Create a Pandas Dataframe by using **pd.DataFrame()**, and passing in either a **list of dictionaries**, or a **dictionary with lists**
# - A lot of data in the real world will be provided in tabular format which can be easily translated into DataFrames
# - Learn more: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

#%%
# Creating a Pandas DataFrame by passing in a LIST OF DICTIONARIES
# Each value in the list is a dictionary
# Imagine that each dictionary represents a row of data in our eventual dataframe
# Each dictionary should have the same keys, since these keys dictate the column headers of our dataframe

my_list = [{"id": 1, "name": "Bob", "account_balance": 500.14},
           {"id": 2, "name": "Amanda", "account_balance": 300.42},
           {"id": 3, "name": "Jill", "account_balance": 943.54},
           {"id": 4, "name": "Dylan", "account_balance": 112.53},
           {"id": 5, "name": "Alex", "account_balance": 895.51}]

my_df_1 = pd.DataFrame(my_list)
my_df_1


#%%
# Re-create the previous Pandas DataFrame, passing in a DICTIONARY WITH LISTS
# The keys of the dictionary represent the column headers of our eventual dataframe
# The lists contain the data for each column

my_dict = {"id": [1, 2, 3, 4, 5],
           "name": ["Bob", "Amanda", "Jill", "Dylan", "Alex"],
           "account_balance": [500.14, 300.42, 943.54, 112.53, 895.51]}

my_df_2 = pd.DataFrame(my_dict)
my_df_2


#%%
# Select a single column from a dataframe by passing in the column's name into square brackets

my_df_2["account_balance"]


#%%
# You can also select a single column and assign it to another variable

names_col = my_df_2["name"]
names_col


#%%
# Now names_col contains only the "names" column

print(names_col[1])


#%%
# Select multiple columns from a dataframe by passing in a list of the names of the columns

my_df_2[["name", "account_balance"]]

#%% [markdown]
# ---
# ## <span style="color:blue">Important DataFrame Functions</span>
# **.head()** returns the first 5 rows of data

#%%
# Create a new DataFrame that represents purchase data from an online retailer

my_dict_2 = {"order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
             "price": [13.50, 9.99, 12.00, 29.99, 
                       14.99, 7.99, 3.49, 10.00, 
                       9.99, 17.99, 20.00, 21.00, 14.99],
             "purchase_category": ["Apparel", "Sports", "Toys", 
                                   "Apparel", "Apparel", "Household", 
                                   "Household", "Toys", "Sports", 
                                   "Sports", "Apparel", "Household", "Apparel"],
             "clicked_ad": [True, True, False, True, False, 
                            True, True, False, False, True, 
                            True, True, False]}
purchase_df = pd.DataFrame(my_dict_2)


#%%
# Show the first 5 rows of data using .head()
# .head() is great for getting a taste of the data you're dealing with

purchase_df.head()

#%% [markdown]
# **.describe()** returns a table of summary statistics on numeric columns in a dataframe

#%%
# Note that .describe() will only return summary statistics for your numeric columns
# In this case, statistics for order_id and price columns are returned

purchase_df.describe()

#%% [markdown]
# **.mean()** returns the average of all values in a given column or dataframe

#%%
# Return the mean of the price column

purchase_df["price"].mean()

#%% [markdown]
# **.sum()** returns the sum of all values in a given column or dataframe

#%%
# Return the sum of all values in the order_id column

purchase_df["order_id"].sum()


#%%
# These values can also be assigned to variables

mean_price = purchase_df["price"].mean()
sum_order_id = purchase_df["order_id"].sum()

mean_price + sum_order_id

#%% [markdown]
# **.unique()** returns an array of all of the unique values within a given column

#%%
# Returns unique values in the purchase_category column

unique_pcat = purchase_df["purchase_category"].unique()
print(unique_pcat)
print(unique_pcat[2])

#%% [markdown]
# **.value_counts()** returns an array containing the # of times each unique value occurs in a given column

#%%
# Returns the value counts of each unique value in the purchase_category column

print(purchase_df["purchase_category"].value_counts())

#%% [markdown]
# ---
# ## <span style="color:blue">Exploring Pandas DataFrames</span>
# 
# Two functions exist to make life easier when trying to slice and dice any DataFrame: **.iloc[ ]** and **.loc[ ]**
#%% [markdown]
# **.iloc[ ]** uses the *numeric* indexes of a dataframe's rows and columns to return specific values

#%%
# Use the purchase_df dataframe created above

purchase_df

#%% [markdown]
# There are several possible ways to use **.iloc[ ]**
# <br>
# The general structure is: **.iloc[*rows you want*, *columns you want*]**
# - Use single values to just get one row/column
# - Use a colon (:) to get all rows/columns
# - Use a list to get specific rows/columns
# - Use a range(x:y) to get a range of rows/columns

#%%
# To return ALL ROWS and COLUMN 2 (order_id)

purchase_df.iloc[ : , 1]

# The colon before the comma in .iloc[] means we want ALL rows
# The 1 after the comma means we want the column at index 1


#%%
# To return ROWS 1 THROUGH 4 (including 4), and ALL COLUMNS

purchase_df.iloc[0:4, : ]


#%%
# To returns ROWS 2, 3, AND 5, and COLUMNS 2 THROUGH 4 (including 4)

purchase_df.iloc[[1, 2, 4], 1:4]

#%% [markdown]
# **.loc[ ]** uses the *named* indexes of a dataframe's rows and columns to return specific values.
#%% [markdown]
# The general structure for .loc[] is the same as that for .iloc[], except named indexes are used instead of numeric indexes
# <br>
# A column's named index is simply its **column name**
# <br>
# By default, when we create a dataframe, a row's index is numeric and starts at 0. You can set a named index for a dataframe's rows by using **.set_index()**

#%%
# Create a new dataframe
example_dict = {"first_name": ["Bill", "James", "Tyler", "Matt", "Jon"],
                "last_name": ["Smith", "Alvarez", "Dant", "May", "Livingston"],
                "age": [25, 34, 52, 26, 43],
                "credit_score": [721, 683, 761, 641, 602]}
credit_df = pd.DataFrame(example_dict)
credit_df


#%%
# Set the row index to be the first_name

credit_df = credit_df.set_index("first_name")
credit_df


#%%
# Now, we can filter this dataframe using .loc[]

# Return data for James' and Tyler's rows, ALL COLUMNS included

credit_df.loc[["James", "Tyler"], : ]


#%%
# Return rows from Bill to Matt (including Matt), and only the age and credit_score columns

credit_df.loc["Bill":"Matt", ["age", "credit_score"]]


#%%
# Return all rows, only the credit_score column

credit_df.loc[ : , "credit_score"]

#%% [markdown]
# Remember, you can get the same data you want using either .loc[ ] or .iloc[ ]
# <br>
# The two functions essentially perform the same task, but with different methods of operation

#%%



