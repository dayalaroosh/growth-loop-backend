# app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

# Load environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Health check
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

# Main endpoint
@app.route("/generate-loops", methods=["POST"])
def generate_loops():
    data = request.get_json()
    idea = data.get("idea")

    if not idea:
        return jsonify({"error": "Missing 'idea' in request"}), 400

    try:
        # GPT-4 prompt setup
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a startup growth strategist. Based on the product idea provided, generate 4 types of growth loops: "
                    "1) Viral loop, 2) Content loop, 3) Retention loop, 4) Paid loop. "
                    "Respond in structured markdown format."
                )
            },
            {
                "role": "user",
                "content": f"My product idea is: {idea}"
            }
        ]

        # Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )

        reply = response.choices[0].message.content
        return jsonify({"growth_loops": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
