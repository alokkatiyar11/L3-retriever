"""
Lab 3 FastAPI API.
@author: Aarti Dashore, Alok Katiyar
Seattle University, ARIN 5360
@see: https://catalog.seattleu.edu/preview_course_nopop.php?catoid=55&coid
=190380
@version: 0.1.0+w26
"""
from pathlib import Path


class DocumentLoader:
    """
    Docstring for DocumentLoader
    Load all the text document from the directory
    Args:
        directory (str): The path to the directory containing text files.
    Returns:
        list[dict]: A list of dictionaries, each containing 'id', 'text', and 'metadata'.

    """
    def load_documents(self, directory: str) -> list[dict]:
        documents = []
        path = Path(directory)
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