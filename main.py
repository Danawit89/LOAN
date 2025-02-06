from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Define the request body format for input data
class LoanData(BaseModel):
    LoanID: str  # LoanID as a string since it's an identifier
    Age: float
    Income: float
    LoanAmount: float
    CreditScore: float
    MonthsEmployed: float
    NumCreditLines: float
    InterestRate: float
    LoanTerm: int
    DTIRatio: float
    Education: str  # Changed to string to accept categorical values
    EmploymentType: str  # Changed to string to accept categorical values
    MaritalStatus: str  # Changed to string to accept categorical values
    HasMortgage: str  # Changed to string to accept categorical values
    HasDependents: str  # Changed to string to accept categorical values
    LoanPurpose: str  # Changed to string to accept categorical values
    HasCoSigner: str  # Changed to string to accept categorical values

# Categorical value mappings for string to integer conversion
education_map = {"Bachelor's": 1, "Master's": 2, "PhD": 3}
employment_type_map = {"Full-time": 1, "Part-time": 2, "Self-employed": 3}
marital_status_map = {"Single": 1, "Married": 2, "Divorced": 3}
has_mortgage_map = {"Yes": 1, "No": 0}
has_dependents_map = {"Yes": 1, "No": 0}
loan_purpose_map = {"Other": 1, "Home": 2, "Car": 3}  # Modify according to your dataset
has_cosigner_map = {"Yes": 1, "No": 0}

# Endpoint to make predictions
@app.post("/predict")
def predict_loan_default(data: LoanData):
    try:
        # Convert input data to dictionary and apply string-to-integer conversion for categorical fields
        data_dict = data.dict()
        data_dict['Education'] = education_map.get(data_dict['Education'], 0)  # Default to 0 if not found
        data_dict['EmploymentType'] = employment_type_map.get(data_dict['EmploymentType'], 0)
        data_dict['MaritalStatus'] = marital_status_map.get(data_dict['MaritalStatus'], 0)
        data_dict['HasMortgage'] = has_mortgage_map.get(data_dict['HasMortgage'], 0)
        data_dict['HasDependents'] = has_dependents_map.get(data_dict['HasDependents'], 0)
        data_dict['LoanPurpose'] = loan_purpose_map.get(data_dict['LoanPurpose'], 0)
        data_dict['HasCoSigner'] = has_cosigner_map.get(data_dict['HasCoSigner'], 0)

        # Include a dummy LoanID in the input data
        data_dict['LoanID'] = 0  # Add a dummy value for LoanID

        # Convert the processed data to DataFrame
        input_data = pd.DataFrame([data_dict])

        # Apply scaling to the input data
        input_data_scaled = scaler.transform(input_data)
        
        # Predict using the trained model
        prediction = model.predict(input_data_scaled)
        
        # Return the prediction result
        result = "Default" if prediction[0] == 1 else "No Default"
        return {"prediction": result}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in prediction: {str(e)}")

# Run the app (using 'uvicorn' from the command line)
# uvicorn app:app --reload