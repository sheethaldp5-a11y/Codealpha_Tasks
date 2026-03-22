# Basic Chatbot

A simple web-based chatbot application built with Flask that provides rule-based responses and sentiment analysis.

## Features

- **Rule-based Responses**: Responds to common greetings, questions, and farewells
- **Sentiment Analysis**: Analyzes user input sentiment (positive, negative, neutral) and adjusts responses accordingly
- **Web Interface**: Clean, responsive web UI for chatting
- **Conversation History**: Maintains in-memory conversation history

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd basic-chatbot
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/`
3. Start chatting with the bot!

## Dependencies

- Flask: Web framework for Python
- VADER Sentiment: Sentiment analysis tool

## Project Structure

```
basic-chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── core/
│   ├── rules.py          # Rule-based response logic
│   └── utils.py          # Utility functions (sentiment analysis)
├── static/
│   └── style.css         # CSS styling for the web interface
├── templates/
│   └── index.html        # HTML template for the chat interface
└── README.md             # This file
```

## How It Works

The chatbot uses a combination of rule-based responses and sentiment analysis:

1. **Input Processing**: User messages are processed for keywords
2. **Sentiment Analysis**: VADER analyzes the emotional tone of the input
3. **Response Generation**: Appropriate responses are selected based on rules and sentiment
4. **Response Modification**: Responses are adjusted based on detected sentiment

## Future Enhancements

- Add more sophisticated NLP capabilities
- Implement persistent conversation storage
- Add user authentication
- Integrate with external APIs for more dynamic responses