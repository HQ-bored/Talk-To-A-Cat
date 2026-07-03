# NGL this is the one files where ai keeps rewiting stuff and i dont understand like half of them
# gotta reveiw this later


# Imports communication libraries for the server
from flask import Flask, request, jsonify
from flask_cors import CORS
# Imports Gemini 2.5 Flash from the Google GenAI library AND types config helper
from google import genai
from google.genai import types

from Encoder import RunCatEncoder

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

    CatsResponse = None
    max_retries = 3

    for attempt in range(max_retries):
        try:
            if cat_chat is None:
                # If the chat session is not initialized, create it safely inside the loop
                cat_chat = client.chats.create(
                    model="gemini-2.5-flash-lite",
                    config=types.GenerateContentConfig(
                        system_instruction="You are a slightly judgmental cat who offers advice for payment like food. Speak in short, concise sentences. Do not use corporate AI fluff, do not flatter the user, and do not act overly sweet. Answer their message from a cat's perspective."
                    )
                )
            
            # cat shoould start the conversation in the futur

            # Sends the user's message to the cat and gets a response
            response = cat_chat.send_message(user_message)
            CatsResponse = response.text
            break  # Exit the loop if successful

        except Exception:
            if attempt < max_retries - 1:
                time.sleep(1)  # Wait for a second before retrying
                continue       # Retry the request
            else:
                # If there's an error like too much traffic for this model after 3 tries
                CatsResponse = "*The cat stares at you blankly.*"
    
    # Encode response 
    print("--- DEBUG START ---")
    print("Raw AI Response:", CatsResponse)

    CatsResponse = RunCatEncoder(CatsResponse)

    print("Encoded Response:", CatsResponse) 
    print("---- DEBUG END ----")

    # Mails the response back to JS under the 'reply' label
    return jsonify({"reply": CatsResponse})




if __name__ == '__main__':
    # Ask how you want to chat today
    mode = input("Press '1' for Web Server, or '2' for Terminal Chat: ")

    if mode == '1':
        print("Starting Flask web server on port 5000...")
        app.run(port=5000)

    elif mode == '2':
        print("Terminal chat active! (Type 'quit' to exit)")

        # Initialize the AI session once
        cat_chat = client.chats.create(
            model="gemini-2.5-flash-lite",
            config=types.GenerateContentConfig(
                system_instruction="You are a slightly judgmental cat who offers advice for payment like food. Speak in short, concise sentences. Do not use corporate AI fluff, do not flatter the user, and do not act overly sweet. Answer their message from a cat's perspective."
            )
        )

        # A loop to keep the conversation going!
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break

            # Send the message to Gemini
            response = cat_chat.send_message(user_input)
            raw_reply = response.text

            # Pass it through your custom encoder
            scrambled_reply = RunCatEncoder(raw_reply)

            # Print the plain English and scrambled version together
            print("Cat (English):", raw_reply)
            print("Cat (Encoded):", scrambled_reply)
            print("-" * 20)