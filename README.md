# 🚗 Car Price Prediction — Machine Learning + REST API

A machine learning project that predicts used car prices (USD) from vehicle features, served through a **FastAPI** REST API.

The project covers data cleaning, feature engineering, a Scikit-learn preprocessing pipeline, a Random Forest regressor, model evaluation, and a tested prediction API.

## 📌 Highlights

- End-to-end workflow: raw CSV → cleaned data → trained pipeline → saved model → API.
- The whole preprocessing + model `Pipeline` is saved as one file, so training and prediction use identical transformations.
- FastAPI service with request validation (Pydantic), a health check, and automated tests (`pytest`).
- Honest evaluation: train and test scores are both reported, and the limitations are listed below.

## 🗂️ Project Structure

```
car-price-prediction-ml/
├── app/
│   ├── main.py          # FastAPI app: /health and /predict
│   └── schemas.py       # Request/response models and input validation
├── data/                # Dataset
├── model/
│   └── car_price_model.pkl   # Saved Scikit-learn Pipeline
├── notebooks/
│   └── car_price_prediction.ipynb
├── test/
│   └── test_api.py      # API tests (pytest)
├── requirements.txt
├── LICENSE
└── README.md
```

## 📊 Dataset

About 4,000 used car listings with these columns:

| Column | Description |
|--------|-------------|
| `brand`, `model` | Make and model |
| `model_year` | Year of manufacture |
| `milage` | Mileage (spelled this way in the original dataset) |
| `fuel_type` | Fuel type |
| `engine` | Raw engine description text |
| `transmission` | Transmission type |
| `ext_col`, `int_col` | Exterior / interior color |
| `accident` | Accident history |
| `clean_title` | Title status (dropped, see below) |
| `price` | Target (USD) |

The exact features used by the model differ from the raw columns after cleaning and feature engineering.

## ⚙️ Machine Learning Workflow

### 1. Data Cleaning
- Dropped `clean_title`.
- Converted `milage` (e.g. `"51,000 mi."`) and `price` (e.g. `"$10,300"`) to numbers.
- Removed listings priced above $200,000 to limit the effect of extreme outliers.
- Filled missing `fuel_type` and `accident` values with `"Unknown"`.
- Dropped remaining rows with missing values (4,009 → 3,934 rows).

### 2. Feature Engineering
Two numeric features are extracted from the raw `engine` text with regular expressions:
- `engine_size` (liters)
- `horsepower`

Missing values in both are filled with the column median.

### 3. Preprocessing
A `ColumnTransformer` inside a Scikit-learn `Pipeline`:

| Feature type | Columns | Transformer |
|--------------|---------|-------------|
| Numeric | `model_year`, `milage`, `engine_size`, `horsepower` | `StandardScaler` |
| Categorical | `brand`, `model`, `fuel_type`, `engine`, `transmission`, `accident` | `OneHotEncoder(handle_unknown="ignore", min_frequency=10)` |

Color columns are present in the input but are not used by the model.

### 4. Model
`RandomForestRegressor(max_depth=22, random_state=4)` trained on an 80/20 train/test split (3,147 / 787 rows, `random_state=4`).

### 5. Saving
The full fitted pipeline is saved with `joblib` to `model/car_price_model.pkl`.

## 📈 Results

Evaluated on a single 80/20 hold-out split:

| Metric | Value |
|--------|------:|
| Test R² | 0.833 |
| Train R² | 0.975 |
| MAE | $7,333 |
| RMSE | $12,329 |

> **Note:** the gap between train R² (0.975) and test R² (0.833) shows that the model overfits. These numbers come from one split and should be treated as preliminary until cross-validation is added.

## 🚀 Getting Started

### 1. Clone and install

```bash
git clone https://github.com/Mobin-Madadi/car-price-prediction-ml.git
cd car-price-prediction-ml
pip install -r requirements.txt
```

The saved model is only guaranteed to load with the **same scikit-learn version** it was trained with, so `requirements.txt` pins exact versions.

### 2. Run the notebook (optional)

```bash
pip install jupyter
jupyter notebook notebooks/car_price_prediction.ipynb
```

Make sure `cars.csv` is at the path the notebook reads from.

## 🌐 API

### Run

```bash
uvicorn app.main:app --reload
```

Interactive documentation (Swagger UI): <http://127.0.0.1:8000/docs>

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Service status and whether the model is loaded |
| POST | `/predict` | Predict the price of a car |

### Example request

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "brand": "Ford",
    "model": "Utility Police Interceptor Base",
    "model_year": 2013,
    "mileage": 51000,
    "fuel_type": "E85 Flex Fuel",
    "engine": "300.0HP 3.7L V6 Cylinder Engine Flex Fuel Capability",
    "transmission": "6-Speed A/T",
    "accident": "At least 1 accident or damage reported",
    "engine_size": 3.7,
    "horsepower": 300
  }'
```

### Example response

```json
{"predicted_price": 15557.78, "currency": "USD"}
```

(The listed price of this car in the dataset is $10,300 — the error is in line with the model's MAE.)

### Input validation

Invalid requests are rejected with `422` before reaching the model, for example:
- `model_year` outside 1990–2027
- negative `mileage`
- missing required fields

### Tests

```bash
pip install pytest httpx
python -m pytest -v
```

5 tests cover the health check, a valid prediction, an invalid year, negative mileage, and a missing field.

## ⚠️ Limitations

- **Overfitting:** train R² is much higher than test R²; no hyperparameter tuning or cross-validation yet.
- **Categorical spelling matters:** values like `brand`, `model`, `transmission` should match the dataset's spelling (e.g. `"6-Speed A/T"`). Unknown values do not raise errors but are ignored by the encoder, which lowers accuracy.
- **Rare models:** categories seen fewer than 10 times in training are grouped together, so predictions for rare models are less reliable.
- **Prices are in USD and reflect the dataset's market**, not any other country or time period.
- **Inconsistent labels:** the transmission label normalization in the notebook only affects exact matches, so most raw labels (e.g. `"6-Speed A/T"`) are used as they are.

## 🔮 Future Improvements

- [ ] Add cross-validation and report mean ± std of the scores.
- [ ] Tune hyperparameters and compare more models (e.g. gradient boosting).
- [ ] Try predicting `log(price)` to handle the skewed price distribution.
- [ ] Return allowed category values from the API and warn on unknown inputs.
- [ ] Add a Dockerfile and deploy the API with a public demo link.
- [ ] Add CI to run the tests on every push.

## 👨‍💻 Author

**Mobin Madadi** — [GitHub](https://github.com/Mobin-Madadi)

## 📄 License

MIT — see [LICENSE](LICENSE).
