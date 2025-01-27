import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Age Distribution
def plot_age_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x="age", kde=True, bins=20, hue="sex", palette="Set2", multiple="stack")
    plt.title("Age Distribution (By Sex)")
    plt.xlabel("Age")
    plt.ylabel("#Cases")
    st.pyplot(plt)

# Correlation Heatmap
def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    st.pyplot(plt)

# Countplot
def plot_countplot(df, var1, var2, x_label):
    plt.figure(figsize=(8, 6))
    sns.countplot(x=var1, hue=var2, data=df)
    plt.xlabel(x_label)
    plt.ylabel("Count")
    plt.legend(title="Disease Presence", loc="upper right", labels=["No Disease", "Disease"])
    st.pyplot(plt)

# Boxplot for thal vs. disease presence
def plot_boxplot(df, var_x, var_y, x_label, y_label):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=var_x, y=var_y, data=df)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    st.pyplot(plt)

# ROC Curve for Regression Analysis
def roc_curve_viz(fpr, tpr, auc):
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {auc:.2f})")
    plt.plot([0, 1], [0, 1], "k--", label="Random Classifier")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    st.pyplot(plt)