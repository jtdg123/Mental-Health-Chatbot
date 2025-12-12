# 🧠 Mental Health Chatbot  
A Natural Language Processing (NLP) and Machine-Learning Powered Mental Health Detection & Support System  
Built with **Flask**, **NLTK**, **Scikit-Learn**, and **sentiment analysis**

---

## 📘 Overview

This project implements an **Intelligent Mental Health Chatbot** that can:

- Detect emotional states such as **anxiety**, **depression**, **stress**, and **loneliness**
- Assess emotional **severity** using VADER **sentiment analysis**
- Predict mental-health categories using a **trained TF-IDF + Logistic Regression model**
- Identify **crisis-related statements** (e.g., self-harm ideation)
- Provide supportive, therapeutic-style responses and coping steps
- Log all chat interactions with timestamps
- Run in a simple **web interface** powered by Flask

This is designed as part of a research project and DOES NOT replace professional help.  
If someone is in crisis, the bot provides the **988 Suicide & Crisis Lifeline**.

---

## 📁 Project Structure
Mental-Health-Chatbot/
│
├── app.py
├── nlp_utils.py
├── train_model.py
├── requirements.txt
│
├── models/
│ ├── vectorizer.pkl
│ └── classifier.pkl
│
├── templates/
│ └── index.html
│
└── static/
├── style.css
└── script.js


---

## 🛠️ Installation Instructions

Follow these steps to run the chatbot on your local machine.

---

### **1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/Mental-Health-Chatbot
cd Mental-Health-Chatbot
```
---

### **2. Create a Virtual Environment**

Windows (PowerShell):
```
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

If PowerShell blocks activation:

Set-ExecutionPolicy -Scope CurrentUser Unrestricted
---
### 3. **Install Dependencies**
```
pip install -r requirements.txt
```

Download the VADER lexicon:

python
```
>>> import nltk
>>> nltk.download('vader_lexicon')
>>> exit()
```
🤖 Training the Machine Learning Model

Run this script once to generate:

models/vectorizer.pkl

models/classifier.pkl

```
python train_model.py
```

After training, you should see:
```
Model training complete. Files saved in /models/
```

You can replace the example dataset in train_model.py with your own CSV or expanded dataset.

🚀 Running the Chatbot

Start the Flask server:
```
python app.py
```

Open your browser:
```
http://127.0.0.1:5000
```

You will see the chatbot interface where you can type messages and receive AI-powered responses.
---
🧠 How the Chatbot Works
## **1. ML Model Prediction**

A TF-IDF vectorizer converts text into numeric features

Logistic Regression predicts anxiety, depression, or stress

## **2. Sentiment Analysis**

VADER sentiment analyzer evaluates:

positivity

negativity

neutrality

compound score

Used to classify:

mild

moderate

severe emotional intensity

## **3. Keyword Safety Net**

Keyword matching identifies:

loneliness cues

burnout indicators

crisis phrases

## **4. Crisis Detection**

If suicide-related phrases appear, the bot responds with:

If you're in danger, please contact 988 immediately.

## **5. Coping Strategy Generator**

Each category (stress, anxiety, depression, etc.) has a set of professionally-informed coping suggestions.

📊 Model Performance (Example Results)

These metrics were generated from the initial training dataset:

Class	F1 Score
Anxiety	0.8975
Depression	0.8882
Stress	0.8972

Training Accuracy: 93%
Validation Accuracy: 90%

Graphs and confusion matrices are included in the paper and presentation.

# 📄 Research Paper + Presentation

This project includes:

IEEE-format research paper

10-minute research presentation (PPTX)

Training logs and model graphs

Available in the repository under docs/ (optional).

# ⚠️ Disclaimer

This chatbot is NOT a medical or therapeutic substitute.
It is for educational and research purposes only.
If someone is in immediate danger, they should dial:

988 — Suicide & Crisis Lifeline
# 🙌 Credits

Developed by:
Jericho Gutlay
Georgia State University
Department of Computer Science

# ⭐ Want to Improve This Project?

Here are optional enhancements:

Add a real mental-health dataset (Kaggle, Reddit, Twitter, etc.)

Expand categories (bipolar, PTSD, grief)

Replace ML model with BERT, RoBERTa, or DistilBERT

Add chatbot memory & multi-turn context

Deploy to a public server (Render, Heroku, etc.)

# 📬 Contact

# For academic or technical questions:
📧 jgutlay1@gsu.edu
