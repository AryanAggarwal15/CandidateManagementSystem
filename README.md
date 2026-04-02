# 🚀 Candidate Management System

A full-stack Candidate Management System built using **FastAPI (Python
backend)** and **HTML/CSS/JavaScript (frontend)**.\
This project allows recruiters to manage candidates by creating,
viewing, filtering, and updating their status.

------------------------------------------------------------------------

## 📌 Features

-   Create Candidate
-   View All Candidates
-   Filter Candidates by Status
-   Update Candidate Status
-   Status Validation (applied, interview, selected, rejected)
-   Interactive Frontend UI
-   SQLite Database

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Backend: FastAPI (Python)
-   Frontend: HTML, CSS, JavaScript
-   Database: SQLite
-   Server: Uvicorn

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone `<your-repo-link>`{=html} cd candidate_api

### 2. Create Virtual Environment

python -m venv venv venv`\Scripts`{=tex}`\activate`{=tex}

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run Backend

python -m uvicorn main:app --reload

Backend URL: http://127.0.0.1:8000

### 5. Run Frontend

python -m http.server 5500

Frontend URL: http://127.0.0.1:5500

------------------------------------------------------------------------

## 📡 API Endpoints

POST /candidates\
GET /candidates\
GET /candidates?status=interview\
PUT /candidates/{id}/status

------------------------------------------------------------------------

## 🧪 Swagger Docs

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 👨‍💻 Author

Aryan Aggarwal
