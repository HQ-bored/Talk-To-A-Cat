
from flask import Flask, request, jsonify
from flask_cors import CORS

# 1. Initialize the server manager and security guard
app = Flask(__name__)
CORS(app)

# 2. LISTENER: Activates when JS calls 'http://127.0.0.1:5000/chat'
@app.route('/chat', methods=['POST'])
def chat():

    # 3. Open incoming package and grab the text under the 'message' label
    data = request.json
    user_message = data.get('message')
    
    # 4. Generate the response (Placeholder for now)
    cat_response = "... --- ..."
    
    # 5. CRITICAL: Mail the response back to JS under the 'reply' label
    return jsonify({"reply": cat_response})

# 6. MAIN ENGINE: Starts the server on port 5000 when you run this file
if __name__ == '__main__':
    app.run(port=5000, debug=True)