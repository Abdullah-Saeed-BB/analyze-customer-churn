# Analyze Customer Churn
By entering customer information the machine learning model will predict customer churn, providing the reasons, and write solutions to keep the customer or gain the customer.

### Project Structure
 - `main.py` The main file to run the project.
 - `custom_function.py`.
 - `customer_churn.csv` Telco customer dataset. [Kaggle page](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).
 - `models/preprocessor.joblib` Is a *sklearn.compose.ColumnTransformer* object to process data.
 - `models/shap_explainer.joblib` Is a *shap.KernelExplainer* object to read the data and interpret the data.
 - `routes/analyze_customer.py` Contain the codes of analyzing customer churn process.
 - `routes/dashboard.py` Contain the codes of the dashboard, for loading the data and creating the plots.
 - `templates/base.html` Is a *jinja2* template to put the header and footer in main pages.
 - `templates/analyze_customer.html` Is a form page to enter the customer information.
 - `templates/customer_result.html` 
 - `templates/dashboard.html` This a home page, contain the main information about the data, and plots to get insights about the data
 - `templates/error_page.html` When error occurs in the backend the user redirected to this page.
 - `templates/not_found.html` When the page that user looking for not exist, the user redircetd to this page.
