# Module 2: Data Analytics and Machine Learning

## 1. Overview

This module focuses on Exploratory Data Analysis (EDA), data preprocessing, classification, imbalanced-data handling, hyperparameter tuning, and regression analysis.

The analysis was performed using Python and common data science and machine learning libraries.

---

## 2. Objectives

The main objectives of this module are:

- Load and understand the dataset.
- Handle missing values appropriately.
- Perform Exploratory Data Analysis (EDA).
- Analyze relationships between variables.
- Visualize important patterns in the data.
- Preprocess and scale the data.
- Build classification models.
- Handle class imbalance using Class Weight and SMOTE.
- Evaluate classification models using multiple metrics.
- Perform hyperparameter tuning.
- Build and evaluate a regression model.
- Analyze regression residuals.

---

## 3. Technologies and Libraries

The following Python libraries were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- imbalanced-learn

---

# 4. Exploratory Data Analysis

EDA was performed to understand the structure, distribution, and relationships within the dataset.

### Visualizations

The following visualizations were created:

- Age histogram
- Fare histogram
- Fare class box plot
- Survival by gender
- Survival by passenger class
- Pair plot
- Correlation analysis

These visualizations helped identify patterns, distributions, relationships, and potential outliers in the dataset.

---

# 5. Data Preprocessing

The dataset was prepared before model training.

The preprocessing steps included:

1. Loading the dataset using Pandas.
2. Identifying missing values.
3. Handling missing values using appropriate strategies.
4. Selecting relevant features.
5. Encoding categorical variables where required.
6. Scaling numerical features where required.
7. Splitting the data into training and testing sets.

---

# 6. Classification Models

Three classification algorithms were implemented:

### Logistic Regression

Logistic Regression was used as a baseline classification model.

### Decision Tree

A Decision Tree classifier was implemented to capture non-linear relationships between features.

### Random Forest

Random Forest was used as an ensemble classification algorithm to improve predictive performance and robustness.

---

# 7. Model Evaluation

The classification models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

The evaluation results were used to compare the performance of different models.

---

# 8. Handling Imbalanced Data

The class distribution was analyzed before model training.

### Class Distribution

| Class | Count | Percentage |
|------:|------:|-----------:|
| 0 | 439 | 61.74% |
| 1 | 272 | 38.26% |

The dataset showed some class imbalance.

Two approaches were evaluated:

### Class Weight

Class weights were used to give more importance to the minority class during model training.

### SMOTE

SMOTE (Synthetic Minority Over-sampling Technique) was used to generate synthetic samples for the minority class.

### Comparison

| Method | Precision | Recall | F1 Score |
|---|---:|---:|---:|
| Baseline | 0.7966 | 0.6912 | 0.7402 |
| Class Weight | 0.7879 | 0.7647 | 0.7761 |
| SMOTE | 0.7813 | 0.7353 | 0.7576 |

### Interpretation

The Class Weight approach produced the highest F1 Score among the three approaches.

It also improved recall compared with the baseline model.

SMOTE also improved recall compared with the baseline, but its F1 Score was lower than the Class Weight approach.

---

# 9. Hyperparameter Tuning

Hyperparameter tuning was performed to improve model performance.

The Random Forest model was tuned using cross-validation.

### Best Parameters

```text
max_depth = 5
max_features = sqrt
n_estimators = 50
