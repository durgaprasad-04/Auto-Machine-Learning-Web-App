# Auto Machine Learning Web App

**Auto Machine Learning Web App** is an automated machine learning web application built using Python, Pandas Profiling, PyCaret, and Streamlit. This tool allows users to upload their datasets, perform exploratory data analysis (EDA), build machine learning models, and download the results — all within a user-friendly interface. It's a powerful yet simple solution for data enthusiasts, analysts, and developers to quickly prototype and evaluate machine learning pipelines.

**Features**
**Data Upload**: Upload your dataset (CSV format) for analysis and model building.
**Exploratory Data Analysis_ (EDA)**: Automatically generate comprehensive EDA reports using Pandas Profiling.
**AutoML**: Build machine learning models using PyCaret, including model comparison, selection, and tuning.
**Streamlit UI**: Interact with the app through a clean and simple web interface powered by Streamlit.
**Model Download**: Export the trained machine learning model for future use.

**Tech Stack**
**_Python_**: The primary programming language for the app.
**_Pandas Profiling_**: Used to generate EDA reports with one click.
**PyCaret**: Provides the machine learning framework for automated model comparison, tuning, and evaluation.
**Streamlit**: Enables the app's web interface, making it easy to run and interact with the app locally or online.

**Installation**

**_Clone the repository_**:
git clone 
cd Auto Machine learning Web App
**_Install the required dependencies_**:
pip install -r requirements.txt
**_Run the app locally_**:
streamlit run app.py

**Usage**
**Upload**: Upload your dataset by clicking the "Upload" option in the sidebar. Once the dataset is uploaded, you can view it in the main window.

**Profiling**: Generate an exploratory data analysis report by selecting the "Profiling" option. The app will create an in-depth analysis of your data, including missing values, correlations, and summary statistics.

**ML (AutoML)**: Under the "ML" section, you can choose your target variable and let PyCaret handle the rest. It will automatically compare models and suggest the best-performing one.

**Download**: Once the model is trained, you can download the best model and use it in your projects.
 
