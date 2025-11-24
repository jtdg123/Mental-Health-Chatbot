# 🧠 Mental Health Chatbot

A lightweight Flask-based chatbot that uses NLP techniques to classify user messages into mental-health-related categories and provide supportive, non-clinical responses.

---

## 📁 Project Structure

```
mental_health_chatbot/
│
├── app.py
├── nlp_utils.py
├── requirements.txt
├── README.md
├── USER_MANUAL.md
│
├── templates/
│   └── index.html
│
└── static/
    └── chat.js
```

---

## 🚀 Features

- Simple web UI (HTML + JS)
- Flask backend with `/chat` endpoint
- Sentiment analysis using NLTK VADER
- Simple intent detection (greeting, anxiety, depression, suicide-related phrases)
- Supportive, safety-first responses (educational/demo only)

---

## 🔧 Step-by-Step Tutorial (Quick Start)

Follow the steps below to get the chatbot running locally and to test it.

> **Prerequisites:** Python 3.8+ installed and `pip` available.

### 1. Clone the repository (or upload files)

```bash
git clone https://github.com/jtdg123/mental_health_chatbot.git
cd mental_health_chatbot
```

If you don't use Git, just upload the project folder with the structure above.

---

### 2. Create and activate a Python virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

**Windows (cmd.exe):**
```cmd
python -m venv venv
venv\Scriptsctivate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your prompt when the venv is active.

---

### 3. Install project dependencies

From the project root (where `requirements.txt` is):

```bash
pip install -r requirements.txt
```

`requirements.txt` contains:
```
Flask>=2.0
nltk>=3.6
```

---

### 4. Ensure NLTK resources are available

The application will attempt to download the `vader_lexicon` automatically if it is not present.  
If you prefer to download manually, run:

```bash
python -c "import nltk; nltk.download('vader_lexicon')"
```

---

### 5. Run the Flask app

```bash
python app.py
```

The app will start at:

```
http://127.0.0.1:5000/
```

---

### 6. Use the Chatbot

Open the link above in a web browser.  
Try messages like:

- “Hello”
- “I’m stressed about school”
- “I feel lonely”
- “I want to die” *(triggers crisis-safety message)*

---

## 🛠 Troubleshooting

**No module named 'flask'**  
→ Install dependencies:
```bash
pip install flask nltk
```

**NLTK VADER not found**  
→ Run:
```bash
python -c "import nltk; nltk.download('vader_lexicon')"
```

**Browser can't connect**  
→ Make sure the Flask server is still running in your terminal.

---

## 🧾 File Summary

- `app.py` — Main Flask backend  
- `nlp_utils.py` — NLP + logic  
- `templates/index.html` — UI  
- `static/chat.js` — frontend JS  
- `USER_MANUAL.md` — full guide  

---

## ⚠️ Safety Disclaimer

This chatbot is NOT a medical or therapeutic tool.  
It is for educational and demonstration purposes only.

