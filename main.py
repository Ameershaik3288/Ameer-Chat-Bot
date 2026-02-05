from flask import Flask, request , render_template
from google import genai

client = genai.Client(api_key="Your API KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.json["msg"],
    ).text

app.run(port=5000)
