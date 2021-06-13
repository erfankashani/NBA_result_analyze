#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:48:49 2020

@author: erfankashani
Credit: https://www.kaggle.com/kanncaa1/data-sciencetutorial-for-beginners

when using spider:
    to run a line: f9
    to comment   : cmd + 1

General Directory management
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np                   # for linear algebra
import pandas as pd                  # data proccessing, CSV file I/O (example pd.read_scv)
import matplotlib.pyplot as plt
import seaborn as sns                # visualiazation tool

# checking the project directory
from subprocess import check_output
print(check_output(["ls", "-R", "./"]).decode("utf8"))

## adding database
data  = pd.read_csv("./DATABASE/pokemon_challenge/pokemon.csv")
data.head(10)
data.info()

# check data correlation
data.corr()

f, ax = plt.subplots(figsize=(18,18))
sns.heatmap(data.corr(), annot=True, linewidth=0.5, fmt= '0.1f', ax=ax)
plt.show()
# plt.savefig('graph1.png')
plt
## Using matplot to visualize the data

# Line Plot
# color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
data.Speed.plot(kind = 'line', color = 'g',label = 'Speed',linewidth=1,alpha = 0.5,grid = True,linestyle = ':')
data.Defense.plot(color = 'r',label = 'Defense',linewidth=1, alpha = 0.5,grid = True,linestyle = '-.')
plt.legend(loc='upper right')     # legend = puts label into plot
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.title('Line Plot')            # title = title of plot
plt.show()

# Scatter Plot
# x = attack, y = defense
data.plot(kind='scatter', x='Attack', y='Defense',alpha = 0.5,color = 'red')
plt.xlabel('Attack')              # label = name of label
plt.ylabel('Defence')
plt.title('Attack Defense Scatter Plot')            # title = title of plot

# Histogram
# bins = number of bar in figure
data.Speed.plot(kind = 'hist',bins = 50,figsize = (12,12))
plt.show()

# if you want to clear the plot
plt.clf() 


## practise with dictionaries
dictionary = {"spain": "madrid", "canada": "ottawa"}    # define the dictionary
dictionary["spain"] = "barcelona"                       # update existing entry
dictionary["france"] = "paris"                          # add new entry
del dictionary["spain"]                                 # delete the entry spain
print(dictionary)                                       # print the dictionary
print("france" in dictionary)                           # check if a key exist
print(dictionary["france"])                             # check the value of the key


## Using Pandas library 

# objects in series or data_frame models
series = data["Defense"]                                # data['Defense'] = series
print(type(series))
data_frame = data[['Defense']]
print(type(data_frame))

# 1 - Filtering Pandas data frame
x = data['Defense']>200     # There are only 3 pokemons who have higher defense value than 200
data[x]

# 2 - Filtering pandas with logical_and
# There are only 2 pokemons who have higher defence value than 2oo and higher attack value than 100
data[np.logical_and(data['Defense']>200, data['Attack']>100 )]

# This is also same with previous code line. Therefore we can also use '&' for filtering.
data[(data['Defense']>200) & (data['Attack']>100)]

# Stay in loop if condition( i is not equal 5) is true
lis = [1,2,3,4,5]
for i in lis:
    print('i is: ',i)
print('')

# Enumerate index and value of list
# index : value = 0:1, 1:2, 2:3, 3:4, 4:5
for index, value in enumerate(lis):
    print(index," : ",value)
print('')   

# For dictionaries
# We can use for loop to achive key and value of dictionary. We learnt key and value at dictionary part.
dictionary = {'spain':'madrid','france':'paris'}
for key,value in dictionary.items():
    print(key," : ",value)
print('')

# For pandas we can achieve index and value
for index,value in data[['Attack']][0:1].iterrows():
    print(index," : ",value)


## Some more python knowledge

# docstrings: documentation for functions. Example:
# for f():
# """This is docstring for documentation of function f"""

# tuple: sequence of immutable python objects.
# cant modify values
# tuple uses paranthesis like tuble = (1,2,3)
# unpack tuple into several variables like a,b,c = tuple

def tuple_ex():
    """ return defined t tuple"""
    t = (1,2,3)
    return t
a,b,c = tuple_ex()
print(a,b,c)

# Scope: what we need to know about scope
# global: defined main body in script
# local: defined in a function
# built in scope: names in predefined built in scope module such as print, len

# guess prints what
x = 2
def f():
    x = 3
    return x
print(x)      # x = 2 global scope
print(f())    # x = 3 local scope

# How can we learn what is built in scope
# import builtins
# dir(builtins)

