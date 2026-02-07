from retrieval.embeddings import DocumentEmbedder
from retrieval.loader import DocumentChunker, DocumentLoader
from retrieval.store import VectorStore


class DocumentRetriever:
    """High-level interface for document retrieval."""

    def __init__(self, chunk_size: int = 300, overlap: int = 30):
        """Initialize retriever with default components."""
        chunker = DocumentChunker(chunk_size=chunk_size, overlap=overlap)
        self.loader = DocumentLoader(chunker=chunker)
        self.store = VectorStore(DocumentEmbedder())
        self._indexed = False  # flag to indicate we've done some indexing

    def index_documents(self, directory: str):
        """
        Load and index documents from a directory.

        Args:
            directory: Path to the directory containing documents

        Returns:
            Number of documents indexed
        """
        before = self.document_count
        documents = self.loader.load_documents(directory)
        self.store.add_documents(documents)
        self._indexed = True
        return self.document_count - before

    def search(self, query: str, n_results: int = 5) -> list[dict]:
        """Search for documents relevant to the query."""
        if not self._indexed:
            raise ValueError("No documents indexed. Call index_documents() first.")
        return self.store.search(query, n_results)

    @property
    def document_count(self) -> int:
        """Return the number of indexed documents."""
        return self.store.count()
