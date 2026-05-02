import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load once when server starts
model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text: str):
    """Split text into small chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text)

def create_and_save_index(doc_id: int, text: str):
    """Create FAISS index from text and save to disk"""
    chunks = chunk_text(text)
    
    # Convert chunks to vectors
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")
    
    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    
    # Save index and chunks to disk
    faiss.write_index(index, f"faiss_indexes/{doc_id}.index")
    with open(f"faiss_indexes/{doc_id}_chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def get_similar_chunks(doc_id: int, question: str, top_k=3):
    """Find most relevant chunks for a question"""
    # Load saved index and chunks
    index = faiss.read_index(f"faiss_indexes/{doc_id}.index")
    with open(f"faiss_indexes/{doc_id}_chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    
    # Convert question to vector
    question_vector = model.encode([question])
    question_vector = np.array(question_vector).astype("float32")
    
    # Search top_k similar chunks
    _, indices = index.search(question_vector, top_k)
    
    return [chunks[i] for i in indices[0]]