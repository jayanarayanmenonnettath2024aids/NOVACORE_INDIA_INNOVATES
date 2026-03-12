import numpy as np
from typing import List, Union
from loguru import logger

class EmbeddingGenerator:
    """
    Simulates a Vector Embedding model (e.g., Sentence-BERT) for semantic search.
    """
    def __init__(self, model_path: str, dimension: int = 384):
        self.model_path = model_path
        self.dimension = dimension
        logger.info(f"EmbeddingGenerator initialized (Dim: {dimension})")

    def generate(self, text: str) -> List[float]:
        """
        Generates a normalized embedding vector for the given text.
        """
        # Production simulation using numpy for deterministic but mock values
        # We seed with the hash of the text to get consistent mock vectors
        np.random.seed(abs(hash(text)) % (10**8))
        vector = np.random.randn(self.dimension)
        normalized_vector = vector / np.linalg.norm(vector)
        return normalized_vector.tolist()

    def calculate_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """
        Calculates cosine similarity between two vectors.
        """
        a = np.array(vec1)
        b = np.array(vec2)
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

embedding_gen = EmbeddingGenerator("assets/models/embedding_model.bin")
