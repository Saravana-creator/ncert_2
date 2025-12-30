#This is for handling the API calls like post,get,put,delete

from fastapi import FastAPI
from pydantic import BaseModel
from ingest import ingest_file
from rag import retrieve
from llm import answer

app=FastAPI()

class IngestRequest(BaseModel):
    path: str

class QuestionRequest(BaseModel):
    question: str
    grade: str = "10"

@app.post("/ingest")
def ingest(data: IngestRequest):
    try:
        result = ingest_file(data.path)
        return {"status":"success", "message": str(result)}
    except Exception as e:
        return {"status":"error", "message": str(e)}

@app.post("/ask")
def ask(data: QuestionRequest):
    try:
        # retrieve returns list of dicts [{'text':..., 'page':...}]
        docs = retrieve(data.question)
        
        # llm.answer returns dict {'answer':..., 'citations':...}
        response = answer(data.question, docs)
        
        return response
    except Exception as e:
        print(f"Error in /ask: {e}")
        return {
            "answer": f"Error processing question: {str(e)}",
            "citations": []
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)