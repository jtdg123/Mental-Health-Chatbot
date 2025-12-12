from flask import Flask, render_template, request, jsonify
from nlp_utils import analyze_message, generate_reply
import nltk

# Ensure VADER dependencies
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    message = data["message"]
    analysis = analyze_message(message)
    reply = generate_reply(message, analysis)

    return jsonify({"reply": reply, "analysis": analysis})

if __name__ == "__main__":
    app.run(debug=True)
