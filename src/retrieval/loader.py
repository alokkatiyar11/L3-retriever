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
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read().strip()
            if text:
                documents.append({
                    'id': filepath.stem,
                    'text': text,
                    'metadata': {'filename': filepath.name}
                })
        return documents