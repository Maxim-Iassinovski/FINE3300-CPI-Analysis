'''Pandas is a library to manage tabular data
# Pandas as a library name is derived from "panel data"
# panda is like a spreadsheet in python
# Anything that can be done in excel can be done in python
# Pandas is fast and powerful but downside is it has a large memory footprint
# to install
#to use pandas in python wrtie "import pandas as pd" in the code
#later downstream in the methods/functions when it is used, we reference pd.  <-- and then type the command
'''
'''
#---------------------------------------------------------------------------------
#EXAMPLE 1 - PRINTING A FLAT STRING OF THE ENTIRE DICTIONARY
#importing pandas library into code
import pandas as pd

#creating a dictionary (squiggly lines denote a dictionary)
dataset = {'model': ['RAV4', 'CRV', 'CAMRY', 'ACCORD', 'RDX', 'MDX'],
           'cylinders': [4, 4, 4, 4, 6, 6]}

#prints string of the entire dictionary
print(dataset)
print(100* '-')

data_frame = pd.DataFrame(dataset)

print(data_frame)

#In pandas, a "series" is a column of data, or an array/list
'''
'''
#You can also export dataframe files to csv, excel or other file types as so:
data_frame.to_csv('filename.csv')

data_frame.to_excel('filename.xlsx')
'''

#NOTES
'''
# take pandas library, reference library called DataFrame, pass data srt into it
#take data that I have, and form a data set, then print the data_frame.
data_frame = pd.DataFrame(dataset)
print(data_frame)

#A series in a panda is a column of data
#prev example has two columns which pandas interpreted them as two series and created a data frame 

#most times, instead of inputting data manually, you will receive the data as a file, (e.g. csv/excel file)
# you can read excel data directly into pandas and form a data frame out of it
data_frame = pd.read_csv('DataSet.6A.csv')

#if you print a large data set it may not print more than 60 lines but that can be changed like this:
pd.options.display.max_rows = 1000

#Data in a pandas data frame can be exported into multiple formats such as csv, excel, json:
#df.to_csv('filename.csv')

# Python and pandas is great for automating routine tasks in excel.

#To print the column headings along with a few intitial rows:
print(data_frame.head(5))
print(data_frame.tail(2))

#to print the size in memeory, number of rows, column data type and the number of non-null values:
print(data_frame.info())
#print(data_frame.dtypes())

#To Access a column in a data frame:
data_frame['COLUMN_NAME']

#to Acessa row in a data frame, you cannot do the same as columns, you need to
#call on a method called iloc[m:n], where m is the row number. And if you want
#to access a row



#Filtering Data - how would you know you want to access an item in a specific row? Filtering data can
#help sort through the data based on certain criteria. E.g. bonds with a maturity with 10 years or less, etc.
'''

#----------------------------------------------------------------------------
#EXAMPLE #2:
import pandas as pd
dataset = {'model': ['RAV4', 'CRV', 'CAMRY', 'ACCORD', 'RDX', 'MDX',],
            'cylinders': [4, 4, 4, 4, 6, 6]}       
                     
data_frame = pd.DataFrame(dataset)

print(data_frame['cylinders'] == 4)
print(100*'-')

print(data_frame[data_frame['cylinders']== 4])
print(100*'-')

print(data_frame[data_frame['cylinders'] == 4]['model'])

print(data_frame.columns)


'''
#----------------------------------------------------------------------------
#EXAMPLE 3:
dataset = {'model': ['RAV4', 'CRV', 'CAMRY', 'ACCORD', 'RDX', 'MDX',],
            'cylinders': [4, 4, 4, 4, 6, 6]}    

data_frame = pd.DataFrame(dataset)

print(data_frame.columns)
print(100*'-')

data_frame.columns = ['models', 'engine cylinders']
print(data_frame)
print(100*'-')

data_frame = data_frame.rename(columns={'engine cylinders':'cyl'})
print(data_frame)
print(100*'-')

#adding a column to the data frame. The number of rows in the data frame and list must match,
#or else there will be and exception
prices = [1, 2, 3, 4]
data_frame['prices'] = prices
'''

'''
#EXAMPLE 4
dataset = {'model': ['RAV4', 'CRV', 'CAMRY', 'ACCORD', 'RDX', 'MDX',],
            'cylinders': [4, 4, 4, 4, 6, 6]}    
prices = [40000.0, 42000.0, 30000.0, 32000.0, 52000.0, 70000.0]
data_frame = pd.DataFrame(dataset)

data_frame['prices'] = prices

print(data_frame)
print(100*'-')

#removes the column of cylinders from the dataframe entirely
data_frame = data_frame.drop(columns=['cylinders'])
print(data_frame)
'''

'''
#EXAMPLE 5: Concactenating data frames
dataset = {'model': ['RAV4', 'CRV', 'CAMRY', 'ACCORD', 'RDX', 'MDX',],
            'cylinders': [4, 4, 4, 4, 6, 6]}

df1 = pd.DataFrame
df2 = pd.DataFrame({'model': ['TLX'], 'prices': [35000.0]})

df = pd.concat([df1, df2], ignore_index = True)
print(df)

df = df.drop([0])
print(df)
'''

'''
#EXAMPLE 6: 
import pandas as pd

dataset_1 = {'model': ['RAV4', 'CRV', 'CAMRY', 'ACCORD', 'RDX', 'MDX'],
'cylinders': [4, 4, 4, 4, 6, 6]}

dataset_2 = {'ctype': ['RAV4', 'CRV', 'CAMRY', 'ACCORD', 'RDX', 'MDX'],
'prices': [40000.0, 42000.0, 35999.0, 39649.0, 60000.0,
70000.0]}

df1 = pd.DataFrame(dataset_1)
df2 = pd.DataFrame(dataset_2)

df = df1.merge(df2, left_on='model', right_on='ctype')

print(df)

'''