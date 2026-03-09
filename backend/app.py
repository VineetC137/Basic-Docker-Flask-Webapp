from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import random
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

quotes = [
    "Small steps every day lead to big results.",
    "Code is like humor. When you have to explain it, it's bad.",
    "First solve the problem, then write the code.",
    "Dream big. Start small. Act now.",
    "Consistency beats talent when talent doesn't work hard.",
    "The best time to plant a tree was 20 years ago. The second best time is now.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Innovation distinguishes between a leader and a follower."
]

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def get_data():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    quote = random.choice(quotes)
    
    return jsonify({
        'time': current_time,
        'date': current_date,
        'quote': quote,
        'status': 'success'
    })

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Flask Docker Application',
        'timestamp': datetime.datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
