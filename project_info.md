[More information about the data in IBM](https://community.ibm.com/community/user/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)

[More information about the data in Kaggle (where I downloaded the data)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

**What is the purpose of the project?**
To predict which customers are likely to churn and understanding why.

**How the website will explain why the customer are likely to churn or not?**
by ploting the waterfall to shows how each feature contribute to customer behavior

**What are the ways to enter customer data**
The simple way to enter it manually and the advanced way is by connect to the database and select the user from the database.

**How the system will work**
I will use flask for front-end and SQLite for the database, and will be two ways to access to customer first by enter customer data, or by access to the database and search for it by the ID.

**What is the pages of the project**
/ (MAIN): Will be the dashboard, contain the percent of churn and unchurn customers, and the effect of each feature, and the type of customers that use our product depend on the data.
/analyze_customer: Selecting customer and analyze them.
