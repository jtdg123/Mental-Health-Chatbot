Mental Health Chatbot — User Manual
1. Overview

The Mental Health Chatbot is a web-based conversational system designed to provide supportive, non-clinical mental health assistance. It uses:

Natural Language Processing (NLP)

Sentiment Analysis (VADER)

Intent Detection

Safety Response Logic

The system runs on a lightweight Flask server and interacts with users through a simple web interface.

2. Features
✔ Sentiment analysis

Detects emotional tone (positive, neutral, negative, very negative).

✔ Intent detection

Recognizes categories such as:

Greeting

Anxiety

Depression

Crisis / Suicide alerts

Farewells

✔ Supportive conversation

Provides empathetic responses and optional coping strategies.

✔ Crisis safety response

If the user expresses intent to self-harm, the chatbot shows emergency hotline resources.

3. System Requirements
Hardware

Any computer capable of running Python 3.

Software

Python 3.8 or higher

pip (Python package manager)

Web browser (Chrome, Firefox, Edge, etc.)

Python Libraries

Installed automatically using:

pip install -r requirements.txt

4. Installation Instructions
Step 1 — Download the Project

Download or clone the repository:

git clone https://github.com/YOUR_USERNAME/mental_health_chatbot.git


Or download the ZIP and extract it.

Step 2 — Install Required Python Libraries

Navigate to the project folder:

cd mental_health_chatbot


Install all dependencies:

pip install -r requirements.txt


This installs Flask and NLTK sentiment tools.

Step 3 — Download NLTK Resources (Automatic)

The program automatically downloads the vader_lexicon if not found.

No extra steps needed.

5. How to Run the Application

Run the Flask app:

python app.py


If the server runs correctly, you will see something like:

Running on http://127.0.0.1:5000/

Access the chatbot

Open your web browser and go to:

http://127.0.0.1:5000


You will now see the chatbot interface.

6. How to Use the Chatbot

Type a message in the input box — for example:

"I feel stressed today"

"Hello"

"I'm really anxious about school"

Click Send.

The chatbot will:

Analyze your sentiment

Detect intents

Choose an appropriate response

Display the analysis and reply

7. Safety Features

The chatbot includes crisis detection for phrases containing:

“suicide”

“kill myself”

“end my life”

“I want to die”

If detected, the bot provides:

Crisis hotline resources

Calm, supportive language

A reminder to seek immediate help

This chatbot is not a replacement for professional mental health care.

8. Project File Structure
mental_health_chatbot/
│
├── app.py
├── nlp_utils.py
├── requirements.txt
├── USER_MANUAL.md
│
├── templates/
│   └── index.html
│
└── static/
    └── chat.js

File Purpose
File	Description
app.py	Main Flask server; routes and API logic
nlp_utils.py	Sentiment analysis + intent detection + response generation
requirements.txt	Required Python libraries (Flask, nltk)
templates/index.html	Chat UI layout
static/chat.js	Browser-side chat logic
USER_MANUAL.md	User documentation
9. Known Limitations

Not a clinical mental health tool

Not trained on medical datasets

Cannot replace professional therapy

Uses simple rule-based intent detection

10. Future Improvements (Optional)

Add transformer-based sentiment models (BERT, RoBERTa)

Add database for chat history

Add emotion classification (anger, fear, joy, sadness)

Add voice input/output
