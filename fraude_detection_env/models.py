from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Claim(Base):
    __tablename__ = 'claims'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    severity = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    private_attorney = Column(Boolean, nullable=False)
    marital_status = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    insurance = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    fraudulent = Column(Boolean, default=False)