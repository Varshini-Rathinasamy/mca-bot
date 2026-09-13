from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    if "hello" in user_input.lower():
        reply = "Hi 👋! How can I help you?"
    else:
        reply = "I got your message: " + user_input

    return jsonify({"reply": reply})