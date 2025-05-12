import streamlit as st
import pandas as pd

st.title("📊 CSV File Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Read the uploaded CSV
        df = pd.read_csv(uploaded_file)
        
        st.success("File successfully loaded!")
        st.write(f"🔢 Rows: {df.shape[0]}, Columns: {df.shape[1]}")

        # Show preview
        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

        # Show column names
        if st.checkbox("Show column names"):
            st.write(df.columns.tolist())
