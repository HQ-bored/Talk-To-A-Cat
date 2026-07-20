from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
from Encoder import RunCatEncoder
import time
import os # Acess secret api key

# Initializes the server manager and security guard
app = Flask(__name__)
CORS(app)

#new
# Initializes the Gemini 2.5 Flash client with the api key
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY")) # migth cause terminal test to fail

cat_chat = None  # Global Nonetype variable
MaxRetries = 3


@app.route('/start-chat', methods=['POST']) #when JS calls /start-chat, start new chat session
def start_chat():
    global cat_chat
    global MaxRetries
    for attempt in range(MaxRetries):
        try:
            cat_chat = client.chats.create(
                model="gemini-2.5-flash-lite",
                config=types.GenerateContentConfig(
                    system_instruction="You are a slightly judgmental cat who offers advice for payment like food. Speak in short, concise sentences of around 10 words. Do not use corporate AI fluff, do not flatter the user, and do not act overly sweet. Answer their message from a cat's perspective."
                )
            )
            return jsonify({"status": "Chat Session Initiated!"})
            break
        except Exception as e:
            if attempt < MaxRetries - 1:
                time.sleep(1)
                continue
            else:
                return "", 500
#new end

# LISTENER: Activates when JS calls 'http://127.0.0.1:5000/chat'
@app.route('/chat', methods=['POST'])
def chat():
    global cat_chat  # Access the global chat session variable
    global MaxRetries #new s
    # Opens incoming communication from JS and extracts the user's message
    data = request.json
    user_message = data.get('message')

    CatsResponse = None

    for attempt in range(MaxRetries):
        try:
            if cat_chat is None:
                # If the chat session is not initialized, create it safely inside the loop
                cat_chat = client.chats.create(
                    model="gemini-2.5-flash-lite",
                    config=types.GenerateContentConfig(
                        system_instruction="You are a slightly judgmental cat who offers advice for payment like food. Speak in short, concise sentences of around 10 words. Do not use corporate AI fluff, do not flatter the user, and do not act overly sweet. Answer their message from a cat's perspective."
                    )
                )
            
            # Sends the user's message to the cat and gets a response
            response = cat_chat.send_message(user_message)
            CatsResponse = response.text
            break  # Exit the loop if successful

        except Exception:
            if attempt < MaxRetries - 1:
                time.sleep(1)  # Wait for a second before retrying
                continue       # Retry the request
            else:
                # If there's an error like too much traffic for this model after 3 tries
                CatsResponse = "*error *The cat stares at you blankly.*"
    
    # Encode response 
    print("Raw AI Response:", CatsResponse)
    #new
    if CatsResponse == "404 : The cat stares at you blankly":
        pass # pass=do nothing continue=go back to top of loop
    else:
        CatsResponse = RunCatEncoder(CatsResponse)
    #new
    print("Encoded Response:", CatsResponse) 

    # Mails the response back to JS under the 'reply' label
    return jsonify({"reply": CatsResponse})

if __name__ == '__main__':
    app.run(port=5000)