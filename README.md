# Analyze Customer Churn (CChurn)
By entering customer information the machine learning model will predict customer churn, providing the reasons, and write solutions for keeping the customer or gain the customer.<br/>
I used a **Flask** to build the web application, **Scikit-learn** to create model, and **SHAP (SHapley Additive exPlanations)** to interpret the model.

The process of creating the model you can find in this [Kaggle notebook](https://www.kaggle.com/code/abdullahsaeedwebdev/telco-customer-churn-ml-shap-80-8-acc)

### [Live demo](https://analyze-customer-churn.onrender.com/)
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

Run the `main.py`, and navigate to `localhost:5000`, and that's it :)

## Screenshots
<img width="1920" height="1025" alt="‏‏لقطة الشاشة (5)" src="https://github.com/user-attachments/assets/930b5a11-7050-4278-9b07-e831529fddd4" />
<img width="1920" height="1029" alt="‏‏لقطة الشاشة (8)" src="https://github.com/user-attachments/assets/d97da45c-2b60-47ab-8ce3-e7ad72cbf749" />
<img width="1920" height="1026" alt="‏‏لقطة الشاشة (6)" src="https://github.com/user-attachments/assets/7d7c4e38-dca3-4239-848b-31648411b55b" />
<img src="https://github.com/user-attachments/assets/5e9b9150-3f77-4b40-ab1d-ce5e5c5fd055" alt="Demo" width="1920"/>