# DEFAULT and FLEXIBLE ARGUMENTS
# Default argument example:
# def f(a, b=1):
#   """ b = 1 is default argument"""
# Flexible argument example:
# def f(*args):
#  """ *args can be one or more"""

# def f(** kwargs)
#  """ **kwargs is a dictionary"""

# flexible arguments *args
def f(*args):
    for i in args:
        print(i)
f(1)
print("")
f(1,2,3,4)
# flexible arguments **kwargs that is dictionary
def f(**kwargs):
    """ print key and value of dictionary"""
    for key, value in kwargs.items():               # If you do not understand this part turn for loop part and look at dictionary in for loop
        print(key, " ", value)
f(country = 'spain', capital = 'madrid', population = 123456)

# LAMBDA FUNCTION: Faster way of writing function
# lambda function
square = lambda x: x**2     # where x is name of argument
print(square(4))
tot = lambda x,y,z: x+y+z   # where x,y,z are names of arguments
print(tot(1,2,3))

# Anonymous function: Like lambda function but it can take more than one arguments.
number_list = [1,2,3]
y = map(lambda x:x**2,number_list)
print(list(y))

# Iterators: iterable is an object that can return an iterator
# iterable: an object with an associated iter() method
# example: list, strings and dictionaries
# iterator: produces next value with next() method
# iteration example
name = "ronaldo"
it = iter(name)
print(next(it))    # print next iteration
print(*it)         # print remaining iteration

# zip(): zip lines
# zip example
list1 = [1,2,3,4]
list2 = [5,6,7,8]
z = zip(list1,list2)
print(z)
z_list = list(z)
print(z_list)

# List Compression: collapse for loops for building lists into a single line
# Example of list comprehension
num1 = [1,2,3]
num2 = [i + 1 for i in num1 ]
print(num2)
# Conditionals on iterable
num1 = [5,10,15]
num2 = [i**2 if i == 10 else i-5 if i < 7 else i+5 for i in num1]
print(num2)
# lets return pokemon csv and make one more list comprehension example
# lets classify pokemons whether they have high or low speed. Our threshold is average speed.
threshold = sum(data.Speed)/len(data.Speed)
data["speed_level"] = ["high" if i > threshold else "low" for i in data.Speed]
data.loc[:10,["speed_level","Speed"]] # we will learn loc more detailed later


######################### Cleaning data #########################

# we are using the same data form in the top of the tutorial

# shape gives number of rows and columns in a tuble
data.shape

# you can check the data's min, max, count, mean, std, from describe() function
data.describe()

# For example: compare attack of pokemons that are legendary  or not
# Black line at top is max
# Blue line at top is 75%
# Green line is median (50%)
# Blue line at bottom is 25%
# Black line at bottom is min
# There are no outliers
data.boxplot(column='Attack',by = 'Legendary')

# Tidy data
# melting two column into one
# Firstly I create new data from pokemons data to explain melt nore easily.
data_new = data.head()    # I only take 5 rows into new data
data_new
# lets melt
# id_vars = what we do not wish to melt
# value_vars = what we want to melt
melted = pd.melt(frame=data_new,id_vars = 'Name', value_vars= ['Attack','Defense'])
melted
# Pivoting data: reverse of melting
# Index is name
# I want to make that columns are variable
# Finally values in columns are value
melted.pivot(index = 'Name', columns = 'variable',values='value')

# concentrate data: concatenate two dataframe
# Firstly lets create 2 data frame
data1 = data.head()
data2= data.tail()
# concat top to bottom
conc_data_row = pd.concat([data1,data2],axis =0,ignore_index =True) # axis = 0 : adds dataframes in row
conc_data_row
# concat right to left
data1 = data['Attack'].head()
data2= data['Defense'].head()
conc_data_col = pd.concat([data1,data2],axis =1) # axis = 1 : adds dataframes in column
conc_data_col


# Data types
# There are 5 basic data types: object(string),boolean, integer, float and categorical.
# We can make conversion data types like from str to categorical or from int to float
# Why is category important:

# make dataframe smaller in memory
# can be utilized for anlaysis especially for sklearn(we will learn later)
data.dtypes                                     # will check the data type of columns
# lets convert object(str) to categorical and int to float.
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')
# As you can see Type 1 is converted from object to categorical
# And Speed ,s converted from int to float
data.dtypes


## Dealing with Missing data and testing with assert

# If we encounter with missing data, what we can do:
# leave as is
# drop them with dropna()
# fill missing value with fillna()
# fill missing values with test statistics like mean
# Assert statement: check that you can turn on or turn off when you are done with your testing of the program

