import streamlit as st
import pandas as pd
import os

# Import profiling capability
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# ML stuff
from pycaret.classification import setup, compare_models, pull, save_model



# Sidebar layout for navigation and title
with st.sidebar:
    st.image("https://robots.net/wp-content/uploads/2023/11/how-to-build-a-machine-learning-app-1700045197.jpg")
    st.title("AutoStreamML")
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])
    st.info("This application allows you to build an automated ML pipeline using Streamlit, Pandas Profiling and PyCaret")

# Check if sourcedata.csv exists, load it if it does
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

# Upload section
if choice == "Upload":
    st.title("Upload your data for modelling!!")
    file = st.file_uploader("Upload your dataset here ")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)  # Save the uploaded file
        st.dataframe(df)  # Display the dataframe

# Profiling section
if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    if 'df' in locals():  # Check if df is defined
        profile_report = ProfileReport(df, explorative=True)  # Generate profiling report
        st_profile_report(profile_report)  # Display the report in Streamlit
    else:
        st.error("Please upload a dataset first!")

# Placeholder for ML section
if choice == "ML":
    st.title("Machine Learning")
    target = st.selectbox("Select your target",df.columns)
    if st.button("Train model"):
        setup(df, target=target, verbose=False)
        setup_df =pull()
        st.info("This is ML experiment settings")
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df= pull()
        st.info("This is ML Model")
        st.dataframe(compare_df)
        best_model
        save_model(best_model, 'best_model')

# Placeholder for Download section
if choice == "Download":
    with open("best_model.pkl", 'rb') as f:
        st.download_button("Download the Model", f,"trained_model.pkl")

