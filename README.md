# Iris Species Prediction API

This project provides a simple and robust API to predict the species of an Iris flower (Setosa, Versicolor, or Virginica) based on its sepal and petal measurements.

The project is built using **FastAPI** for the web framework and a **Logistic Regression** model trained with **Scikit-learn**. It serves as a complete example of how to deploy a machine learning model into a production-ready web service.

---

## Features

- **FastAPI Backend**: A modern, high-performance web framework for building APIs.
- **Scikit-learn Model**: Uses a trained Logistic Regression model for predictions.
- **Data Validation**: Employs Pydantic for robust, type-hinted validation of incoming request data.
- **Interactive Docs**: Automatically generates interactive API documentation (via Swagger UI at `/docs`).
- **Clear Project Structure**: Organized for clarity and best practices in a production environment.

---

## Project Structure

```bash
iris_api/
├── .venv/ # Virtual environment directory
├── main.py # The main FastAPI application code
├── iris_logistic_regression_model.joblib # The pre-trained model file
├── requirements.txt # Project dependencies
└── README.md # This file
```
---

## Setup and Installation

To run this project locally, please follow these steps:

**1. Clone the Repository (or create the folder structure manually)**

**2. Create and Activate a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Navigate to the project directory
cd path/to/iris_api

# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
3. Install Dependencies

Install all the required Python libraries from the requirements.txt file.

```bash
pip install -r requirements.txt
```
How to Run the API
With the virtual environment active and dependencies installed, start the API server using Uvicorn.

```bash
uvicorn main:app --reload
```
The server will start and be accessible at http://127.0.0.1:8000.

How to Use the API
Once the server is running, you can interact with the API in two ways:

1. Interactive Documentation (Recommended)

Open your web browser and navigate to:

```bash
http://127.0.0.1:8000/docs
```
This will open the Swagger UI, where you can see all the available endpoints, test them with sample data, and see the responses directly in your browser.

2. Using curl (Command Line)

You can also send a POST request to the /predict endpoint using a command-line tool like curl.

```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.9,
  "sepal_width": 3,
  "petal_length": 5.1,
  "petal_width": 1.8
}'
```
```bash
Expected Response:

{
  "predicted_species_name": "Iris-virginica"
}
```
