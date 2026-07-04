import pickle
import re
import string
from nltk.corpus import stopwords

# Load model
with open("../models/fake_news_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load vectorizer
with open("../models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

def predict_news(news):
    cleaned = clean_text(news)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)

    if prediction[0] == 0:
        return "Fake News ❌"
    else:
        return "True News ✅"