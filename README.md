# DocMind — Local Document Q&A System

> Upload a PDF. Ask questions. Get answers — 100% locally, no internet required.



---

## What is this?

DocMind is a **local RAG (Retrieval-Augmented Generation)** system that lets you:
- Upload any PDF document
- Ask natural language questions about it
- Get accurate answers based **only** on that document

No OpenAI. No API keys. No internet. Everything runs on your machine.

---

## How it works

```
PDF Upload
    ↓
Extract Text (PyMuPDF)
    ↓
Split into Chunks (LangChain)
    ↓
Convert to Vectors (sentence-transformers)
    ↓
Store in FAISS Index
    ↓
User asks a question
    ↓
Question → Vector → Find similar chunks (FAISS)
    ↓
Chunks + Question → Ollama (llama3.2)
    ↓
Answer returned to user
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Tailwind CSS |
| Backend | Python + FastAPI |
| LLM | Ollama (llama3.2) — runs locally |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Search | FAISS |
| PDF Parsing | PyMuPDF |
| Database | MySQL + SQLAlchemy |
| Text Splitting | LangChain |

---

## Project Structure

```
document-qa/
├── backend/
│   ├── main.py            # FastAPI app and API routes
│   ├── database.py        # MySQL connection and Document model
│   ├── pdf_parser.py      # Extract text from PDF using PyMuPDF
│   ├── embeddings.py      # Chunk text, create and query FAISS index
│   ├── qa_engine.py       # Send context + question to Ollama
│   └── uploads/           # Uploaded PDF files stored here
│   └── faiss_indexes/     # FAISS indexes saved per document
├── frontend/
│   ├── src/
│   │   └── App.jsx        # Main React component
│   ├── index.html
│   └── package.json
└── README.md
```

---

## Prerequisites

Make sure you have these installed before starting:

- Python 3.10+
- Node.js 18+
- MySQL 8.0+
- [Ollama](https://ollama.com/download) — download and install from ollama.com

---

## Setup Instructions

### Step 1 — Clone the repository

```bash
git clone https://github.com/yourusername/document-qa.git
cd document-qa
```

### Step 2 — Set up MySQL

Open MySQL Workbench or terminal and run:

```sql
CREATE DATABASE document_qa;
```

### Step 3 — Set up the backend

```bash
cd backend
pip install fastapi uvicorn python-multipart sqlalchemy pymysql pymupdf langchain langchain-community sentence-transformers faiss-cpu requests
```

Update your MySQL password in `database.py`:
```python
password = quote_plus("your_mysql_password")
```

### Step 4 — Pull the Ollama model

```bash
ollama pull llama3.2
```

This downloads the LLM locally (~2GB). Only needed once.

### Step 5 — Start Ollama

```bash
ollama serve
```

Keep this terminal open.

### Step 6 — Start the backend

Open a new terminal:

```bash
cd backend
uvicorn main:app --reload
```

Backend runs at: `http://localhost:8000`

You can test it at: `http://localhost:8000/docs`

### Step 7 — Set up and start the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at: `http://localhost:5173`

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/upload` | Upload a PDF file |
| POST | `/ask` | Ask a question about a document |
| GET | `/documents` | Get list of all uploaded documents |
| GET | `/` | Health check |

### Example — Upload PDF
```bash
curl -X POST http://localhost:8000/upload \
  -F "file=@document.pdf"
```

### Example — Ask a question
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"doc_id": 1, "question": "What is this document about?"}'
```

---

## Usage

1. Open `http://localhost:5173` in your browser
2. Click **Upload PDF** and select any PDF file
3. Wait for processing (text extraction + indexing)
4. Type your question in the input box
5. Press Enter or click **Ask**
6. Get your answer instantly

---

## Constraints

- Only PDF files are supported
- Answers are based strictly on the uploaded document content
- No external AI APIs used — fully offline
- Scanned PDFs (image-only) may not extract text properly

---

## Demo

> Upload a PDF → Ask questions → Get answers locally

Screenshots and demo video included in `/demo` folder.

---

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) — Modern Python web framework
- [Ollama](https://ollama.com/) — Run LLMs locally
- [sentence-transformers](https://www.sbert.net/) — Text embeddings
- [FAISS](https://github.com/facebookresearch/faiss) — Vector similarity search by Meta
- [LangChain](https://langchain.com/) — Text splitting utilities
- [PyMuPDF](https://pymupdf.readthedocs.io/) — PDF text extraction
- [React](https://react.dev/) — Frontend UI
- [Tailwind CSS](https://tailwindcss.com/) — Styling

---

## Author

Made with love for the Webseeder Technologies internship task assessment.

---

## License

MIT License — free to use and modify.




