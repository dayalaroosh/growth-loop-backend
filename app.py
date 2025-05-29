from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_growth_loops(idea):
    prompt = f"""
You are a growth product strategist. Given the product idea below, suggest growth loops across four categories:
1. Viral Loop
2. Content Loop
3. Retention Loop
4. Paid Loop

Each loop should be 2-3 lines max and include the mechanism, trigger, and expected user behavior.

Product idea: "{idea}"
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a growth product strategist."},
                  {"role": "user", "content": prompt}],
        temperature=0.7
    )

    answer = response["choices"][0]["message"]["content"]

    return {
        "growth_loops": answer.strip(),
        "focus_group_url": "https://growth-focus-group.streamlit.app"
    }

@app.route("/generate-loops", methods=["POST"])
def generate_loops():
    data = request.get_json()
    idea = data.get("idea", "")

    if not idea.strip():
        return jsonify({"error": "Missing idea"}), 400

    result = generate_growth_loops(idea)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
