import pandas as pd
import numpy as np

#reading and converting csv file into pandas dataframe.
df2 = pd.read_csv("AEP_hourly.csv")

print(df)

#Changing Datetime from str to datetime.
df2["Datetime"] = pd.to_datetime(df2["Datetime"])
df = df2[df2.Datetime.dt.strftime('%H:%M:%S').between('01:00:00','01:00:00')]

#First ten rows of dataframe
print(df.head(10))

#Information about dataframe
df.info()

#Other information about dataframe like its mean, median and other paremeters.
print(df.describe())

#Separating date, time, month etc. from datetime col. of dataframe and creating new columns for storing them.
df["Date"] = pd.to_datetime(df["Datetime"]).dt.date
df["Month"] = pd.to_datetime(df["Datetime"]).dt.month
df["Year"] = pd.to_datetime(df["Datetime"]).dt.year
df["Day"] = pd.to_datetime(df["Datetime"]).dt.day_name()

#Arranging columns
df.insert(1,"Units",df["AEP_MW"])
df = df.drop(["AEP_MW","Datetime"], axis = 1)

#Last 10 rows of new dataframe.
print(df.tail(10))

print("Total number of years in data :- ")
print(np.unique(df["Year"]))

df.reset_index(inplace = True)
df = df.drop(["index"], axis = 1)
print(df)
new = df.to_csv('Energy1.csv', index = True)
