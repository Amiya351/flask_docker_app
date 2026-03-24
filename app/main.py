# app/main.py
import os
from flask import Flask, render_template
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default_key")

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=debug_mode)