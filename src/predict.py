import os
import pickle
import re
import string
from nltk.corpus import stopwords

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
model_path = os.path.join(BASE_DIR, "models", "fake_news_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# Load model
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Load vectorizer
with open(vectorizer_path, "rb") as file:
    vectorizer = pickle.load(file)

stop_words = set(stopwords.words("english"))