import os
import json
from flask import Flask, request, jsonify, render_template_string
from google import genai
from google.genai import types

app = Flask(__name__)

# Load RAG Knowledge Base
with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

# Initialize Gemini Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = f"""
You are an intelligent, friendly customer service AI assistant for a premier coffee house.
Use the following Knowledge Base to answer customer inquiries, make personalized recommendations, and assist with orders:
{json.dumps(knowledge_base, indent=2)}

Guidelines:
1. Only answer based on the knowledge base provided. If an item or detail is not present, politely state that you cannot verify it.
2. Be warm, professional, and concise.
3. Suggest complementary food pairings when customers order a beverage.
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Track 1: Customer AI Assistant</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f6f9; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .chat-card { width: 100%; max-width: 600px; background: white; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.08); overflow: hidden; display: flex; flex-direction: column; height: 85vh; }
        .chat-header { background: #1a73e8; color: white; padding: 16px 20px; font-size: 18px; font-weight: 600; }
        .chat-box { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; }
        .msg { max-width: 80%; padding: 10px 14px; border-radius: 16px; font-size: 14px; line-height: 1.5; }
        .msg.user { align-self: flex-end; background: #e8f0fe; color: #1967d2; border-bottom-right-radius: 4px; }
        .msg.bot { align-self: flex-start; background: #f1f3f4; color: #202124; border-bottom-left-radius: 4px; }
        .input-row { display: flex; border-top: 1px solid #e0e0e0; padding: 12px; background: #fafafa; gap: 8px; }
        input[type="text"] { flex: 1; padding: 10px 14px; border: 1px solid #ccc; border-radius: 20px; outline: none; font-size: 14px; }
        button { background: #1a73e8; color: white; border: none; border-radius: 20px; padding: 10px 20px; font-weight: 600; cursor: pointer; }
        button:hover { background: #1557b0; }
    </style>
</head>
<body>
    <div class="chat-card">
        <div class="chat-header">☕ Coffee AI Assistant (Track 1)</div>
        <div class="chat-box" id="chatBox">
            <div class="msg bot">Hello! Welcome to our coffee lounge. How can I assist you with our menu or special blends today?</div>
        </div>
        <div class="input-row">
            <input type="text" id="userInput" placeholder="Ask about menu, dietary options, or recommendations..." onkeypress="handleKey(event)" />
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const text = input.value.trim();
            if (!text) return;

            const chatBox = document.getElementById('chatBox');
            chatBox.innerHTML += `<div class="msg user">${text}</div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const res = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                chatBox.innerHTML += `<div class="msg bot">${data.reply}</div>`;
            } catch (err) {
                chatBox.innerHTML += `<div class="msg bot">Sorry, something went wrong. Please try again.</div>`;
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function handleKey(e) {
            if (e.key === 'Enter') sendMessage();
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    if not user_msg:
        return jsonify({"reply": "Please provide a valid question."}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.3
            )
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Service temporarily unavailable: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)