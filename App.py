#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 17:25:37 2023

@author: expert
"""

import streamlit as st
import pandas as pd

# Load data from a CSV file
df = pd.read_csv("/home/expert/Spyder/AgverseTech/Agverse_3rdWeekfullcode/Telemetry_api_code/Data_Cleaned_TimeDelay.csv")

# Add a title to the app
st.title("Data Summary Statistics")

# Display the total number of records
num_rows = len(df)
st.subheader("Total Number of Records")
st.write(f"There are {num_rows} records in this dataset.")

# Display the count of each Sensor ID
st.subheader("Count of Each Sensor ID")
sensor_counts = df['mac_id'].value_counts()
st.write(sensor_counts)

# Display summary statistics by Sensor ID
st.subheader("Summary Statistics by Sensor ID")
sensor_stats = df.groupby('mac_id')['Time Difference (s)'].agg(['mean', 'max', 'min'])
sensor_stats.rename(columns={'mean': 'Average Interval', 'max': 'Maximum Interval', 'min': 'Minimum Interval'}, inplace=True)
sensor_stats['Average Interval'] = sensor_stats['Average Interval'].round(2)
st.write(sensor_stats)
