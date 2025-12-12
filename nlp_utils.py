# nlp_utils.py
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer
from datetime import datetime
import os

# Ensure VADER lexicon
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()
ps = PorterStemmer()

# Chat logging
def save_chat_log(user_msg, bot_msg):
    os.makedirs("logs", exist_ok=True)
    with open(os.path.join("logs", "chat_logs.txt"), "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        f.write(f"\nUser: {user_msg}")
        f.write(f"\nBot:  {bot_msg}\n")

# Keyword lists and phrases
MENTAL_HEALTH_KEYWORDS = {
    "depression": [
        "depressed", "hopeless", "worthless", "empty", "numb",
        "can't go on", "suicidal", "no point", "lifeless"
    ],
    "anxiety": [
        "anxious", "anxiety", "panic", "worried", "overwhelmed",
        "scared", "fear", "nervous", "paranoid"
    ],
    "stress": [
        "stressed", "pressure", "burned out", "burnout",
        "too much", "exhausted", "tired of everything"
    ],
    "loneliness": [
        "lonely", "alone", "isolated", "nobody", "no one cares"
    ],
    "crisis": [
        "kill myself", "hurt myself", "end it all", "suicide",
        "self harm", "cut myself", "i want to die"
    ]
}

PHRASES = {
    "depression": [
        "nothing matters", "i give up", "can't go on",
        "i feel empty", "i feel hopeless", "i hate myself",
        "i can't get out of bed", "i don't enjoy anything"
    ],
    "anxiety": [
        "my heart is racing", "i'm shaking", "i can't breathe",
        "feeling overwhelmed", "i'm panicking", "i can't calm down",
        "i feel nervous", "i feel on edge"
    ],
    "stress": [
        "too much to do", "i can't handle this", "burned out",
        "under pressure", "can't focus", "i feel overwhelmed"
    ],
    "loneliness": [
        "i feel alone", "nobody understands me",
        "no one cares", "i feel disconnected",
        "i have no one"
    ]
}

def classify_mental_health(text):
    text_lower = text.lower()
    words = [ps.stem(w) for w in text_lower.split()]

    # Crisis override
    for term in MENTAL_HEALTH_KEYWORDS["crisis"]:
        if term in text_lower:
            return {"categories":["crisis"], "scores":{"crisis":999}}

    # Category scoring
    scores = {cat: 0 for cat in ["depression", "anxiety", "stress", "loneliness"]}

    # Keyword scoring
    for category, keywords in MENTAL_HEALTH_KEYWORDS.items():
        if category == "crisis":
            continue
        for kw in keywords:
            kw_lower = kw.lower()
            kw_stem = ps.stem(kw_lower)
            if kw_lower in text_lower:
                scores[category] += 2
            elif kw_stem in words:
                scores[category] += 1
            elif any(kw_stem in ps.stem(w) for w in words):
                scores[category] += 1

    # Phrase patterns
    for category, patterns in PHRASES.items():
        for p in patterns:
            if p in text_lower:
                scores[category] += 3

    # Normalize and select
    max_score = max(scores.values())
    if max_score == 0:
        return {"categories":["general_emotion"], "scores":scores}
    detected = [cat for cat, score in scores.items() if score == max_score and score>0]
    return {"categories": detected if detected else ["general_emotion"], "scores":scores}

def analyze_message(text):
    sentiment = sia.polarity_scores(text)
    classification = classify_mental_health(text)
    compound = sentiment["compound"]
    if compound <= -0.6:
        severity = "severe"
    elif compound <= -0.2:
        severity = "moderate"
    else:
        severity = "mild"
    result = {
        "sentiment": sentiment,
        "severity": severity,
        "categories": classification["categories"],
        "scores": classification["scores"]
    }
    return result

STEPS = {
    "depression": [
        "Try grounding with a simple, gentle activity.",
        "Set one very small goal for today.",
        "Reach out to someone you trust and let them know.",
        "Remember that feelings change; you're not alone."
    ],
    "anxiety": [
        "Take three slow, deep breaths.",
        "Name five things you can see right now.",
        "Identify one specific trigger and try to reframe it.",
        "Practice a 5–4–3–2–1 grounding exercise."
    ],
    "stress": [
        "Identify the main source of pressure right now.",
        "Break the problem into smaller actionable steps.",
        "Give yourself permission to rest for a short period.",
        "Try a short breathing or stretch break."
    ],
    "loneliness": [
        "Acknowledge your feelings—they are valid.",
        "Send a short message to someone you trust.",
        "Try a small activity that you enjoy.",
        "Consider joining a community group related to your interests."
    ]
}

def generate_reply(user_text, analysis):
    categories = analysis["categories"]
    severity = analysis["severity"]
    # Crisis Handling
    if "crisis" in categories:
        response = (
            "I'm really sorry you're feeling like this. If you're in immediate danger or considering self-harm, "
            "please contact emergency services or call/text 988 (US). You deserve support and safety."
        )
        save_chat_log(user_text, response)
        return response
    # Category Responses
    for category in ["depression", "anxiety", "stress", "loneliness"]:
        if category in categories:
            steps = "\n".join(STEPS[category])
            response = (
                f"It sounds like you may be experiencing {category} with {severity} intensity.\n\n"
                f"Here are some suggestions:\n{steps}\n\n"
                "Would you like to tell me more about what's been hardest recently?"
            )
            save_chat_log(user_text, response)
            return response
    # Fallback
    compound = analysis["sentiment"]["compound"]
    if compound <= -0.4:
        response = "It sounds like something upsetting is happening. I'm here to listen. What feels most difficult?"
    elif compound >= 0.4:
        response = "That's great to hear. Tell me more about what's going well."
    else:
        response = "I hear you. Can you tell me more about that?"
    save_chat_log(user_text, response)
    return response

def chat(user_text):
    analysis = analyze_message(user_text)
    response = generate_reply(user_text, analysis)
    return response

