import streamlit as st

st.title("📊 Financial Data Dashboard")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    import pandas as pd
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df.head(20))

    st.subheader("Data Description")
    st.json(df.describe().to_dict())

    st.subheader("Visualizations")
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np

    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        st.pyplot(fig)
