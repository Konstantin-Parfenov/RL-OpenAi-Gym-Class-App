# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'location': 'Unknown', 'reward': 'Too big to fail'})

if __name__ == '__main__':
    app.run()