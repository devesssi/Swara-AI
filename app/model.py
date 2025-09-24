import os
import pickle
import random

import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'svr_sentiment_model.pkl')

class SentimentModel:
    def __init__(self):
        with open(MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)
        # If you have a vectorizer or tokenizer, load it here as well

    def predict(self, text: str):
        # Example: if your model expects a list of texts
        X = [text]
        proba = self.model.predict_proba(X)[0]
        label_idx = np.argmax(proba)
        label = self.model.classes_[label_idx]
        confidence = float(proba[label_idx])
        return label, confidence

model = SentimentModel()