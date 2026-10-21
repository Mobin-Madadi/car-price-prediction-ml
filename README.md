# 🚗 Car Price Prediction — Machine Learning

A machine learning project focused on predicting used car prices
using Python and Scikit-learn.

The project explores data preprocessing, feature engineering,
categorical encoding, regression models, and model evaluation
to understand the factors that influence used car prices.

## 🎯 Project Goals

- Explore and clean used car price data.
- Handle missing values and inconsistent categorical data.
- Perform feature engineering on vehicle specifications.
- Build reproducible preprocessing and machine learning pipelines.
- Train and evaluate regression models.
- Investigate the features that contribute to price predictions.
- Prepare the trained model for future API integration.

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## 📊 Dataset Features

The dataset includes information about used vehicles, such as:

- Brand and model
- Model year
- Mileage
- Fuel type
- Engine specifications
- Transmission
- Exterior and interior colors
- Accident history
- Vehicle price

The exact features used by the model may differ from the
original dataset after preprocessing and feature engineering.

## ⚙️ Machine Learning Workflow

### 1. Data Cleaning

- Inspect missing values.
- Handle missing numerical and categorical values.
- Normalize inconsistent categorical labels.
- Remove features that provide no useful variation.

### 2. Feature Engineering

Additional numerical features are extracted from engine
specifications, including:

- `engine_size`
- `horsepower`

Missing values in these engineered features are handled
using median imputation.

### 3. Preprocessing

A Scikit-learn `ColumnTransformer` is used to process
numerical and categorical features.

Numerical preprocessing:
- `StandardScaler`

Categorical preprocessing:
- `OneHotEncoder`
- `handle_unknown="ignore"`
- `min_frequency=10`

The preprocessing steps are integrated into a Scikit-learn
`Pipeline` to keep transformations consistent between
training and prediction.

### 4. Model Training

The project currently explores regression algorithms,
including:

- Linear Regression
- Random Forest Regressor

Random Forest is used to model nonlinear relationships
between vehicle specifications and prices.

### 5. Model Evaluation

Model performance is evaluated using regression metrics:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The project also compares training and test R² scores
to investigate potential overfitting.

### 6. Feature Importance

Permutation importance is used to investigate how individual
input features affect model performance.

This helps identify which vehicle characteristics are
most informative for predicting prices.

## 📈 Preliminary Results

On the current train-test split, the following R² scores
have been observed:

| Model | Test R² |
|---|---:|
| Linear Regression | ~0.690 |
| Random Forest Regressor | ~0.83 |

The Random Forest model currently achieves the best observed
test R² score.

These results are preliminary and depend on the selected
train-test split and model configuration. Cross-validation
and further validation are needed to assess generalization
more reliably.

## 🚀 Getting Started

### Prerequisites

- Python
- Jupyter Notebook
- Required Python libraries

### Installation

Clone the repository:

```bash
git clone https://github.com/Mobin-Madadi/car-price-prediction-ml.git
cd car-price-prediction-ml
```

Install the required dependencies:

```bash
pip install numpy pandas scikit-learn jupyter
```

Open the project notebook and execute its cells in order.

Make sure the dataset is available at the path expected
by the notebook.

🔮 Future Improvements
- Validate model performance using cross-validation.
- Evaluate additional regression algorithms.
- Improve model generalization.
- Save the complete trained preprocessing and prediction pipeline.
- Build a REST API using FastAPI.
- Add input validation and prediction tests.
- Document API usage and example requests.

👨‍💻 Author
Mobin Madadi

GitHub: *[Mobin Madadi](https://github.com/Mobin-Madadi)*
