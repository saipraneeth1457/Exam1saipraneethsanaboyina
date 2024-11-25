import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Page Configuration
st.set_page_config(page_title="Car Price Analysis", layout="wide")

# Title
st.title("Car Price Analysis")

# Sidebar
st.sidebar.header("Navigation")
sections = ["Introduction", "Load Data", "Visualize Patterns", "Descriptive Statistics", "Correlation & Causation"]
selected_section = st.sidebar.radio("Select Section", sections)

# Load Data
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/saipraneeth1457/Exam1saipraneethsanaboyina/refs/heads/main/Exam1_clean_df.csv'
    return pd.read_csv(url)

if selected_section == "Introduction":
    st.write("""
    This app explores factors affecting car prices using data visualization, grouping, and correlation techniques.
    """)

if selected_section == "Load Data":
    df = load_data()
    st.write("### Dataset")
    st.dataframe(df.head())
    st.write("### Data Types")
    st.write(df.dtypes)

if selected_section == "Visualize Patterns":
    df = load_data()
    st.write("### Visualizing Relationships")
    st.write("Scatterplot: Engine Size vs. Price")
    fig, ax = plt.subplots()
    sns.regplot(x="engine-size", y="price", data=df, ax=ax)
    st.pyplot(fig)

    st.write("Scatterplot: Highway-MPG vs. Price")
    fig, ax = plt.subplots()
    sns.regplot(x="highway-mpg", y="price", data=df, ax=ax)
    st.pyplot(fig)

    st.write("Boxplot: Drive-Wheels vs. Price")
    fig, ax = plt.subplots()
    sns.boxplot(x="drive-wheels", y="price", data=df, ax=ax)
    st.pyplot(fig)

if selected_section == "Descriptive Statistics":
    df = load_data()
    st.write("### Descriptive Statistics")
    st.write(df.describe())
    st.write("Value Counts: Drive-Wheels")
    st.write(df['drive-wheels'].value_counts())

if selected_section == "Correlation & Causation":
    df = load_data()
    st.write("### Correlation and Causation")
    st.write("Pearson Correlation: Horsepower and Price")
    pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
    st.write(f"Pearson Coefficient: {pearson_coef:.2f}, P-Value: {p_value:.2e}")

    st.write("Pearson Correlation: Length and Price")
    pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
    st.write(f"Pearson Coefficient: {pearson_coef:.2f}, P-Value: {p_value:.2e}")

    st.write("Pearson Correlation: Width and Price")
    pearson_coef, p_value = stats.pearsonr(df['width'], df['price'])
    st.write(f"Pearson Coefficient: {pearson_coef:.2f}, P-Value: {p_value:.2e}")
