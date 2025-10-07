import json
import pathlib
from typing import List, Tuple, Optional, Union

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQIndex:
    """
    Tiny TF-IDF FAQ retriever.
    """

    def __init__(
        self,
        faq_path: Union[str, pathlib.Path],
        min_score: float = 0.35,
        top_n: int = 3,
    ):
        self.faq_path = pathlib.Path(faq_path)
        self.min_score = float(min_score)
        self.top_n = int(top_n)

        data = json.loads(self.faq_path.read_text(encoding="utf-8"))
        # Keep simple arrays for vectorization
        self.questions: List[str] = [row["question"] for row in data]
        self.answers: List[str] = [row["answer"] for row in data]

        # Build TF-IDF index on questions
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.q_matrix = self.vectorizer.fit_transform(self.questions)

    def search(self, query: str) -> Optional[Tuple[str, str, float]]:
        """
        Return (matched_question, answer, score) or None if below threshold.
        """
        if not query or not query.strip():
            return None
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.q_matrix)[0]

        best_idx = int(sims.argmax())
        best_score = float(sims[best_idx])

        if best_score < self.min_score:
            return None

        return self.questions[best_idx], self.answers[best_idx], best_score

    # Optional alias so app.py can call query(...)
    def query(self, query: str) -> Optional[Tuple[str, str, float]]:
        return self.search(query)