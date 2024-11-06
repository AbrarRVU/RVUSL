#Edit the 8th to 12th line code before upload to gihub
# Import necessary libraries
import streamlit as st
import seaborn as sb
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")


# --- Input for Author Information ---
st.sidebar.header("Visualization skill workshop - Plotly")
name = st.sidebar.text_input("Shaikh Abrar Ahmed")
usn = st.sidebar.text_input("Section F - B.Tech")
instructor_name = st.sidebar.text_input("Prof. Ashwini Kumar Mathur, SoCSE")

# --- Load Dataset ---
dataset = sb.load_dataset('tips')  # Loading the tips dataset


# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())


# --- Task 1: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2)  # Display the chart in Streamlit

# --- Task 2: Scatter Plot ---
st.subheader("Task 2: Scatter Plot - Total Bill vs. TIp (Color coded by gender)")
# Scatter Plot: Total Bill vs. Tip (Color-coded by Gender)
plot01 = px.scatter(
    dataset, x='total_bill', y='tip', color='sex',
    title='Total bill V/S Tip (Colored by gender)',
    labels={'total_bill': 'Total bill ($)', 'tip': 'Tip ($)'},
    template='plotly_dark', #Cool dark theme
    size='size' #The size of points based on the size of the group
)
st.plotly_chart(plot01)
