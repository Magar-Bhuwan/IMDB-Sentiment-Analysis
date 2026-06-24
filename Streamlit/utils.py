import re
import joblib
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

BASE_DIR = Path(__file__).resolve().parent

LABELS = {
    0: "Negative",
    1: "Positive"
}


class SentimentAnalyser:
    def __init__(self, model_path, vector_path):
        self.model_path = Path(model_path)
        self.vector_path = Path(vector_path)

        # Load once during initialization
        self.classifier = self.read_joblib_file(self.model_path)
        self.vectorizer = self.read_joblib_file(self.vector_path)

    def text_processor(self, text):
        text = text.lower()

        # Remove HTML tags
        text = re.sub(r"<.+?>", "", text)

        # Remove URLs
        text = re.sub(r"(https?:\/\/\S+)|(www\.\S+)", "", text)

        # Remove punctuation
        text = re.sub(r"[^\w\s]", " ", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        # Remove stopwords
        words = [
            word
            for word in text.split()
            if word not in ENGLISH_STOP_WORDS and len(word) > 1
        ]

        return " ".join(words)

    def read_joblib_file(self, file_path):
        try:
            return joblib.load(file_path)
        except Exception as e:
            raise RuntimeError(
                f"Failed to load file: {file_path}\nError: {e}"
            )

    def get_embeddings(self, tokens, model):
        """
        Works for:
        - Gensim Word2Vec model
        - KeyedVectors
        """

        # If a full Word2Vec model was loaded
        if hasattr(model, "wv"):
            model = model.wv

        vectors = [
            model[word]
            for word in tokens
            if word in model
        ]

        if not vectors:
            return np.zeros(model.vector_size)

        return np.mean(vectors, axis=0)

    def prediction_pipeline(self, user_input):
        cleaned_text = self.text_processor(user_input)

        vector = self.get_embeddings(
            cleaned_text.split(),
            self.vectorizer
        )

        prediction = self.classifier.predict(
            vector.reshape(1, -1)
        )

        return LABELS.get(prediction[0], "Unknown")


if __name__ == "__main__":
    predictor = SentimentAnalyser(
        model_path=BASE_DIR / "IMDB" / "SVM_model.joblib",
        vector_path=BASE_DIR / "IMDB" / "Word2Vec_imdb_250.joblib"
    )

    result = predictor.prediction_pipeline(
        user_input="This movie was amazing. Great acting and story!"
    )

    print(result)