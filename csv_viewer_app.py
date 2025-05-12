import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📂 Upload and Process a File")

# Upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read the file into a DataFrame
    df = pd.read_csv(uploaded_file)

    st.subheader("✅ Raw Data Preview")
    st.write(df.head())

    # Example processing: drop missing values
    cleaned_df = df.dropna()  

    st.subheader("🧹 Cleaned Data (No Missing Values)")
    st.write(cleaned_df.head())
    
    #fill with 0 for null values
    df_filled = df.fillna(0)
    st.subheader("Filled with 0  null values")
    st.write(df_filled.head())

    st.subheader("example of shape function")
    st.write(f"🔢 Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    #df.plot() returns a Matplotlib object — use st.pyplot(fig) to render it.
    #You must import matplotlib.pyplot as plt.
    #This approach gives you more customization than st.bar_chart().
    
    st.subheader("example of bar graph") 
    if "Product Name" in cleaned_df.columns and "Total Price" in cleaned_df.columns:
       st.subheader("📈 Total Price by Product (Pandas Plot)")

       # Prepare data
       grouped = cleaned_df.groupby("Product Name")["Total Price"].sum().sort_values()

       # Plot
       fig, ax = plt.subplots(figsize=(10, 6))  # Moved figsize here
       grouped.plot(kind="barh", ax=ax, color='skyblue')
       ax.set_xlabel("Total Price")
       ax.set_ylabel("Product Name")
       ax.set_title("Total Sales by Product")

       st.pyplot(fig)
    
    # Example analysis: summary stats
    st.subheader("📊 Summary Statistics")
    st.write(cleaned_df.describe())

else:
    st.info("Please upload a CSV file to continue.")
