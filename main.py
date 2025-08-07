# Imports
from fastapi import FastAPI
from pydantic import BaseModel
import joblib, uvicorn
import pandas as pd

# Initialising FastAPI APP
app = FastAPI(
    title="Iris Prediction API",
    description="An API to predict the species of an Iris flower based on its measurements.",
    version="1.0.0"
)

# Loading Pre-Trained Model
try:
    model = joblib.load('iris_logistic_regression_model.joblib')
except FileNotFoundError:
    print("Error: Model file not found.")
    model = None
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    model = None

# Defining Data structure for Request
class IrisRequest(BaseModel):
    sepal_length: float  
    sepal_width: float
    petal_length: float
    petal_width: float

    # Example data for the automatic docs
    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }

# Defining API Endpoints

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Prediction API! Go to /docs for interactive documentation."}

# Predict Endpoint
@app.post("/predict")
def predict_species(request: IrisRequest):
    # check if model was loaded
    if model is None:
        return {"error": "Model is not available. Please check server logs."}

    # creating dataframe with the same name of column as in training, as it is required for prediction
    input_data = pd.DataFrame([{
        "SL": request.sepal_length,
        "SW": request.sepal_width,
        "PL": request.petal_length,
        "PW": request.petal_width
    }])

    # using model and input data to predict the correct species
    prediction_numeric = model.predict(input_data)
    predicted_class_code = int(prediction_numeric[0])
    species_mapping = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
    predicted_species_name = species_mapping.get(predicted_class_code, "Unknown")

    return {
        "predicted_species_name": predicted_species_name,
    }

# run the API directly from the script using `python main.py`
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)