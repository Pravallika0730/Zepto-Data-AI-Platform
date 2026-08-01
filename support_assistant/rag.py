from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

# -----------------------------
# Load Embedding Model
# -----------------------------
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully!\n")

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = Path(__file__).parent

DOCS_DIR = BASE_DIR / "docs"

CHROMA_DIR = BASE_DIR / "chroma_db"

print("Current Folder :", BASE_DIR)
print("Docs Folder    :", DOCS_DIR)
print("Chroma Folder  :", CHROMA_DIR)
print()

# -----------------------------
# Create ChromaDB Client
# -----------------------------
client = chromadb.PersistentClient(path=str(CHROMA_DIR))

collection = client.get_or_create_collection(
    name="zepto_docs"
)

# -----------------------------
# Remove Existing Documents
# -----------------------------
existing = collection.get()

if existing["ids"]:
    collection.delete(ids=existing["ids"])

# -----------------------------
# Read Documents
# -----------------------------
files = sorted(DOCS_DIR.glob("*.txt"))

print(f"Documents Found: {len(files)}\n")

for file in files:

    print(f"Embedding {file.name}")

    text = file.read_text(encoding="utf-8")

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[file.stem],
        documents=[text],
        embeddings=[embedding]
    )

print("\n----------------------------------")
print("All documents embedded successfully!")
print("Total Documents:", collection.count())
print("----------------------------------")