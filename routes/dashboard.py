from flask import Blueprint, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import base64
from io import BytesIO
import joblib 
import shap

import inspect

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

    churn_rates = []

    if request.method == "POST":
        # Filter by the Contract
        if "tenure__more_avg" in request.form:
            churn_rates_option = "Tenure more than average"
            churn_rates = [
                chunk["Churn"].value_counts(True)["Yes"] * 100
                for chunk in split_dataframe(data[data["tenure"] >= data["tenure"].mean()])
            ]
        elif "tenure__less_avg" in request.form:
            churn_rates_option = "Tenure less than average"
            churn_rates = [
                chunk["Churn"].value_counts(True)["Yes"] * 100
                for chunk in split_dataframe(data[data["tenure"] < data["tenure"].mean()])
            ]
        for contract_type in ["Month-to-month", "One year", "Two year"]:
            if f"Contract__{contract_type}" in request.form:
                churn_rates_option = f"{contract_type} contract"
                churn_rates = [
                    chunk["Churn"].value_counts(True)["Yes"] * 100
                    for chunk in split_dataframe(data[data["Contract"] == contract_type])
                ]
                break
    if not churn_rates:
        churn_rates_option = f"All"
        churn_rates = [chunk["Churn"].value_counts(True)["Yes"] * 100 for chunk in split_dataframe(data)]

    churn_rates = list(map(float, churn_rates))

    # Create Beeswarm plot

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
                           churn_rates_option=churn_rates_option, bar_plot=img_base64)