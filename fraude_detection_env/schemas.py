from pydantic import BaseModel
from typing import Optional

class ClaimBase(BaseModel):
    amount: float
    severity: int
    age: int
    private_attorney: bool
    marital_status: str
    specialty: str
    insurance: str
    gender: str
    fraudulent: Optional[bool] = False

class ClaimCreate(ClaimBase):
    pass

class Claim(ClaimBase):
    id: int

    class Config:
        orm_mode = True
