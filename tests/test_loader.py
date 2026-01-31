"""
Lab 3 FastAPI API.
@author: Aarti Dashore, Alok Katiyar
Seattle University, ARIN 5360
@see: https://catalog.seattleu.edu/preview_course_nopop.php?catoid=55&coid
=190380
@version: 0.1.0+w26

Unit tests for DocumentLoader.

These tests validate that DocumentLoader.load_documents:
- Loads only .txt files in a directory
- Skips empty/whitespace-only files
- Returns the expected schema for each document
- Behaves correctly for empty or non-existent directories

"""

from __future__ import annotations

from pathlib import Path

import pytest

from src.retrieval.loader import DocumentLoader


@pytest.fixture
def loader() -> DocumentLoader:
    """
    Provide a fresh DocumentLoader instance for each test.
    """
    return DocumentLoader()


def test_loader_loads_documents(tmp_path):
    """Test loading documents from a directory."""
    # create some test files
    (tmp_path / "file1.txt").write_text("This is a test file")
    (tmp_path / "file2.txt").write_text("This is another test file")

    loader = DocumentLoader()
    docs = loader.load_documents(str(tmp_path))

    assert len(docs) == 2
    assert all("id" in doc and "text" in doc and "metadata" in doc for doc in docs)


def _write_file(path: Path, content: str, encoding: str = "utf-8") -> None:
    """
    Helper to create a text file with given content.
    """
    path.write_text(content, encoding=encoding)


def test_returns_empty_list_for_empty_directory(tmp_path: Path, loader: DocumentLoader) -> None:
    """
    If the directory contains no .txt files, load_documents should return an empty list.
    """
    docs = loader.load_documents(str(tmp_path))
    assert docs == []


def test_loads_single_text_file(tmp_path: Path, loader: DocumentLoader) -> None:
    """
    A single .txt file should be loaded and returned as one document with correct schema.
    """
    _write_file(tmp_path / "a.txt", "hello world")

    docs = loader.load_documents(str(tmp_path))

    assert len(docs) == 1
    doc = docs[0]

    assert doc["id"] == "a"
    assert doc["text"] == "hello world"
    assert doc["metadata"]["filename"] == "a.txt"


def test_ignores_non_txt_files(tmp_path: Path, loader: DocumentLoader) -> None:
    """
    Files that do not end with .txt should be ignored.
    """
    _write_file(tmp_path / "a.txt", "hello")
    _write_file(tmp_path / "b.md", "should not load")
    _write_file(tmp_path / "c.json", '{"x": 1}')

    docs = loader.load_documents(str(tmp_path))

    assert len(docs) == 1
    assert docs[0]["id"] == "a"


def test_skips_empty_files(tmp_path: Path, loader: DocumentLoader) -> None:
    """
    Empty .txt files should be skipped (because text becomes empty after .strip()).
    """
    _write_file(tmp_path / "empty.txt", "")
    _write_file(tmp_path / "spaces.txt", "   \n\t  ")
    _write_file(tmp_path / "valid.txt", "content")

    docs = loader.load_documents(str(tmp_path))

    assert len(docs) == 1
    assert docs[0]["id"] == "valid"
    assert docs[0]["text"] == "content"


def test_loads_multiple_text_files(tmp_path: Path, loader: DocumentLoader) -> None:
    """
    Multiple .txt files should be loaded. The order is not guaranteed by glob(),
    so we compare by ids.
    """
    _write_file(tmp_path / "one.txt", "first")
    _write_file(tmp_path / "two.txt", "second")
    _write_file(tmp_path / "three.txt", "third")

    docs = loader.load_documents(str(tmp_path))
    ids = {d["id"] for d in docs}

    assert ids == {"one", "two", "three"}

    # Validate schema for each document
    for d in docs:
        assert set(d.keys()) == {"id", "text", "metadata"}
        assert "filename" in d["metadata"]
        assert d["metadata"]["filename"] == f"{d['id']}.txt"
        assert isinstance(d["text"], str) and d["text"].strip() != ""


def test_raises_for_nonexistent_directory(loader: DocumentLoader) -> None:
    """
    Current implementation will raise when directory doesn't exist because Path.glob()
    on a non-existent directory effectively yields nothing BUT open() will never run.
    However, behavior can depend on OS/path.

    This test enforces a clearer behavior: if directory doesn't exist, raise FileNotFoundError.

    If you DON'T want this behavior, remove this test or update your loader.
    """
    with pytest.raises(FileNotFoundError):
        loader.load_documents("/this/path/should/not/exist")


def test_raises_not_a_directory_error(tmp_path, loader):
    """
    Passing a file path instead of a directory should raise NotADirectoryError.
    """
    # Create a regular file
    file_path = tmp_path / "not_a_dir.txt"
    file_path.write_text("I am a file, not a directory")

    # Attempt to load documents using the file path
    with pytest.raises(NotADirectoryError):
        loader.load_documents(str(file_path))
