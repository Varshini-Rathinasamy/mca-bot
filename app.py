from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message").lower()

    if "hello" in user_input:
        reply = "Hi 👋! How can I help you?"
    elif "your name" in user_input:
        reply = "I am MCA Chatbot 🤖"
    elif "course" in user_input:
        reply = "This chatbot is for MCA students"
    else:
        reply = "Sorry, I don't understand 😅"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()