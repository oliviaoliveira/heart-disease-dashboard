## Heart Disease Analysis Dashboard

Author: Olívia Oliveira (email: oliviarfoliveira@gmail.com; github: oliviaoliveira)

### Overview
This project analyzes heart disease data using Python and DuckDB. It includes:
- Data preprocessing and cleaning.
- Exploratory Data Analysis (EDA) with visualizations.
- Logistic regression for predicting heart disease presence.
- An interactive dashboard built with Streamlit.

### Dataset
The Cleveland Heart Disease dataset is a well-known resource in the medical and machine learning communities, primarily used for the classification of heart disease presence. 

#### Key Attributes

| Variable Name | Role    | Type        | Demographic | Description                                           | Units | Missing Values |
|---------------|---------|-------------|-------------|-------------------------------------------------------|-------|----------------|
| age           | Feature | Integer     | Age         |                                                       | years | no             |
| sex           | Feature | Categorical | Sex         |                                                       |       | no             |
| cp            | Feature | Categorical |             |                                                       |       | no             |
| trestbps      | Feature | Integer     |             | resting blood pressure (on admission to the hospital) | mmHg  | no             |
| chol          | Feature | Integer     |             | serum cholestoral                                     | mg/dl | no             |
| fbs           | Feature | Categorical |             | fasting blood sugar > 120 mg/dl                       |       | no             |
| restecg       | Feature | Categorical |             |                                                       |       | no             |
| thalach       | Feature | Integer     |             | maximum heart rate achieved                           |       | no             |
| exang         | Feature | Categorical |             | exercise induced angina                               |       | no             |
| oldpeak       | Feature | Integer     |             | ST depression induced by exercise relative to rest    |       | no             |
| slope         | Feature | Categorical |             |                                                       |       | no             |
| ca            | Feature | Integer     |             | number of major vessels (0-3) colored by flourosopy   |       | yes            |
| thal          | Feature | Categorical |             |                                                       |       | yes            |
| num           | Target  | Integer     |             | diagnosis of heart disease                            |       | no             |



#### Dataset Composition
Total Instances: 303 patients </br>
Attribute Count: 14, as detailed above </br>
Missing Values: certain attributes contain missing data

For a comprehensive understanding and additional context, you can refer to the UCI Machine Learning Repository's page on the Heart Disease dataset ( https://archive.ics.uci.edu/dataset/45/heart+disease ). 

### Installation
1. Github repo: link
2. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project
   pip install -r requirements.txt
   streamlit run app.py

### Bibliography
Janosi A, Steinbrunn W, Pfisterer M, Detrano R. Heart Disease [dataset]. 1989. UCI Machine Learning Repository. Available from: https://doi.org/10.24432/C52P4X.