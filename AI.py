# Lost some of my Og comments cuz ai had to rewrite this based off our previous debug chats after i accidentally replaced the original code with a earlier version.
# i will have to reveiw this later to comment it properly and make sure it didnt add anything unnecessary, but for now it works.

# Imports communication libraries for the server
from flask import Flask, request, jsonify
from flask_cors import CORS
# Imports Gemini 2.5 Flash from the Google GenAI library AND types config helper
from google import genai
from google.genai import types
import time

# Initializes the server manager and security guard
app = Flask(__name__)
CORS(app)
# Initializes the Gemini 2.5 Flash client
client = genai.Client()

cat_chat = None  # Global variable to hold the chat session

# LISTENER: Activates when JS calls 'http://127.0.0.1:5000/chat'
@app.route('/chat', methods=['POST'])
def chat():
    global cat_chat  # Access the global chat session variable

    # Opens incoming communication from JS and extracts the user's message
    data = request.json
    user_message = data.get('message')

    cat_response = None
    max_retries = 3

    for attempt in range(max_retries):
        try:
            if cat_chat is None:
                # If the chat session is not initialized, create it safely inside the loop
                cat_chat = client.chats.create(
                    model="gemini-2.5-flash-lite",
                    config=types.GenerateContentConfig(
                        system_instruction="You are a serious, wise, slightly judgmental cat. Speak in short, concise sentences. Do not use corporate AI fluff, do not flatter the user, and do not act overly sweet. Answer their message from a cat's perspective."
                    )
                )
            
            # Sends the user's message to the cat and gets a response
            response = cat_chat.send_message(user_message)
            cat_response = response.text
            break  # Exit the loop if successful

        except Exception:
            if attempt < max_retries - 1:
                time.sleep(1)  # Wait for a second before retrying
                continue       # Retry the request
            else:
                # If there's an error like too much traffic for this model after 3 tries
                cat_response = "*The cat stares at you blankly.*"
    
    # Mails the response back to JS under the 'reply' label
    return jsonify({"reply": cat_response})

# Starts the server on port 5000 when you run this file
if __name__ == '__main__':
    app.run(port=5000)