import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Example dataset (replace with real training data)
texts = [
    "I feel anxious about everything", 
    "I'm overwhelmed and nervous",
    "I feel depressed and hopeless",
    "Nothing makes sense anymore",
    "I'm stressed with school",
    "Too much pressure and burnout"
]

labels = [
    "anxiety",
    "anxiety",
    "depression",
    "depression",
    "stress",
    "stress"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

clf = LogisticRegression()
clf.fit(X, labels)

# Save models
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(clf, "models/classifier.pkl")

print("Model training complete. Files saved in /models/")
