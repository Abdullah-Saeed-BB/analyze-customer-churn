from flask import Blueprint, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import base64
from io import BytesIO
import joblib 
import shap

# Create a Blueprint named 'main'
dashboard_bp = Blueprint('dashboard', __name__)

data = pd.read_csv("./customer_churn.csv")

def split_dataframe(data, n_chunks=6):
    n_chunks = 6
    chunk_size = len(data) // n_chunks

    chunks = [data.iloc[i * chunk_size : (i + 1) * chunk_size] for i in range(n_chunks)]
    return chunks    

@dashboard_bp.route("/", methods=["GET", "POST"])
def dashboard():
    churn_rate = data["Churn"].value_counts(True)["Yes"] * 100

    total_customers = data.shape[0]

    churn_filters = [
        ("all", [True] * data.shape[0]),
        ("month-to-month contract", data["Contract"] == "Month-to-month"),
        ("one year contract", data["Contract"] == "One year"),
        ("two year contract", data["Contract"] == "Two year"),
        ("tenure more than avg", data["tenure"] >= data["tenure"].mean()),
        ("tenure less than avg", data["tenure"] < data["tenure"].mean()),
    ]    
    churn_rates = [
        [title, [float(chunk["Churn"].value_counts(True)["Yes"] * 100) for chunk in split_dataframe(data[condition])]]
        for title, condition in churn_filters 
    ]
    
    img_base64 = None
    if request.method == "POST":
        # # Create Bar plot
        explainer = joblib.load("./models/shap_explainer.joblib")
        preprocessor = joblib.load("./models/preprocessor.joblib")

        data_trans = preprocessor.transform(data)
        data_trans[:, -1] = np.uint(data_trans[:, -1] == "Yes")

        data10 = shap.utils.sample(data_trans, 10, 42)

        shap_values = explainer(data10)

        feature_names = preprocessor.get_feature_names_out()
        feature_names = list(map(lambda col: col.split("__")[-1], feature_names))

        plt.figure(figsize=(10, 6))

        shap.plots.bar(shap_values, show=False)
        ax = plt.gca()
        new_labels = [label.get_text().split("__")[-1].replace("_", " = ") for label in ax.get_yticklabels()]
        ax.set_yticklabels(new_labels)

        plt.tight_layout()
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
        plt.close()
    
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render_template("dashboard.html", churn_rate=churn_rate,
                           total_customers=total_customers, churn_rates=churn_rates,
                           bar_plot=img_base64)