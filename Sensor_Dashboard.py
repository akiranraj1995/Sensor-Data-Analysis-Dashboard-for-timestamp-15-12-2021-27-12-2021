#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:20:03 2023

@author: expert
"""
#Dashboard_Webapp.py
#============================
#IMPORTING LIBRARIES

import streamlit as st
import pandas as pd

# Load your data into a Pandas DataFrame
df=pd.read_csv("/home/expert/Spyder/AgverseTech/Agverse_3rdWeekfullcode/Telemetry_api_code/Data_Cleaned_TimeDelay.csv")

# Create the Streamlit app
st.title("Sensor Data Analysis Dashboard for timestamp 15-12-2021/27-12-2021")
num_rows = len(df)

#1.TOTAL NO. OF RECORDS
st.subheader("1.  Total Number of Records" )
st.write(f"Total  Records : **{num_rows}**")

#==============================================================================

#2.TOTAL COUNT OF EACH SENSOR IDs
# Get the counts of unique items in a column
counts = df['mac_id'].value_counts() 

st.subheader("2. Count of each Sensor IDs")

# Create a new DataFrame with the unique items and their counts
unique_items = pd.DataFrame({'mac_id': counts.index, 'Counts': counts.values})

# Reset the index of the dataframe to add an index column
unique_items = unique_items.reset_index().rename(columns={'index': 'Index'})

# Display the result as a table in Streamlit
st.write(unique_items) 

#===============================================================================

#3. Display summary statistics
st.subheader("3. Summary Statistics by Sensor ID")

grouped_data = df.groupby(["mac_id"])["Time Difference (s)"].agg(["mean", "max", "min"])
#Renaming the Columns header
grouped_data = grouped_data.rename(columns={"mean": "Average Interval", "max": "Maximum Interval", "min": "Minimum Interval"})

#Rounding Off the decimal points
grouped_data["Average Interval"] = grouped_data["Average Interval"].round(2).apply(lambda x: '{:.2f}'.format(x))

#Rename the index/header of the grouped_data dataframe
grouped_data = grouped_data.rename_axis("mac_id").reset_index()

# Reset the index of the dataframe to add an index column
grouped_data = grouped_data.reset_index().rename(columns={'index': 'Index'})

st.write(grouped_data)


#==================================================================================






