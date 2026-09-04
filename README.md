# 🚗 Car Price Prediction ML

A Machine Learning project focused on predicting car prices based on vehicle features using **Python, Pandas, NumPy, Matplotlib, and Scikit-learn**.

This project was built as a practical Machine Learning project, covering the main steps of a typical ML workflow — from data cleaning and exploratory data analysis to feature engineering, model training, evaluation, and prediction.

---

## 📌 Project Overview

The goal of this project is to build a model that can estimate the price of a car based on information such as its mileage, engine characteristics, and other available vehicle features.

The project focuses on understanding the complete workflow of a **Regression Machine Learning problem** rather than simply training a model.

### 🔄 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Data Preprocessing
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Train / Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Prediction
```

---

## 📂 Project Structure

```text
car-price-prediction-ml/
│
├── data/
│   └── dataset files
│
├── notebooks/
│   └── machine learning notebooks
│
├── README.md
└── LICENSE
```

---

## 🧹 Data Cleaning & Preprocessing

Before training the models, the dataset was cleaned and prepared for Machine Learning.

The preprocessing steps included:

* Handling missing values
* Inspecting data types
* Removing or dealing with unnecessary data
* Converting features into usable numerical formats
* Checking the distribution of the target variable
* Detecting and handling unrealistic values
* Preparing the dataset for model training

---

## 📊 Exploratory Data Analysis

Exploratory Data Analysis was performed to better understand the dataset and identify relationships between vehicle features and price.

The analysis included:

* Distribution analysis
* Feature relationships
* Correlation analysis
* Visualization of important variables
* Investigation of outliers
* Analysis of the target variable

### 📈 Visualization

The project uses **Matplotlib** to visualize the data and better understand patterns within the dataset.

---

## ⚙️ Feature Engineering

Different features were investigated and prepared to improve the performance of the regression models.

Feature engineering was used to:

* Transform raw features
* Prepare numerical variables
* Improve model input
* Investigate relationships between features and car prices

---

## 🤖 Machine Learning Models

The project focuses on **Regression** because the target variable — car price — is continuous.

Different regression approaches were investigated, including:

### Multiple Linear Regression

A baseline regression model used to estimate car prices from multiple vehicle features.

### Polynomial Regression

Polynomial features were also explored to investigate whether non-linear relationships between the input features and car price could improve the model.

The models were compared based on their performance on unseen test data.

---

## 🧪 Model Evaluation

The trained models were evaluated using a separate test dataset.

The evaluation process focuses on measuring how accurately the models can predict car prices for data they have not seen during training.

Evaluation metrics were used to compare different approaches and determine which model performed better.

---

## 📈 Results

The project demonstrates how different preprocessing techniques and regression approaches can affect prediction performance.

Rather than relying on a single model, the project explores the relationship between:

```text
Data Quality
     +
Feature Selection
     +
Feature Engineering
     +
Model Selection
     ↓
Prediction Performance
```

The experiments also show the importance of inspecting the target variable and handling extreme or unrealistic values before training a regression model.

---

## 🛠️ Technologies Used

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Mobin-Madadi/car-price-prediction-ml.git
```

### 2. Navigate to the project

```bash
cd car-price-prediction-ml
```

### 3. Install the required libraries

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

### 4. Start Jupyter Notebook

```bash
jupyter notebook
```

Then open the notebooks inside the `notebooks` directory.

---

## 📚 What I Learned

This project helped me gain practical experience with:

* 🐍 Python for Machine Learning
* 🧹 Data Cleaning
* 📊 Exploratory Data Analysis
* 📈 Data Visualization
* ⚙️ Feature Engineering
* 🔀 Train/Test Splitting
* 🤖 Regression Models
* 📐 Multiple Linear Regression
* 📊 Polynomial Regression
* 🧪 Model Evaluation
* 🔍 Comparing Machine Learning approaches

---

## 👤 Author

**Mobin Madadi**

🐙 GitHub: [Mobin-Madadi](https://github.com/Mobin-Madadi)

---

## 📄 License

This project is licensed under the **MIT License**.
