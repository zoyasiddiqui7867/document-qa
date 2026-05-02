from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import shutil
import os

from database import get_db, Document
from pdf_parser import extract_text_from_pdf
from embeddings import create_and_save_index
from qa_engine import answer_question

app = FastAPI()

# Allow React frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- UPLOAD PDF ---
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Only allow PDFs
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    
    # Save file to uploads folder
    filepath = f"uploads/{file.filename}"
    with open(filepath, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    # Save record to MySQL
    doc = Document(filename=file.filename, filepath=filepath)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    
    # Extract text and create FAISS index
    text = extract_text_from_pdf(filepath)
    create_and_save_index(doc.id, text)
    
    return {"doc_id": doc.id, "filename": doc.filename, "message": "Uploaded successfully"}

# --- ASK QUESTION ---
class QuestionRequest(BaseModel):
    doc_id: int
    question: str

@app.post("/ask")
def ask_question(request: QuestionRequest, db: Session = Depends(get_db)):
    # Check document exists
    doc = db.query(Document).filter(Document.id == request.doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    answer = answer_question(request.doc_id, request.question)
    return {"answer": answer}

# --- GET ALL DOCUMENTS ---
@app.get("/documents")
def get_documents(db: Session = Depends(get_db)):
    docs = db.query(Document).all()
    return [{"id": d.id, "filename": d.filename, "uploaded_at": d.uploaded_at} for d in docs]