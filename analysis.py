import duckdb
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, roc_auc_score
from visualizations import roc_curve_viz

# Run SQL queries with DuckDB
def run_sql_query(df, query):
    con = duckdb.connect()
    con.execute("CREATE TABLE heart_data AS SELECT * FROM df")
    result = con.execute(query).df()
    return result


# Perform Logistic Regression
def perform_regression_analysis(df, goal_variable):
    X = df.drop(goal_variable, axis=1)
    y = df[goal_variable]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Generate ROC Curve
    y_prob = model.predict_proba(X_test)[:, 1]  # Predicted probabilities for class 1
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    auc = roc_auc_score(y_test, y_prob)
    roc_curve_viz(fpr, tpr, auc)

    # Generate classification report
    report = classification_report(y_test, y_pred)
    return report