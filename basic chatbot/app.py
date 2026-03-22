from flask import Flask, render_template, request, jsonify
from core.rules import get_chatbot_response
from core.utils import get_sentiment

app = Flask(__name__)

# In-memory conversation history
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'response': "I didn't catch that. Could you say something?"})

    # Add user message to history
    conversation_history.append({'sender': 'user', 'message': user_input})

    # Get sentiment
    sentiment = get_sentiment(user_input)

    # Get chatbot response
    response = get_chatbot_response(user_input)

    # Modify response based on sentiment
    if sentiment == 'positive':
        response = f"I'm glad you're feeling positive! {response}"
    elif sentiment == 'negative':
        response = f"I'm sorry to hear that. {response}"

    # Add bot response to history
    conversation_history.append({'sender': 'bot', 'message': response})

    return jsonify({'response': response, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
