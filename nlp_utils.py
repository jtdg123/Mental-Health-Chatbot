import re
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

INTENT_PATTERNS = {
    "greeting": [r"hi", r"hello", r"hey", r"good (morning|afternoon|evening)"],
    "bye": [r"bye", r"goodbye", r"see you", r"farewell"],
    "suicide": [r"suicid", r"kill myself", r"end my life", r"i want to die"],
    "depressed": [r"depress", r"sad", r"feeling down", r"lonely", r"worthless"],
    "anxiety": [r"anxi", r"nervous", r"panic", r"worried", r"stressed"],
    "help": [r"help", r"need someone", r"can you help", r"advice"],
}

RESOURCE_SUGGESTIONS = {
    "suicide": [
        "If you are in immediate danger, call your local emergency number right now.",
        "In the U.S. you can call or text 988 to reach the Suicide & Crisis Lifeline."
    ],
    "default": [
        "Consider reaching out to a trusted friend, family member, or a mental health professional.",
        "If you want, I can provide breathing exercises or grounding techniques."
    ]
}

def detect_intents(text):
    text_l = text.lower()
    intents = []
    for intent, patterns in INTENT_PATTERNS.items():
        for p in patterns:
            if re.search(p, text_l):
                intents.append(intent)
                break
    return intents

def analyze_message(text):
    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound <= -0.5:
        sentiment = "very_negative"
    elif compound < -0.05:
        sentiment = "negative"
    elif compound <= 0.05:
        sentiment = "neutral"
    elif compound < 0.5:
        sentiment = "positive"
    else:
        sentiment = "very_positive"

    intents = detect_intents(text)
    return {"sentiment": sentiment, "scores": scores, "intents": intents}

def generate_reply(text, analysis):
    intents = analysis["intents"]
    sentiment = analysis["sentiment"]

    if "suicide" in intents or "suicid" in text.lower():
        return "\n\n".join([
            "I'm really sorry you're feeling this way. You might be in immediate danger — please call your local emergency number or a crisis line right now.",
            *RESOURCE_SUGGESTIONS["suicide"]
        ])

    if sentiment in ("very_negative", "negative") or any(i in intents for i in ("depressed", "anxiety")):
        base = [
            "I'm sorry you're going through that — it sounds really difficult.",
            "If you'd like, I can try a short grounding exercise or breathing exercise, or provide resources.",
            "Would you like a breathing exercise, resources, or to tell me more?"
        ]
        base.extend(RESOURCE_SUGGESTIONS["default"])
        return "\n\n".join(base)

    if "greeting" in intents:
        return "Hello! I'm here to listen. How are you feeling today?"

    if "bye" in intents:
        return "Take care. If you need anything else, I'm here."

    if sentiment in ("neutral", "positive", "very_positive"):
        return "Thanks for sharing — tell me more if you'd like. I'm listening."

    return "I hear you. Can you tell me a bit more about that?"
