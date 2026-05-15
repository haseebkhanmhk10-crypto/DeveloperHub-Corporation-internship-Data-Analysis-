# Data Science and Analytics Portfolio

A comprehensive collection of data analysis, exploratory data analysis (EDA), and machine learning projects developed during the Data Science & Analytics Internship. This portfolio showcases a robust analytical workflow, emphasizing data preprocessing, predictive modeling, and the extraction of actionable business insights.

---

## 📊 Project Overview

This repository is structured around five distinct analytical tasks. Each task addresses a specific business or statistical problem, utilizing different datasets and requiring tailored machine learning approaches—ranging from simple data visualization to complex classification and regression models.

### Key Objectives
- **Exploratory Data Analysis (EDA):** Uncover underlying patterns, distributions, and anomalies within raw datasets.
- **Data Engineering & Preprocessing:** Implement robust data cleaning strategies, missing value imputation, and categorical feature encoding.
- **Predictive Modeling:** Train, evaluate, and optimize regression and classification algorithms to solve specific domain problems.
- **Insight Generation:** Translate statistical findings and model outputs into actionable intelligence for decision-making.

---

## 📂 Project Structure and Datasets

The repository is organized by task, each containing its respective dataset and source code.

| Task | Domain | Objective | Dataset | Target Variable |
|:---|:---|:---|:---|:---|
| **Task 1** | Data Exploration | Conduct foundational EDA and visualize data distributions. | `iris.csv` | Species Classification |
| **Task 2** | Financial Risk | Analyze and predict credit risk using applicant financial data. | `train/test.csv` | `Loan_Status` |
| **Task 3** | Customer Retention | Predict customer churn likelihood in the banking sector. | `Churn_Modelling.csv` | `Exited` (Binary) |
| **Task 4** | Healthcare | Estimate medical insurance claim amounts based on health factors. | `insurance.csv` | `charges` (Continuous) |
| **Task 5** | Direct Marketing | Predict personal loan offer acceptance for targeted marketing. | `bank.csv` | `y` (Loan Acceptance) |

---

## 🛠️ Technologies and Libraries

This project relies on a modern Python data science stack:
- **Language:** Python 3.x
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `matplotlib`, `seaborn`
- **Machine Learning:** `scikit-learn` (Linear Regression, Logistic Regression, Decision Trees, Random Forest, ColumnTransformer)

---

## 📈 Analysis Workflow & Key Findings

### Task 1: Exploratory Data Analysis
- **Workflow:** Executed foundational data exploration utilizing scatter plots, histograms, and box plots to examine feature distributions and identify potential outliers.
- **Outcome:** Established a baseline understanding of feature scaling and variance before modeling.

### Task 2: Credit Risk Analysis
- **Workflow:** Addressed missing data using robust mode and median imputation strategies. Visualized the distributions of critical financial metrics (e.g., loan amounts, applicant income).
- **Outcome:** Prepared a clean, reliable dataset primed for binary classification of loan default risk.

### Task 3: Bank Customer Churn Prediction
- **Workflow:** Applied one-hot encoding to categorical variables and trained a **Random Forest Classifier**. Extracted and analyzed feature importances.
- **Key Insight:** `Age`, `Estimated Salary`, and `Credit Score` were identified as the primary drivers of customer attrition.
- **Performance:** Achieved an overall accuracy of **86.05%** on the test set.

### Task 4: Medical Insurance Cost Estimation
- **Workflow:** Engineered features for a **Linear Regression** model to predict continuous medical claim amounts.
- **Key Insight:** `Smoking status`, `Age`, and `BMI` exhibited a strong positive correlation with medical insurance charges, with smokers systematically incurring significantly higher costs.
- **Performance:** Evaluated with a Mean Absolute Error (MAE) of **$4,181.19** and RMSE of **$5,796.28**.

### Task 5: Personal Loan Acceptance Prediction
- **Workflow:** Designed a comprehensive preprocessing pipeline using `ColumnTransformer` to handle mixed data types. Trained both **Logistic Regression** and **Decision Tree** classifiers.
- **Key Insight:** Demographic segments such as 'students' and 'retirees' demonstrated higher baseline loan acceptance rates. 
- **Performance:** While the models achieved high overall accuracy (~89.8%), the analysis highlighted the challenge of predicting the minority class (loan acceptance) in a highly imbalanced dataset, emphasizing the need for recall-focused optimization.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.x installed. It is recommended to use a virtual environment.

### Installation
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Install required dependencies:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

### Execution
Navigate to the respective task directory and execute the Python script or launch the Jupyter Notebook:
```bash
cd "Task 1"
python "Task 1 Exploring and Visualizing a Simple Dataset.py"
```

---

## 🔮 Future Enhancements

To further refine the predictive capabilities of these models, future iterations will focus on:
- **Advanced Imbalance Handling:** Implement techniques such as **SMOTE** (Synthetic Minority Over-sampling Technique) or class-weight adjustments to improve recall for minority classes (e.g., in Task 5).
- **Ensemble Modeling:** Explore advanced gradient boosting frameworks like **XGBoost** or **LightGBM** for improved accuracy.
- **Hyperparameter Tuning:** Systematically optimize model parameters utilizing `GridSearchCV` or `RandomizedSearchCV`.

---

## 👤 Author

**Haseeb**  
 https://github.com/haseebkhanmhk10-crypto
 www.linkedin.com/in/haseebkhan01122
