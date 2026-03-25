from flask import Flask, request, jsonify
from flask import send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

import os
API_KEY = os.getenv("DEEPL_API_KEY")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")
def translate(text, target_lang):
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {API_KEY}"
    }

    data = {
        "text": text,
        "target_lang": target_lang
    }
    res = requests.post(url, headers=headers, data=data)
    print(res.text)
    return res.json()["translations"][0]["text"]

def make_example(text):
    return f"This is an example sentence using '{text}'."

@app.route("/translate", methods=["POST"])
def translate_api():
    text = request.json["text"]
    en = translate(text, "EN")
    de = translate(text, "DE")

    return jsonify({
        "english": en,
        "german": de,
        "example": make_example(en)
    })
def translate_api():
    text = request.json["text"]
    en = translate(text, "EN")
    de = translate(text, "DE")

    return jsonify({
    "english": en,
    "german": de,
    "example": make_example(en)
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
