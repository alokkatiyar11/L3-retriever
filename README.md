# Lab 3: Document Retrieval System

Semantic search system using ChromaDB and sentence transformers for ARIN 5360.

This project implements a document retrieval system that uses vector embeddings and semantic search to find relevant information across text and PDF documents. The system automatically chunks large documents into smaller, overlapping segments for more precise retrieval and better search results.


### Chunking:
Let's have a look at what this project is intended to perform:

Chunking results from dracula text file:
![chunking_results_from_dracula_text_file](/images/q5.png)

Chunking results from MSAI pdf file:
![chunking_results_from_msai_pdf_file](/images/q5_1.png)

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
L3-retriever/
├── documents/
│   ├── 01_cloud_onboarding.txt
│   ├── 02_password_reset.txt
│   ├── 03_ml_model_deployment.txt
│   ├── 04_api_rate_limits.txt
│   ├── 05_database_backup.txt
│   ├── 06_incident_response.txt
│   ├── 07_kubernetes_scaling.txt
│   ├── 08_data_privacy_policy.txt
│   ├── 09_logging_best_practices.txt
│   ├── 10_network_troubleshooting.txt
│   ├── 11_frontend_deployment.txt
│   ├── 12_git_workflow.txt
│   ├── 13_monitoring_alerts.txt
│   ├── 14_security_audit.txt
│   ├── 15_ci_cd_pipeline.txt
│   ├── 16_data_pipeline_overview.txt
│   ├── 17_customer_support_process.txt
│   ├── 18_api_authentication.txt
│   ├── 19_code_review_guidelines.txt
│   ├── 20_release_management.txt
│   ├── 21_data_retention.txt
│   ├── 22_access_control.txt
│   ├── 23_performance_testing.txt
│   ├── 24_disaster_recovery.txt
│   ├── 25_api_versioning.txt
│   ├── 26_training_new_engineers.txt
│   ├── 27_remote_work_policy.txt
│   ├── 28_cloud_cost_optimization.txt
│   ├── 29_feature_flag_usage.txt
│   ├── 30_internal_wiki_usage.txt
│   ├── dracula_by_bram_stoker.txt
│   ├── MSAI-courses.pdf
│   ├── sample1.txt
│   ├── sample2.txt
│   ├── sample3.txt
│   └── sample4.txt
│
├── images/
│   ├── q5_1.png
│   └── q5.png
|
├── src/
│   └── retrieval/
│       ├── __init__.py
│       ├── embeddings.py
│       ├── loader.py
│       ├── main.py
│       ├── retriever.py
│       └── store.py
│
├── static/
│   ├── index.html
│   └── style.css
│
├── tests/
│   ├── __pycache__/
│   ├── data/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_integration.py
│   ├── test_loader.py
│   ├── test_retriever.py
│   ├── test_smoke.py
│   └── test_store.py
│
├── .gitignore
├── .python-version
├── README.md
├── image2.png
├── pyproject.toml
└── uv.lock
```

# Architecture:

- Loader: Reads .txt file from the documents/
- Embedder: Converts text to vector using sentenc-transformers
- Store: Manages chromadb collections for similarity search
- Retriever: Coordinates components for end-to-end retrieval
- API: FastAPI endpoints for heath checks and search
- Chunking: Test file for document chunking and document loader.

# Adding Documents

Place .txt and .pdf files in the `documents/` directory and restart the server. Documents are indexed automatic startup.

# Screenshot

![API_Web_Interface](image2.png)

# Video Links:
Lab3 Retrieval:
https://youtu.be/mrfsLGAVN8o

Lab4: Chunking:
https://youtu.be/BoKSugwwzys