"""
Lab 3 FastAPI API.
@author: Aarti Dashore, Alok Katiyar
Seattle University, ARIN 5360
@see: https://catalog.seattleu.edu/preview_course_nopop.php?catoid=55&coid
=190380
@version: 0.1.0+w26
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class DocumentLoader:
    """
    Docstring for DocumentLoader
    Load all the text document from the directory
    Args:
        directory (str): The path to the directory containing text files.
    Returns:
        list[dict]: A list of dictionaries, each containing 'id', 'text', and 'metadata'.

    Raises:
        FileNotFoundError: If directory does not exist.
        NotADirectoryError: If path exists but is not a directory.
    """

    def load_documents(self, directory: str) -> list[dict]:
        documents = []
        path = Path(directory)

        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")
        if not path.is_dir():
            raise NotADirectoryError(f"Not a directory: {directory}")

        for filepath in path.glob("*.txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read().strip()
            if text:
                documents.append(
                    {"id": filepath.stem, "text": text, "metadata": {"filename": filepath.name}}
                )
        return documents


class DocumentChunker:
    """Chunk documents into smaller pieces for better retrieval."""

    def __init__(self, chunk_size: int = 300, overlap: int = 30):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be > 0")
        if overlap < 0:
            raise ValueError("overlap must be >= 0")
        if overlap >= chunk_size:
            raise ValueError("overlap must be < chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str, doc_id: str) -> list[dict]:
        """Split the given text into overlapping chunks."""
        words = text.split()  # pull out words from text

        if len(words) <= self.chunk_size:
            return [
                {
                    "id": f"{doc_id}_0",
                    "text": text,
                    "metadata": {
                        "chunk": 0,
                        "doc_id": doc_id,
                    },
                }
            ]

        chunks, start, chunk_num = [], 0, 0

        while start < len(words):
            end = start + self.chunk_size
            chunk_text = " ".join(words[start:end])

            chunks.append(
                {
                    "id": f"{doc_id}_{chunk_num}",
                    "text": chunk_text,
                    "metadata": {
                        "chunk": chunk_num,
                        "doc_id": doc_id,
                    },
                }
            )

            start = end - self.overlap
            chunk_num += 1

        return chunks
