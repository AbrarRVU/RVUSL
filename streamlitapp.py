# Import necessary libraries
import streamlit as st
import seaborn as sb
import plotly.express as px
import pandas as pd

# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")
# --- Load Dataset ---
dataset = sb.load_dataset('tips')  # Load the 'tips' dataset from seaborn

# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(dataset.head())

# --- Task 1: Interactive Bar Chart ---
st.subheader("Task 1: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
bar_chart_fig = px.bar(
    dataset, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(bar_chart_fig)  # Display the bar chart

# --- Task 2: Interactive Scatter Plot ---
st.subheader("Task 2: Scatter Plot - Total Bill vs. Tip (Color-coded by Gender)")
# Scatter Plot: Total Bill vs. Tip (Color-coded by Gender)
scatter_plot_fig = px.scatter(
    dataset, x='total_bill', y='tip', color='sex',
    title='Total Bill vs. Tip (Colored by Gender)',
    labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'},
    template='plotly_dark',  # Cool dark theme
    size='size'  # Size of points based on the size of the group
)
st.plotly_chart(scatter_plot_fig)  # Display the scatter plot
