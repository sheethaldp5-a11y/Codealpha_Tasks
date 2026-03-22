import random

def get_chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Simple rule-based logic
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!", "Hey!"],
        "hi": ["Hi there!", "Hello!", "Greetings!", "Hey!"],
        "how are you": ["I'm doing well, thank you!", "I'm great, how about you?", "Everything's good on my end!"],
        "what is your name": ["I'm ChatBot!", "You can call me ChatBot.", "I am your friendly neighborhood chatbot."],
        "bye": ["Goodbye!", "See you later!", "Have a great day!", "Bye! Take care!"],
        "default": ["I'm not sure I understand that. Could you rephrase?", "That's interesting, tell me more.", "I'm still learning! Can you say that differently?"]
    }
    
    # Check for keywords in user input
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
            
    return random.choice(responses["default"])

def start_chat():
    print("ChatBot: Hello! I'm ready to chat. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == 'bye':
            print("ChatBot: " + get_chatbot_response('bye'))
            break
        
        response = get_chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    start_chat()
