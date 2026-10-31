from pydantic import BaseModel, Field


class CarInput(BaseModel):
    brand: str = Field(min_length=1, examples=["Ford"])
    model: str = Field(min_length=1, examples=["Utility Police Interceptor Base"])
    model_year: int = Field(ge=1990, le=2027, examples=[2013])
    mileage: float = Field(ge=0, le=500_000, examples=[51000])
    fuel_type: str = Field(examples=["E85 Flex Fuel"])
    engine: str = Field(default="Unknown", examples=["3.7L V6 Cylinder Engine"])
    transmission: str = Field(examples=["6-Speed A/T"])
    accident: str = Field(examples=["At least 1 accident or damage reported"])
    engine_size: float = Field(gt=0, le=10, examples=[3.7])
    horsepower: float = Field(gt=0, le=2000, examples=[300])

    def to_row(self) -> dict:
        return {
            "brand": self.brand,
            "model": self.model,
            "model_year": self.model_year,
            "milage": self.mileage,
            "fuel_type": self.fuel_type,
            "engine": self.engine,
            "transmission": self.transmission,
            "ext_col": "Unknown",
            "int_col": "Unknown",
            "accident": self.accident,
            "engine_size": self.engine_size,
            "horsepower": self.horsepower,
        }


class PriceOutput(BaseModel):
    predicted_price: float
    currency: str = "USD"