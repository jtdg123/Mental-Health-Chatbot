from flask import Flask, render_template, request, jsonify
from nlp_utils import analyze_message, generate_reply
import nltk

# ensure vader lexicon is available
try:
    from nltk.sentiment import SentimentIntensityAnalyzer
except Exception:
    nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    message = data['message']
    analysis = analyze_message(message)
    reply = generate_reply(message, analysis)

    response = {
        'reply': reply,
        'analysis': analysis
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
