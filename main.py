from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models, schemas
from database import engine, SessionLocal, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS (VERY IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

VALID_STATUSES = ["applied", "interview", "selected", "rejected"]

# ✅ Root route (no more 404)
@app.get("/")
def home():
    return {"message": "Candidate API is running 🚀"}

# 1️⃣ Create Candidate
@app.post("/candidates")
def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db)):
    if candidate.status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status")

    existing = db.query(models.Candidate).filter(models.Candidate.email == candidate.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_candidate = models.Candidate(
        name=candidate.name,
        email=candidate.email,
        skill=candidate.skill,
        status=candidate.status
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return new_candidate

# 2️⃣ Get All Candidates (with optional filter)
@app.get("/candidates")
def get_candidates(status: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Candidate)

    if status:
        if status not in VALID_STATUSES:
            raise HTTPException(status_code=400, detail="Invalid status filter")
        query = query.filter(models.Candidate.status == status)

    return query.all()

# 3️⃣ Update Candidate Status
@app.put("/candidates/{id}/status")
def update_status(id: int, update: schemas.UpdateStatus, db: Session = Depends(get_db)):
    if update.status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status")

    candidate = db.query(models.Candidate).filter(models.Candidate.id == id).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    candidate.status = update.status
    db.commit()
    db.refresh(candidate)

    return candidate