# we can see there are 800 entries but type 2 only has 414 or name has 799 so they have some NAN values
data.info();
# lets focus on type 2 column, there are 386 NaN values
data["Type 2"].value_counts(dropna =False)
# Lets drop nan values
data1=data   # also we will use data to fill missing value so I assign it to data1 variable
data1["Type 2"].dropna(inplace = True)  # inplace = True means we do not assign it to new variable. Changes automatically assigned to data
# now use asserts to check your work
# assert 1==1 will return nothing cause its true
# assert 1==2 will throw an AssertionError which tells you statement is wrong
assert  data['Type 2'].notnull().all() # returns nothing because we drop nan values
# now lets fill the rows
data["Type 2"].fillna('empty',inplace = True)
#check your work
assert  data['Type 2'].notnull().all() # returns nothing because we do not have nan values

## More review for pandas

# single column = series
# NaN = not a number
# dataframe.values = numpy

# we can build data frams from csv files, from dictionaries using zip() function
# we can also add new columns and
# broadcasting: Create new column and assign a value to entire column  

# make data frames from dictionary
country = ["Spain","France"]
population = ["11","12"]
list_label = ["country","population"]
list_col = [country,population]
zipped = list(zip(list_label,list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
df
# Add new columns
df["capital"] = ["madrid","paris"]
df
# Broadcasting
df["income"] = 0                                    #Broadcasting entire column
df


## Visualizing Exploratory Data

# Plot
# Subplot
# Histogram:
#  bins: number of bins
#  range(tuble): min and max values of bins
#  normed(boolean): normalize or not
#  cumulative(boolean): compute cumulative distribution

# Plotting all data 
data1 = data.loc[:,["Attack","Defense","Speed"]]
data1.plot()
# it is confusing
# subplots
data1.plot(subplots = True)
plt.show()
# scatter plot  
data1.plot(kind = "scatter",x="Attack",y = "Defense")
plt.show()
# hist plot  
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),normed = True)
# histogram subplot with non cumulative and cumulative
fig, axes = plt.subplots(nrows=2,ncols=1)
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),density = True,ax = axes[0])
data1.plot(kind = "hist",y = "Defense",bins = 50,range= (0,250),density = True,ax = axes[1],cumulative = True)
plt.savefig('graph.png')
plt

## Working with Pandas Time Series

# datetime = object
# parse_dates(boolean): Transform date to ISO 8601 (yyyy-mm-dd hh:mm:ss ) format
time_list = ["1992-03-08","1992-04-12"]
print(type(time_list[1])) # As you can see date is string
# however we want it to be datetime object
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))

# close warning
import warnings
warnings.filterwarnings("ignore")
# In order to practice lets take head of pokemon data and add it a time list
data2 = data.head()
date_list = ["1992-01-10","1992-02-10","1992-03-10","1993-03-15","1993-03-16"]
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object
# lets make date as index
data2= data2.set_index("date")
data2 
# Now we can select according to our date index
print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])

# RESAMPLING PANDAS TIME SERIES
# Resampling: statistical method over different time intervals
# Needs string to specify frequency like "M" = month or "A" = year
# Downsampling: reduce date time rows to slower frequency like from daily to weekly
# Upsampling: increase date time rows to faster frequency like from daily to hourly
# Interpolate: Interpolate values according to different methods like ‘linear’, ‘time’ or index’

# We will use data2 that we create at previous part
data2.resample("A").mean()                  # grabs our time indexed data and return the results based on annual results
# Lets resample with month
data2.resample("M").mean()
# As you can see there are a lot of nan because data2 does not include all months
# In real life (data is real. Not created from us like data2) we can solve this problem with interpolate
# We can interpolete from first value
data2.resample("M").first().interpolate("linear")
# Or we can interpolate with mean()
data2.resample("M").mean().interpolate("linear")

# INDEXING DATA FRAMES
# Indexing using square brackets
# Using column attribute and row label
# Using loc accessor
# Selecting only some columns

# read data
data = pd.read_csv('../input/pokemon.csv')
data= data.set_index("#")
data.head()
# indexing using square brackets
data["HP"][1]
# using column attribute and row label
data.HP[1]
# using loc accessor
data.loc[1,["HP"]]
# Selecting only some columns
data[["HP","Attack"]]

## SLICING DATA FRAME

# Difference between selecting columns
# Series and data frames
# Slicing and indexing series
# Reverse slicing
# From something to end
# Difference between selecting columns: series and dataframes
print(type(data["HP"]))     # series
print(type(data[["HP"]]))   # data frames
# Slicing and indexing series
data.loc[1:10,"HP":"Defense"]   # 10 and "Defense" are inclusive
# Reverse slicing 
data.loc[10:1:-1,"HP":"Defense"]
# From something to end
data.loc[1:10,"Speed":] 