# Growth Loop Generator (Flask API)

A lightweight backend for generating tailored growth loops using GPT-4. Can be used with Typedream, Typebot, Framer, or any frontend that supports API calls.

### 🚀 Endpoint

**POST /generate-loops**

Example body:
```json
{
  "idea": "An AI assistant that writes job descriptions for hiring managers"
}
```

### 🛠 Tech Stack

- Flask (API server)
- OpenAI GPT-4 (growth loop logic)
- Render (deployment)
- Streamlit (optional focus group simulator)

👉 Check `focus_group_url` field in the response to run validation via multi-agent discussion.
