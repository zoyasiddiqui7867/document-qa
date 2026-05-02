import requests
from embeddings import get_similar_chunks

def answer_question(doc_id: int, question: str) -> str:
    """Get answer from Ollama using relevant PDF chunks"""
    
    # Get relevant chunks
    chunks = get_similar_chunks(doc_id, question)
    context = "\n\n".join(chunks)
    
    # Build prompt
    prompt = f"""Answer the question based only on the context below. 
If the answer is not in the context, say 'I dont know'.

Context:
{context}

Question: {question}

Answer:"""
    
    # Call Ollama locally
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    
    return response.json()["response"]