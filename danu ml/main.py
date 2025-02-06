from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Define input data model
class LoanData(BaseModel):
    Age: float
    Income: float
    LoanAmount: float
    CreditScore: float
    MonthsEmployed: float
    NumCreditLines: float
    InterestRate: float
    LoanTerm: int
    DTIRatio: float

# Prediction endpoint
@app.post("/predict")
def predict_loan_default(data: LoanData):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Apply scaling to numerical fields
        input_data_scaled = scaler.transform(input_data)
        
        # Make a prediction
        prediction = model.predict(input_data_scaled)
        
        # Format response
        result = "Default" if prediction[0] == 1 else "No Default"
        return {"prediction": result}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in prediction: {str(e)}")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Loan Default Prediction API is running successfully!"}