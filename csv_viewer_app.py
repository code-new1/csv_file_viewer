import streamlit as st
import pandas as pd

st.title("📂 Upload and Process a File")

# Upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read the file into a DataFrame
    df = pd.read_csv(uploaded_file)

    st.subheader("✅ Raw Data Preview")
    st.write(df.head())

    # Example processing: drop missing values
    #cleaned_df = df.dropna()
    #fill with 0
    df_filled = df.fillna(0)

    st.subheader("🧹 Cleaned Data (No Missing Values)")
    st.write(cleaned_df.head())

    # Example analysis: summary stats
    st.subheader("📊 Summary Statistics")
    st.write(cleaned_df.describe())

else:
    st.info("Please upload a CSV file to continue.")
