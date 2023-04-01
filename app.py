import streamlit as st
import pandas as pd

# Load data from a CSV file
df = pd.read_csv("/home/expert/Spyder/AgverseTech/Agverse_3rdWeekfullcode/Telemetry_api_code/Data_Cleaned_TimeDelay.csv")

# Add a title to the app
st.title("Sensor-Data-Analysis-Dashboard-for-timestamp-15-12-2021-27-12-2021")

# Display the total number of records
num_rows = len(df)
st.subheader(" 1. Total Number of Records")
st.write(f"There are {num_rows} records in this dataset.")

# Display the count of each Sensor ID
st.subheader("2. Count of Each Sensor ID")
sensor_counts = df['mac_id'].value_counts().reset_index()
sensor_counts.rename(columns={'index': 'Sensor ID', 'mac_id': 'Value Counts'}, inplace=True)
st.write(sensor_counts)

# Display summary statistics by Sensor ID
st.subheader("3. Summary Statistics by Sensor ID")
sensor_stats = df.groupby('mac_id')['Time Difference (s)'].agg(['mean', 'max', 'min']).reset_index()
sensor_stats.rename(columns={'mac_id': 'Sensor ID', 'mean': 'Average Interval', 'max': 'Maximum Interval', 'min': 'Minimum Interval'}, inplace=True)
sensor_stats['Average Interval'] = sensor_stats['Average Interval'].round(2)
st.write(sensor_stats)
