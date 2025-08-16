# Analyze Customer Churn
By entering customer information the machine learning model will predict customer churn, providing the reasons, and write solutions to keep the customer or gain the customer.

### Project Structure


✨ Features
Churn Prediction: Predicts whether a customer will churn or not.

SHAP Explanations: Visualizes the impact of each feature on the model's prediction, providing transparency and trust in the model's decisions.

Web Interface: A simple and intuitive web interface built with Flask.

RESTful API: An API endpoint to get predictions programmatically.

📊 Dataset
This project uses the Telco Customer Churn dataset, which is publicly available on Kaggle. The dataset contains information about a fictional telecommunications company's customers, including:

Demographic Information: Gender, age range, and whether they have partners and dependents.

Account Information: How long they've been a customer, their contract type, payment method, and billing preferences.

Services: The services they have subscribed to, such as phone, internet, online security, and streaming TV.

Churn: Whether the customer churned within the last month.

🛠️ Installation
To get a local copy up and running, follow these simple steps.

Prerequisites
Python 3.8+

pip

Steps
Clone the repository:

git clone https://github.com/your_username/your_project_name.git
cd your_project_name

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

pip install -r requirements.txt

🏃‍♀️ Usage
Run the Flask application:

python app.py

Open your web browser and navigate to http://127.0.0.1:5000/.

Use the web interface to input customer data and get a churn prediction and SHAP explanation.

API Endpoint
You can also get predictions by sending a POST request to the /predict endpoint with a JSON payload containing the customer's information.

Example using curl:

curl -X POST \
  http://127.0.0.1:5000/predict \
  -H 'Content-Type: application/json' \
  -d '{
        "tenure": 10,
        "MonthlyCharges": 50.5,
        "TotalCharges": 500.5,
        "Contract": "Month-to-month",
        "OnlineSecurity": "No",
        "TechSupport": "No",
        "InternetService": "DSL"
      }'

💻 Technologies Used
Flask: A lightweight web framework for Python.

Scikit-learn: For building the machine learning model.

SHAP: For explaining the machine learning model's predictions.

Pandas: For data manipulation and analysis.

NumPy: For numerical operations.

HTML/CSS/JavaScript: For the front-end interface.
