import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit app title
st.title("Video Game Sales Data Explorer")

# Sidebar for user inputs and settings
st.sidebar.header("Settings")
st.sidebar.write("Customize your analysis.")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload a dataset (CSV format)", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    st.write("## Dataset Preview")
    st.dataframe(df)

    # Data insights
    st.write("### Dataset Information")
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")
    st.write("### Columns")
    st.write(df.columns.tolist())

    # Display descriptive statistics
    st.write("### Descriptive Statistics")
    st.write(df.describe())

    # Interactive filtering
    st.write("### Filter by Platform or Genre")
    platforms = st.multiselect("Select Platform(s)", df["Platform"].unique())
    genres = st.multiselect("Select Genre(s)", df["Genre"].unique())

    filtered_df = df[
        (df["Platform"].isin(platforms) if platforms else True) &
        (df["Genre"].isin(genres) if genres else True)
    ]

    st.write("### Filtered Dataset")
    st.dataframe(filtered_df)

    # Visualizations
    st.write("### Visualizations")

    # Top-selling games
    st.write("#### Top 10 Games by Global Sales")
    top_sales = df.nlargest(10, "Global_Sales")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top_sales, x="Global_Sales", y="Name", ax=ax)
    ax.set_title("Top 10 Games by Global Sales")
    st.pyplot(fig)

    # Platform distribution
    st.write("#### Sales Distribution by Platform")
    platform_sales = df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    platform_sales.plot(kind="bar", ax=ax)
    ax.set_title("Total Global Sales by Platform")
    st.pyplot(fig)

    # Genre distribution
    st.write("#### Sales Distribution by Genre")
    genre_sales = df.groupby("Genre")["Global_Sales"].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    genre_sales.plot(kind="pie", autopct='%1.1f%%', ax=ax, ylabel="")
    ax.set_title("Global Sales Distribution by Genre")
    st.pyplot(fig)

    # Insights summary
    st.write("### Insights Summary")
    st.write("Here are some key insights:")
    st.write(f"- Total games in dataset: {df.shape[0]}")
    st.write(f"- Most popular platform: {platform_sales.idxmax()} with {platform_sales.max()} global sales.")
    st.write(f"- Most popular genre: {genre_sales.idxmax()} with {genre_sales.max()} global sales.")
else:
    st.write("### Please upload a dataset to begin analysis.")
