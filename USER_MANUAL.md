🅒 USER MANUAL
------------------------------------------------------------

Below is a clean and ready-to-submit USER_MANUAL.md.

USER MANUAL — Mental Health Chatbot
1. Overview

The Mental Health Chatbot is a web-based conversational agent that uses:

Natural Language Processing (NLP)

Sentiment Analysis (VADER)

Intent detection

Safety response logic

The system provides supportive, non-clinical emotional assistance.

2. System Requirements
Software

Python 3.8+

pip (Python package manager)

Python Libraries

Install using:

pip install -r requirements.txt

3. How to Run the Program
Step 1 — Download or extract the project folder
mental_health_chatbot/

Step 2 — Install required libraries
pip install -r requirements.txt

Step 3 — Run the chatbot
python app.py

Step 4 — Access the chatbot

Open a browser and go to:

http://127.0.0.1:5000


You will see the chat interface.

4. How to Use the Chatbot

Type a message such as:

“I feel sad today”

“Hello”

“I feel stressed”

Click Send.

The chatbot will:

Analyze message sentiment

Detect intents (greeting, anxiety, crisis, etc.)

Respond with supportive messages

Provide crisis hotline info if needed

5. Safety Features

If the user expresses suicidal intent, the bot provides:

Emergency contact instructions

988 Suicide & Crisis Lifeline (U.S.)

Compassionate acknowledgment

6. File Descriptions
File	Purpose
app.py	Flask backend server
nlp_utils.py	NLP + sentiment + intent detection logic
templates/index.html	Chat UI interface
static/chat.js	Front-end chat behavior
requirements.txt	Required libraries
USER_MANUAL.md	User documentation
