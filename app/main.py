from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from app.schemas import CarInput, PriceOutput

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "car_price_model.pkl"
ml = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml["model"] = joblib.load(MODEL_PATH)
    yield
    ml.clear()


app = FastAPI(title="Car Price Prediction API", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": "model" in ml}


@app.post("/predict", response_model=PriceOutput)
def predict(car: CarInput):
    model = ml.get("model")
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded")

    row = pd.DataFrame([car.to_row()])

    try:
        price = float(model.predict(row)[0])
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed")

    return PriceOutput(predicted_price=round(price, 2))