from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Lain's /chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Lain."},
                {"role": "user", "content": user_message}
            ]
        )
        return jsonify({"reply": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Optional root route for testing
@app.route("/")
def root():
    return "Lain backend online."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
