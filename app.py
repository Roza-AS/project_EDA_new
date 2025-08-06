# Run the app using: "poetry run streamlit run app.py"

import streamlit as st
import pandas as pd
from main import run_basic_eda

st.title("Auto EDA Tool")

uploaded_file = st.file_uploader("Upload your dataset in CSV format please", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("## Dataset Preview")
    st.dataframe(df.head())

    st.write("## EDA Results")
    run_basic_eda(df)
else:
    st.info("Please upload a CSV file to begin.")
