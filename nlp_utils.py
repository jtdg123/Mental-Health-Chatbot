# nlp_utils.py

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer
from datetime import datetime

# ----------------------------------------------------
# Ensure VADER Lexicon
# ----------------------------------------------------

try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()
ps = PorterStemmer()

# ----------------------------------------------------
# Chat Logging
# ----------------------------------------------------

def save_chat_log(user_msg, bot_msg):
    """Append chat messages to chat_logs.txt with timestamps."""
    with open("chat_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        f.write(f"\nUser: {user_msg}")
        f.write(f"\nBot:  {bot_msg}\n")

# ----------------------------------------------------
# Keyword Lists
# ----------------------------------------------------

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
        "self harm", "cut myself"
    ]
}

# ----------------------------------------------------
# Phrase-Level Mental Health Patterns
# ----------------------------------------------------

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

# ----------------------------------------------------
# Improved Classification
# ----------------------------------------------------

def classify_mental_health(text):
    """Weighted keyword + phrase-based mental health detection."""
    text_lower = text.lower()
    words = [ps.stem(w) for w in text_lower.split()]

    # Crisis override
    for term in MENTAL_HEALTH_KEYWORDS["crisis"]:
        if term in text_lower:
            return ["crisis"]

    # Category scoring
    scores = {cat: 0 for cat in ["depression", "anxiety", "stress", "loneliness"]}

    # ----- Keyword scoring -----
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

    # ----- Phrase patterns (strong indicators) -----
    for category, patterns in PHRASES.items():
        for p in patterns:
            if p in text_lower:
                scores[category] += 3

    # ----- Determine detected categories -----
    max_score = max(scores.values())

    if max_score == 0:
        return ["general_emotion"]

    detected = [cat for cat, score in scores.items() if score == max_score]

    return detected

# ----------------------------------------------------
# Sentiment + Severity Scoring
# ----------------------------------------------------

def analyze_message(text):
    """Run sentiment analysis and categorize severity."""
    sentiment = sia.polarity_scores(text)
    categories = classify_mental_health(text)

    compound = sentiment["compound"]

    if compound <= -0.6:
        severity = "severe"
    elif compound <= -0.2:
        severity = "moderate"
    else:
        severity = "mild"

    return {
        "sentiment": sentiment,
        "severity": severity,
        "categories": categories
    }

# ----------------------------------------------------
# Supportive Responses
# ----------------------------------------------------

STEPS = {
    "depression": [
        "1. Try grounding yourself with a simple, gentle activity.",
        "2. Choose one tiny goal for today (even very small steps count).",
        "3. Reach out to someone you trust and let them know you're struggling.",
        "4. Remind yourself that what you’re feeling is valid—you're not alone."
    ],
    "anxiety": [
        "1. Take three slow, deep breaths.",
        "2. Identify one specific thing that triggered your anxiety.",
        "3. Remind yourself: this feeling will pass.",
        "4. Try a 5–4–3–2–1 grounding exercise."
    ],
    "stress": [
        "1. Identify the main source of pressure right now.",
        "2. Break the problem into smaller, manageable steps.",
        "3. Give yourself permission to rest—your body needs it.",
        "4. Reset with 60 seconds of slow breathing."
    ],
    "loneliness": [
        "1. Acknowledge how you're feeling—it’s okay to feel this way.",
        "2. Reach out to someone, even with a small message.",
        "3. Try doing one small activity you normally enjoy.",
        "4. Join an online or local community related to your interests."
    ]
}

# ----------------------------------------------------
# Response Generator
# ----------------------------------------------------

def generate_reply(user_text, analysis):
    categories = analysis["categories"]
    severity = analysis["severity"]

    # Crisis Handling
    if "crisis" in categories:
        response = (
            "I'm really sorry you're feeling like this. You are not alone.\n\n"
            "If you're thinking about harming yourself or are in danger, "
            "please contact **988** (Suicide & Crisis Lifeline) right now.\n"
            "You deserve safety and support."
        )
        save_chat_log(user_text, response)
        return response

    # Category Responses
    for category in ["depression", "anxiety", "stress", "loneliness"]:
        if category in categories:
            steps = "\n".join(STEPS[category])
            response = (
                f"It sounds like you may be experiencing **{category}**, "
                f"with a **{severity}** level of emotional intensity.\n\n"
                "Here are a few steps that might help:\n"
                f"{steps}\n\n"
                "I'm here for you. What part feels the hardest right now?"
            )
            save_chat_log(user_text, response)
            return response

    # General fallback
    compound = analysis["sentiment"]["compound"]
    if compound <= -0.4:
        response = (
            "It sounds like something upsetting might be happening. "
            "I'm here to talk through it with you.\n\n"
            "What feels the most difficult right now?"
        )
    elif compound >= 0.4:
        response = (
            "It sounds like something positive is going on! "
            "I'd love to hear more about what's been going well."
        )
    else:
        response = (
            "I hear you. I'm here to support you through whatever you're feeling. "
            "What's been on your mind lately?"
        )

    save_chat_log(user_text, response)
    return response

# ----------------------------------------------------
# Main Chat Function
# ----------------------------------------------------

def chat(user_text):
    analysis = analyze_message(user_text)
    response = generate_reply(user_text, analysis)
    return response
