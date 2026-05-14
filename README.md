# Machine Learning Projects – README

## Overview

This repository contains three machine learning projects focused on predictive analytics using Python and Scikit-learn. Each project demonstrates a complete machine learning workflow including:

* Data exploration and preprocessing
* Feature engineering and encoding
* Model training and evaluation
* Data visualization
* Business insight generation

These projects are suitable for learning supervised machine learning concepts and building practical data science experience.

---

# Projects Included

## 1. Customer Churn Prediction (Bank Customers)

**File:** `task_3_customer_churn_prediction_(bank_customers).py`

### Objective

Predict whether a bank customer is likely to leave the bank (customer churn prediction).

### Dataset

Churn Modelling Dataset (`Churn_Modelling.csv`)

### Techniques Used

* Data cleaning
* One-hot encoding
* Train-test split
* Random Forest Classification
* Feature importance analysis

### Key Features

* Geography
* Gender
* Age
* Balance
* Credit Score
* Estimated Salary
* Tenure

### Model Used

* `RandomForestClassifier`

### Evaluation Metrics

* Accuracy Score
* Classification Report
* Confusion Matrix

### Key Insights

* Age was one of the strongest churn indicators.
* Customers with lower engagement and balance patterns showed higher churn probability.
* Feature importance analysis helped identify business-critical churn drivers.

### Libraries Used

* pandas
* scikit-learn
* matplotlib
* seaborn

---

# 2. Predicting Insurance Claim Amounts

**File:** `task_4_predicting_insurance_claim_amounts.py`

### Objective

Predict medical insurance charges based on customer attributes.

### Dataset

Medical Cost Personal Dataset (`insurance.csv`)

### Techniques Used

* Data preprocessing
* One-hot encoding
* Linear regression modeling
* Data visualization
* Regression evaluation

### Key Features

* Age
* BMI
* Smoking status
* Gender
* Region
* Number of children

### Model Used

* `LinearRegression`

### Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

### Visualizations Included

* BMI vs Charges
* Age vs Charges
* Smoking Status vs Charges

### Key Insights

* Smoking status had the strongest impact on insurance costs.
* Higher BMI generally increased medical charges.
* Older individuals tended to have higher insurance expenses.

### Libraries Used

* pandas
* scikit-learn
* matplotlib
* seaborn
* numpy

---

# 3. Personal Loan Acceptance Prediction

**File:** `task_5_personal_loan_acceptance_prediction.py`

### Objective

Predict whether customers are likely to accept a personal loan offer.

### Dataset

Bank Marketing Dataset (`bank.csv`)

### Techniques Used

* Exploratory Data Analysis (EDA)
* One-hot encoding
* Logistic Regression
* Decision Tree Classification
* Customer behavior analysis

### Key Features

* Age
* Job
* Marital Status
* Education
* Housing Loan
* Contact Type

### Models Used

* `LogisticRegression`
* `DecisionTreeClassifier`

### Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Key Insights

* Loan acceptance prediction suffered from class imbalance.
* Students and retired customers showed higher acceptance rates.
* Logistic Regression and Decision Tree models achieved strong overall accuracy but weaker minority-class prediction performance.

### Libraries Used

* pandas
* scikit-learn
* matplotlib
* seaborn

---

# Installation

Install required Python libraries before running the scripts:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

# How to Run

Run any project file using Python:

```bash
python task_3_customer_churn_prediction_(bank_customers).py
```

```bash
python task_4_predicting_insurance_claim_amounts.py
```

```bash
python task_5_personal_loan_acceptance_prediction.py
```

---

# Project Structure

```text
├── task_3_customer_churn_prediction_(bank_customers).py
├── task_4_predicting_insurance_claim_amounts.py
├── task_5_personal_loan_acceptance_prediction.py
├── Churn_Modelling.csv
├── insurance.csv
├── bank.csv
└── README.md
```

---

# Skills Demonstrated

* Machine Learning Fundamentals
* Classification and Regression
* Data Cleaning and Preprocessing
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Model Evaluation
* Data Visualization
* Business Insight Extraction

---

# Future Improvements

Possible enhancements for these projects include:

* Hyperparameter tuning
* Cross-validation
* Handling class imbalance with SMOTE
* Feature selection optimization
* Advanced ensemble models (XGBoost, LightGBM)
* Deployment using Flask or Streamlit

---

# Author

Created as part of practical machine learning and data analytics learning projects using Python and Scikit-learn.
