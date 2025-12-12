import nltk
import joblib
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer
from datetime import datetime

# Load trained ML model + vectorizer
vectorizer = joblib.load("models/vectorizer.pkl")
classifier = joblib.load("models/classifier.pkl")

# Ensure VADER
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()
ps = PorterStemmer()

# Chat log saving
def save_chat_log(user_msg, bot_msg):
    with open("chat_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        f.write(f"\nUser: {user_msg}")
        f.write(f"\nBot: {bot_msg}\n")

# Keywords
MENTAL_HEALTH_KEYWORDS = {
    "depression": ["depressed","hopeless","worthless","empty","numb","suicidal"],
    "anxiety": ["anxious","panic","worried","overwhelmed","fear","nervous"],
    "stress": ["stressed","burned out","pressure","exhausted","overloaded"],
    "loneliness": ["alone","lonely","isolated","abandoned"],
    "crisis": ["kill myself","end it","suicide","self harm","cut myself"]
}

def classify_keywords(text):
    t = text.lower()
    found = []
    for cat, words in MENTAL_HEALTH_KEYWORDS.items():
        for w in words:
            if w in t:
                found.append(cat)
                break
    if not found:
        found.append("general_emotion")
    return found

def analyze_message(text):
    sentiment = sia.polarity_scores(text)
    compound = sentiment["compound"]

    # Severity scale
    if compound <= -0.6:
        severity = "severe"
    elif compound <= -0.2:
        severity = "moderate"
    else:
        severity = "mild"

    # ML prediction
    features = vectorizer.transform([text])
    ml_prediction = classifier.predict(features)[0]

    keyword_categories = classify_keywords(text)

    return {
        "sentiment": sentiment,
        "severity": severity,
        "categories": keyword_categories,
        "ml_prediction": ml_prediction
    }

STEPS = {
    "depression": [
        "Try grounding yourself with slow breathing.",
        "Set one small goal today.",
        "Reach out to someone you trust.",
        "Your feelings are real and valid."
    ],
    "anxiety": [
        "Take three deep breaths.",
        "Identify what triggered this feeling.",
        "This feeling will pass.",
        "Try the 5–4–3–2–1 grounding exercise."
    ],
    "stress": [
        "Identify one source of pressure.",
        "Break the task into small steps.",
        "Give yourself permission to rest.",
        "Reset with slow breathing."
    ],
    "loneliness": [
        "What you're feeling is understandable.",
        "Try messaging someone close to you.",
        "Do one activity you enjoy.",
        "Join an online group for connection."
    ]
}

def generate_reply(msg, analysis):
    categories = analysis["categories"]

    if "crisis" in categories:
        reply = (
            "I'm really sorry you're feeling this way.\n"
            "If you're in danger or considering harm, please call **988** immediately.\n"
            "You deserve support and safety."
        )
        save_chat_log(msg, reply)
        return reply

    for c in ["depression","anxiety","stress","loneliness"]:
        if c in categories:
            steps = "\n".join(STEPS[c])
            reply = (
                f"It sounds like you may be experiencing **{c}**, "
                f"with emotional intensity described as **{analysis['severity']}**.\n\n"
                f"Here are some steps that might help:\n{steps}\n\n"
                "I'm here with you. What feels hardest right now?"
            )
            save_chat_log(msg, reply)
            return reply

    reply = "I hear you. Tell me more—I'm here to understand how you're feeling."
    save_chat_log(msg, reply)
    return reply

