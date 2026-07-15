# Imports communication libraries for the server
from flask import Flask, request, jsonify
from flask_cors import CORS
# Imports Gemini from the Google GenAI library AND types config helper
from google import genai
from google.genai import types
import time  # Allows us to use time.sleep() for the retry delays

# Initializes the server manager and security guard
app = Flask(__name__)
CORS(app)
# Initializes the Gemini client
client = genai.Client()

@app.route('/chat', methods=['POST'])
def chat():
    # Grabs the text from your website's text box
    data = request.json
    user_message = data.get('message')
    
    cat_response = None
    max_retries = 3

    # --- AUTOMATIC RETRY LOOP ---
    for attempt in range(max_retries):
        try:
            # Attempt to get a response from the lite model
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction="You are a serious, wise, slightly judgmental cat. Speak in short, concise sentences. Do not use corporate AI fluff, do not flatter the user, and do not act overly sweet. Answer their message from a cat's perspective."
                )
            )
            cat_response = response.text
            break  # It worked! Break out of the loop immediately.
            
        except Exception:
            # If it fails, check if we have retries left
            if attempt < max_retries - 1:
                time.sleep(1)  # Wait 1 second before trying again
                continue       # Jump to the next attempt loop
            else:
                # If it fails all 3 times, give the fallback message
                cat_response = "*The cat stares at you blankly. Try again.*"
    
    # Packs up the cat's answer and sends it back to your browser
    return jsonify({"reply": cat_response})

if __name__ == '__main__':
    app.run(port=5000)