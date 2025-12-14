from flask import Flask, render_template, request, jsonify
from nlp_utils import analyze_message, generate_reply

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']

    analysis = analyze_message(message)
    reply = generate_reply(message, analysis)

    return jsonify({'reply': reply, 'analysis': analysis})

if __name__ == "__main__":
    app.run(debug=True)
