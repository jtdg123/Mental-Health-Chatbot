# 🧠 Mental Health Chatbot

A lightweight Flask-based chatbot that uses NLP techniques to classify user messages into mental-health-related categories and provide supportive, non-clinical responses.

## 📁 Project Structure
```
mental_health_chatbot/
│
├── app.py
├── nlp_utils.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── chat.js
│
└── USER_MANUAL.md
```

## 🚀 Features
- Simple and clean web UI (HTML + JS)
- Flask backend serving a /chat endpoint
- NLP preprocessing (tokenization, stopword removal, lemmatization)
- Basic intent classification (stress, anxiety, sadness, anger, neutral)
- Supportive, safe responses (NOT a medical tool)
- Easy to deploy locally or on platforms like Render/Heroku

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/mental_health_chatbot.git
cd mental_health_chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app
```bash
python app.py
```

### 4. Open in your browser
```
http://127.0.0.1:5000/
```

## 🧩 How It Works

### Frontend
- `index.html` displays the chat UI.
- `chat.js` handles sending/receiving messages.

### Backend
- `app.py` runs the Flask server.
- `nlp_utils.py` processes text & classifies messages.

## ⚠️ Disclaimer
This chatbot is not a therapist and does not provide medical advice.  
For educational demonstration only.

## 🤝 Contributions
Pull requests and issues are welcome!
