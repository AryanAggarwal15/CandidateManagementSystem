from pydantic import BaseModel, EmailStr
from typing import Optional

VALID_STATUSES = ["applied", "interview", "selected", "rejected"]

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    skill: str
    status: str

    def validate_status(self):
        if self.status not in VALID_STATUSES:
            raise ValueError("Invalid status")

class CandidateResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    skill: str
    status: str

    class Config:
        from_attributes = True

class UpdateStatus(BaseModel):
    status: str