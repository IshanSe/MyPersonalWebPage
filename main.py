from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/content')
def content():
    return send_from_directory('.', 'content.html')

@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory('.', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)