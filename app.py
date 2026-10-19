from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the This App, This means it is running!</h1>"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)