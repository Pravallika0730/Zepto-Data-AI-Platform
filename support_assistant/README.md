# Zepto Support Assistant

## Overview

This module implements a Retrieval-Augmented Generation (RAG) support assistant for Zepto policy documents.

## Features

- FastAPI REST API
- LangGraph workflow
- ChromaDB vector database
- SentenceTransformer embeddings
- Intent classification
- Policy document retrieval
- Mock LLM response generation

## Project Structure

```
support_assistant/
│
├── app.py
├── graph.py
├── rag.py
├── prompts.py
├── schemas.py
├── Dockerfile
├── requirements.txt
├── README.md
├── docs/
└── chroma_db/
```

## Installation

```bash
pip install -r requirements.txt
```

## Build Vector Database

```bash
python rag.py
```

## Run API

```bash
uvicorn app:app --reload
```

## API

POST `/ask`

Example request:

```json
{
  "question": "What is the delivery fee?"
}
```

Example response:

```json
{
  "answer": "Standard delivery is free for orders above INR 149. Orders below INR 149 incur a flat INR 25 delivery fee."
}
```