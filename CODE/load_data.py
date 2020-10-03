import pandas as pd
import numpy as np
import matplotlib

nba = pd.read_csv("../DATABASE/nba_all_elo.csv")

# check the database
# type(nba)
# print(nba)
print ( "length:" + str(len(nba)) )
print ( "shape: " + str(nba.shape) )

# Looks at the first 5 row
# print ( "head 5 rows: \n " + str(nba.head) )

# Display all columns
pd.set_option("display.max.columns", None)

# Only show 2 decimal placse
pd.set_option("display.precision", 2)

# print ( "tail 5 rows: \n " + str(nba.tail) )

# Returns the info about your database, the columns and their datatypes
DATABSE_INFO = nba.info()                        

# Shows baseic descriptive statistic for all numerical data (no strings)
DESCRIBE_DATABASE_NUMERIC = nba.describe()

# Returns the info about your database, the columns and their datatype for object datatype or strings
DESCRIBE_DATASET_OBJECTS = nba.describe(include=np.object)

# Shows how often a vlaue is occured in a column
TEAM_ID_VALUE_COUNT = nba["team_id"].value_counts()

# Other possible panda functions: min() , max() , sum()

######### Building a data frame from some panda sequences #########

CITY_EMPLOYEE_COUNT = pd.Series({'Amesterdam': 5, 'Tokyo': 8})
CITY_REVENUES = pd.Series(
    [4200,8000, 6500],
    index = ['Amesterdam', 'Toronto', 'Tokyo']
)

CITY_DATA = pd.DataFrame({
    "revenue": CITY_REVENUES,
    "employee_count": CITY_EMPLOYEE_COUNT
})

######### DATA CLEANING #########

# Alters the dataframe
GAMES_WITH_NOTE = nba[nba["notes"].notnull()]

# Drops the rows with a missing data in them
ROWS_WITHOUT_MISSING_DATA = nba.dropna()


######### DATA VISUALIZING #########

# line plot
nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot()

# bar plot
nba["fran_id"].value_counts().head(10).plot(kind="bar")

print(nba.shape)
print(GAMES_WITH_NOTE.shape)