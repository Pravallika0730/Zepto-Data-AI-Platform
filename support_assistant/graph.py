from typing import TypedDict

import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer
from langgraph.graph import StateGraph, END

from prompts import SYSTEM_PROMPT


# -----------------------------
# Load Embedding Model
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Load ChromaDB
# -----------------------------
BASE_DIR = Path(__file__).parent

client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

collection = client.get_collection("zepto_docs")


# -----------------------------
# Graph State
# -----------------------------
class GraphState(TypedDict):
    question: str
    context: str
    answer: str
    intent: str


# -----------------------------
# Intent Classifier
# -----------------------------
def classify_intent(state: GraphState):

    question = state["question"].lower()

    keywords = [
    "delivery",
    "fee",
    "charges",
    "return",
    "refund",
    "membership",
    "pass",
    "gift",
    "gift card",
    "cancel",
    "support",
    "order",
    "replacement",
    "damaged",
    "tracking",
    "track"
]

    if any(word in question for word in keywords):
        state["intent"] = "policy"
    else:
        state["intent"] = "general"

    return state


# -----------------------------
# Retrieve + Answer
# -----------------------------
def retrieve_and_answer(state: GraphState):

    embedding = model.encode(state["question"]).tolist()

    result = collection.query(
        query_embeddings=[embedding],
        n_results=1
    )

    context = result["documents"][0][0]

    state["context"] = context

    question = state["question"].lower()

    # MOCK LLM
    if (
    "delivery" in question
    or "fee" in question
    or "charge" in question
):
        state["answer"] = (
            "Standard delivery is free for orders above INR 149. "
            "Orders below INR 149 incur a flat INR 25 delivery fee. "
            "Priority delivery is available for an additional INR 15."
        )

    elif "gift" in question and "valid" in question:
        state["answer"] = (
            "Zepto gift cards are valid for 1 year from the date of issue."
        )

    elif "return" in question or "refund" in question:
        state["answer"] = (
            "Damaged, spoiled, or incorrect grocery items can be reported "
            "within 24 hours. Approved refunds are processed within "
            "3–5 business days to the original payment method or instantly "
            "to the Zepto Wallet if selected."
        )

    elif "cancel" in question:
        state["answer"] = (
            "Orders can be cancelled free of cost before they are packed. "
            "Once packed, cancellation is no longer available."
        )

    elif "membership" in question or "pass" in question:
        state["answer"] = (
            "Zepto offers Basic, Zepto Pass, and Zepto Pass+ memberships "
            "with different delivery and discount benefits."
        )

    elif "support" in question:
        state["answer"] = (
            "Zepto customer support is available 24/7 through in-app chat. "
            "Email support is also available for non-urgent queries."
        )

    else:
        state["answer"] = (
            "I'm sorry, I couldn't find that information "
            "in the available policy documents."
        )

    return state

# -----------------------------
# Direct Answer
# -----------------------------
def direct_answer(state: GraphState):

    state["answer"] = (
        "I'm sorry, I couldn't find that information "
        "in the available policy documents."
    )

    return state


# -----------------------------
# Routing
# -----------------------------
def route(state: GraphState):

    if state["intent"] == "policy":
        return "retrieve"

    return "direct"


# -----------------------------
# Build Graph
# -----------------------------
builder = StateGraph(GraphState)

builder.add_node(
    "classify",
    classify_intent
)

builder.add_node(
    "retrieve",
    retrieve_and_answer
)

builder.add_node(
    "direct",
    direct_answer
)

builder.set_entry_point("classify")

builder.add_conditional_edges(
    "classify",
    route,
    {
        "retrieve": "retrieve",
        "direct": "direct"
    }
)

builder.add_edge("retrieve", END)
builder.add_edge("direct", END)

graph = builder.compile()