from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY_HERE"

chat_history = []

@app.route("/", methods=["GET", "POST"])
def chat():
    global chat_history

    if request.method == "POST":
        user = request.form["user_input"]

        chat_history.append({"role": "user", "content": user})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=chat_history
            )

            reply = response.choices[0].message["content"]

            chat_history.append({"role": "assistant", "content": reply})

        except Exception as e:
            reply = "Error: " + str(e)

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)