import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import perform_regression_analysis, run_sql_query
from visualizations import plot_age_distribution, plot_correlation_heatmap, plot_countplot, plot_boxplot

# Dashboard title
st.markdown("<h1 style='text-align: center;'>Heart Disease Analysis Dashboard</h1>", unsafe_allow_html=True)

# Initialize session state for navigation
if "section" not in st.session_state:
    st.session_state.section = "Introduction"

# Sidebar for Navigation
st.sidebar.title("Heart Disease Analysis")

# Use buttons or other widgets to update session state for navigation
if st.sidebar.button("Introduction"):
    st.session_state.section = "Introduction"

if st.sidebar.button("Dataset Overview"):
    st.session_state.section = "Dataset Overview"

if st.sidebar.button("Descriptive Analysis"):
    st.session_state.section = "Descriptive Analysis"

if st.sidebar.button("Correlation Analysis"):
    st.session_state.section = "Correlation Analysis"

if st.sidebar.button("Logistic Regression"):
    st.session_state.section = "Logistic Regression"

if st.sidebar.button("SQL Query Interface"):
    st.session_state.section = "SQL Query Interface"

# File Upload
file_path = "./data/processed.cleveland.data"
columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
           "thalach", "exang", "oldpeak", "slope", "ca", "thal", "disease_presence"]
df = pd.read_csv(file_path, names=columns, na_values=["?"])

# Process the data
## Goal variable >> presence of heart disease [binary]
df["disease_presence"] = df["disease_presence"].apply(lambda x: 1 if x > 0 else 0)
initial_rows = df.shape[0]
# Cleaning: Handling missing data
df = df.dropna()
final_rows = df.shape[0]
removed_records = initial_rows - final_rows

# Render Main Content
if st.session_state.section == "Introduction":
    with open("README.md", "r") as file:
        readme_content = file.read()
    st.markdown(readme_content)

if st.session_state.section == "Dataset Overview":
    st.subheader("**Dataset Overview**")
    st.write("**Dataset Name:** processed.cleveland.data (source: https://archive.ics.uci.edu/dataset/45/heart+disease)")

    # Metrics for quick overview
    col1, col2 = st.columns(2)
    col1.metric("Total Records", df.shape[0])
    col2.metric("Heart Disease Cases", df[df["disease_presence"] == 1].shape[0])

    st.write(df.head())
    st.write(f"Shape of the dataset: {df.shape}")
    st.write(f"Number of records removed due to missing values (cleaning phase): {removed_records}")

    st.subheader("**Summary Statistics**")
    st.write(df.describe())

elif st.session_state.section == "Descriptive Analysis":
    # Some quick metrics
    col1, col2 = st.columns(2)
    # Average Age
    col1.metric("Average Age", round(df["age"].mean(), 1))
    # Percentage of Females
    num_females = df[df["sex"] == 0].shape[0]
    percent_females = (num_females / df.shape[0]) * 100
    col2.metric("Percentage of Females", f"{percent_females:.1f}%")

    st.subheader("**Age Distribution by Sex**")
    plot_age_distribution(df)

elif st.session_state.section == "Correlation Analysis":
    tab1, tab2, tab3 = st.tabs(["Correlation Heatmap", "Chest Pain Analysis", "Thalassemia Analysis"])

    with tab1:
        st.subheader("**Correlation Heatmap**")
        plot_correlation_heatmap(df)

    with tab2:
        st.subheader("**Chest Pain Types (cp) by Disease Presence**")
        plot_countplot(df, "cp", "disease_presence", x_label="Chest Pain Types (cp)")

        '''Chest Pain Type (cp):
        1: Typical angina;
        2: Atypical angina;
        3: Non-anginal pain;
        4: Asymptomatic'''

        st.info(
            "**Analysis #1 from the Correlation Heatmap:** A moderate positive correlation (**~0.41**) suggests that certain chest pain types ('cp) are associated with heart disease ('disease_presence').")

    with tab3:
        st.subheader("**Distribution of Thalassemia ('thal') by Disease Presence**")
        plot_boxplot(df, var_x="disease_presence", var_y="thal", x_label="Disease Presence (0 = No, 1 = Yes)",
                     y_label="Thalassemia (thal)")
        st.info(
            "**Analysis #2 from the Correlation Heatmap:** A positive correlation (**~0.53**) indicates that higher 'thal' values (thalassemia condition) are associated with a greater likelihood of heart disease ('disease_presence').")

elif st.session_state.section == "Logistic Regression":
    st.subheader("**Logistic Regression Analysis**")
    report = perform_regression_analysis(df, "disease_presence")

    st.write("**Classification Report:**")
    st.text(report)

    st.info("Model Strengths: The model is performing well, with an overall accuracy of 88%.")

elif st.session_state.section == "SQL Query Interface":
    st.subheader("You can manipulate the dataset by your own!")
    query = st.text_area("Write your SQL query below (e.g., SELECT * FROM heart_data LIMIT 5):",
                         "SELECT sex, mean(age) as media_idades FROM heart_data group by sex;")
    query_results = run_sql_query(df, query)  # Call SQL function
    st.write("Query Results:")
    st.write(query_results)