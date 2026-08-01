from fastapi import FastAPI
from schemas import QueryRequest, QueryResponse
from graph import graph

app = FastAPI(
    title="Zepto Support Assistant"
)


@app.get("/")
def home():
    return {
        "message": "Zepto Support Assistant API is Running!"
    }


@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):

    result = graph.invoke(
        {
            "question": request.question,
            "context": "",
            "answer": "",
            "intent": ""
        }
    )

    return QueryResponse(
        answer=result["answer"]
    )