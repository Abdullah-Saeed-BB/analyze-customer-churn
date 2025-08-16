from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import joblib
from custom_function import feature_names_out, get_churn_drivers
import shap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

analyze_customer_bp = Blueprint('analyze_customer', __name__)

columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       'MonthlyCharges', 'TotalCharges']

@analyze_customer_bp.route("/")
def analyze_customer():
    return render_template('./analyze_customer.html')

@analyze_customer_bp.route("result")
def result():
    data = [request.args.get(col) for col in columns]
    data_df = pd.DataFrame([data], columns=columns)

    preprocessor = joblib.load("./models/preprocessor.joblib") 

    try:
        data_trans = preprocessor.transform(pd.concat([data_df, data_df], axis=0))[0]

        # Change the (No&Yes) to (0 & 1)
        data_trans = [0 if d == "No" else 1 if d == "Yes" else d for d in data_trans]
        
        explainer = joblib.load("./models/shap_explainer.joblib")

        shap_value = explainer(np.array([data_trans]))

        preproc_columns = preprocessor.get_feature_names_out()
        preproc_columns = list(map(lambda col: col.split("__")[-1], preproc_columns))

        isChurn = round(sum(shap_value[0].values)) == True

        plt.title("Some of features does not look right because these are processed data")

        shap.waterfall_plot(shap.Explanation(
            values=shap_value[0],
            base_values=explainer.expected_value,
            data=data_trans,
            feature_names=preproc_columns,
        ), show=False)

        waterfall_plot = create_plot_data()
        
        shap.bar_plot(shap_value[0].values, feature_names=preproc_columns, show=False)

        summary_plot = create_plot_data()

        recommends = get_churn_drivers(shap_value[0].values, preproc_columns, isChurn)
        recommend_title = "🚨 Retention Intervention Plan" if isChurn else "✅ Loyalty & Growth Opportunities"

        return render_template('./customer_result.html', data=dict(zip(columns, data)),
                                waterfall_plot=waterfall_plot, summary_plot=summary_plot,
                                recommend_title=recommend_title, recommends=recommends)
    except:
        return render_template("./error_page.html", title="Something Went Wrong",
                               description="An error occurred while analyzing the data. The URL might be missing or incorrect. Please try again with a valid URL.")        



@analyze_customer_bp.route('/', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':

        val = request.form.get
        data = dict(map(lambda col: (col, val(col) if val(col) != None else "No") , columns))

        return redirect(url_for(".result", **data))


def create_plot_data():
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", dpi=140)
    buf.seek(0)
    plt.close()

    plot_data = base64.b64encode(buf.getvalue()).decode('ascii')
    buf.close()
    return plot_data