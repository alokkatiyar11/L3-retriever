# Lab 3: Document Retrieval System

Semantic search system using ChromaDB and sentence transformers for ARIN 5360.

## Quick Start

```bash
# Install dependencies
uv sync

# Start server
uv run uvicorn src.retrieval.main:app --reload
```

Server starts at http://localhost:8000

## Usage

### Via API

**Check health:**
```bash
curl http://localhost:8000/health
```

### Via Browser

Visit http://localhost:8000 (requires `static/index.html`).

## Testing

Run all Tests with coverage
```Bash
uv run pytest
```

Run any specific files
```bash
uv run pytest .tests\test_store.py\
```

## Code Quality

Run the ruff checks for linting
`uv run ruff check .`

Fixing the lint:
`uv run ruff check --fix`

Check the formatting:
`uv run ruff format --check .`

Formatting the code:
`uv run ruf format .`


## Project Structure
```
lab3
├── documents
│   └── sample1.txt
├── pyproject.toml
├── README.md
├── src
│   └── retrieval
│       ├── __init__.py
│       └── main.py
├── static
│   ├── index.html
│   └── style.css
├── tests
│   ├── __init__.py
│   └── test_smoke.py
└── uv.lock
```

# Architecture:
- Loader: Reads .txt file from the documents/
- Embedder: Converts text to vector using sentenc-transformers
- Store: Manages chromadb collections for similarity search
- Retriever: Coordinates components for end-to-end retrieval
- API: FastAPI endpoints for heath checks and search

# Adding Documents
Place .txt files in the `documents/` directory and restart the server. Documents are indexed automatic startup.

# Screenshot
![API_Web_Interface](5.png)

# Video Links:
