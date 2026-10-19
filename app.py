from flask import Flask, jsonify
from redis import Redis

app = Flask(__name__)

db = Redis(host='redis-db', port=6379, decode_responses=True)

@app.route('/')
def home():
    visitors = db.incr('visitor_count')
    return f"<h1>Welcome to the This App, This means it is running!</h1><p>This page has been visited {visitors} times.</p>"

@app.route('/health')
def health():
    try:
        db.ping()
        return jsonify(status='healthy', database='connected'), 200
    except Exception as e:
        return jsonify(status='unhealthy', error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)