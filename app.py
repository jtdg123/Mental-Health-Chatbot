from flask import Flask, render_template, request, jsonify
from nlp_utils import analyze_message, generate_reply
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error":"No message provided"}), 400
    message = data["message"]
    analysis = analyze_message(message)
    reply = generate_reply(message, analysis)
    return jsonify({"reply": reply, "analysis": analysis})

if __name__ == "__main__":
    app.run(debug=True)
