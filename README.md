# Analyze Customer Churn (CChurn)
By entering customer information the machine learning model will predict customer churn, providing the reasons, and write solutions for keeping the customer or gain the customer.<br/>
I used a **Flask** to build the web application, **Scikit-learn** to create model, and **SHAP (SHapley Additive exPlanations)** to interpret the model.

The process of creating the model you can find in this [Kaggle notebook](https://www.kaggle.com/code/abdullahsaeedwebdev/telco-customer-churn-ml-shap-80-8-acc)

#### [Live demo](https://analyze-customer-churn.onrender.com/)
## Project Structure
 - `main.py` The main file to run the project.
 - `custom_function.py`. Contain main functions, to avoid write everything in single file.  
 - `customer_churn.csv` [Telco customer dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).
 - `models/preprocessor.joblib` Is a *sklearn.compose.ColumnTransformer* object to process data.
 - `models/shap_explainer.joblib` Is a *shap.KernelExplainer* object to read the data and interpret it.
 - `routes/analyze_customer.py` Contain the codes of analyzing customer churn process.
 - `routes/dashboard.py` Contain the codes of the dashboard, for loading the data and creating the plots.
 - `templates/base.html` Is a *jinja2* template to put the header and footer in main pages.
 - `templates/analyze_customer.html` Is a form page to enter the customer information.
 - `templates/customer_result.html` After enter customer information, shows the result of analyzing the customer.
 - `templates/dashboard.html` This is the home page, contain the main information about the data, and plots to get insights about the data
 - `templates/error_page.html` When error occurs in the backend the user redirected to this page.
 - `templates/not_found.html` When the page that user looking for not exist, the user redircetd to this page.

## Installation
Clone the project:<br/>
`git clone https://github.com/Abdullah-Saeed-BB/analyze-customer-churn.git`

Run the `main.py`, and navigate to `localhost:5000` that shows in the log, and that's it :)

## Screenshots
