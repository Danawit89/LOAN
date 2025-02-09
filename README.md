
---

# **Loan Default Prediction** 💰

This project aims to build a **machine learning model** that predicts whether a loan applicant will default based on historical financial data. The model utilizes **Random Forest Classification** and is deployed using **FastAPI** and **Render** for real-time predictions.

## **Dataset Details** 📊
- **Source**: Kaggle
- **License**: Publicly available for educational purposes.
- **Structure**: CSV format with structured numerical & categorical features.
- **Target Variable**: `Default` (1 = Default, 0 = No Default).

## **Tech Stack** ⚙️
- **Python** (pandas, scikit-learn, FastAPI, joblib)
- **Visualization**: Matplotlib, Seaborn
- **Model Deployment**: FastAPI, Render

## **Project Structure** 📁

```
├── data/                # Dataset
├── models/              # Trained model files
├── src/
│   ├── train_model.py   # Model training script
│   ├── preprocess.py    # Data preprocessing functions
│   ├── main.py           # FastAPI app for deployment
├── README.md            # Project overview
├── requirements.txt     # Dependencies
└── notebooks/           # Jupyter notebooks for EDA
```

## **⚙️ Installation & Setup** 🚀

### **1️⃣ Clone the Repository**:
```bash
git clone https://github.com/Danawit89/LOAN.git.git
cd loan-default-prediction
```

### **2️⃣ Install Dependencies**:
```bash
pip install -r requirements.txt
```

### **3️⃣ Train the Model**:
```bash
python main.py
```

### **4️⃣ Run FastAPI Server**:
```bash
python -m uvicorn main:app --reload
```

## **API Endpoint** 🔌
**Endpoint**: `POST /predict`

### **Input Format (JSON)**:
```json
{
  "LoanID": "I38PQUQS96",
  "Age": 56,
  "Income": 85994,
  "LoanAmount": 50587,
  "CreditScore": 520,
  "MonthsEmployed": 80,
  "NumCreditLines": 4,
  "InterestRate": 15.23,
  "LoanTerm": 36,
  "DTIRatio": 0.44,
  "Education": "Bachelor's",
  "EmploymentType": "Full-time",
  "MaritalStatus": "Divorced",
  "HasMortgage": "Yes",
  "HasDependents": "Yes",
  "LoanPurpose": "Other",
  "HasCoSigner": "Yes"
}
```

### **Output Format (JSON)**:
```json
{
  "prediction": "No Default"
}
```

### **Input Format (JSON)**:
```json
{
  "LoanID": "C1OZ6DPJ8Y",
  "Age": 46,
  "Income": 84208,
  "LoanAmount": 129188,
  "CreditScore": 451,
  "MonthsEmployed": 26,
  "NumCreditLines": 3,
  "InterestRate": 21.17,
  "LoanTerm": 24,
  "DTIRatio": 0.31,
  "Education": "Master's",
  "EmploymentType": "Unemployed",
  "MaritalStatus": "Divorced",
  "HasMortgage": "Yes",
  "HasDependents": "Yes",
  "LoanPurpose": "Auto",
  "HasCoSigner": "No"
}
```

### **Output Format (JSON)**:
```json
{
  "prediction": "Default"
}
```

---

This project is deployed using **Render**, allowing real-time loan default predictions.

To access the API, visit: [Render API Link](https://loan-i2jn.onrender.com/docs)  

## **📌 Future Enhancements**:
- ✔ Improve model performance with hyperparameter tuning  
- ✔ Add more advanced feature engineering  
- ✔ Deploy on cloud platforms like AWS or GCP

---

**GitHub Repository**: [Loan Default Prediction GitHub](https://github.com/Danawit89/LOAN.git)

---
