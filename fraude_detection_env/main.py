from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from dependency import get_db
from models import Claim

# Initialize FastAPI
app = FastAPI()

# Request model to validate extracted data from Colab
class ClaimData(BaseModel):
    amount: float
    severity: int
    age: int
    private_attorney: bool
    marital_status: str
    specialty: str
    insurance: str
    gender: str
    fraudulent: bool = False  # Default to False

# Fraud detection logic (basic placeholder)
def detect_fraud(claim: ClaimData) -> bool:
    # Example logic: High severity and low age could indicate fraud
    if claim.severity > 5 and claim.age < 18:
        return True
    return False

# API to process claims
@app.post("/process-claim/")
def process_claim(claim_data: ClaimData, db: Session = Depends(get_db)):
    # Detect fraud
    claim_data.fraudulent = detect_fraud(claim_data)

    # Save the claim to the database
    new_claim = Claim(**claim_data.dict())
    db.add(new_claim)
    db.commit()
    db.refresh(new_claim)

    return {"message": "Claim processed successfully", "claim_id": new_claim.id, "fraudulent": claim_data.fraudulent}
