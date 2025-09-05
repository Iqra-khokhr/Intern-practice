import re

# Step 1: Define patterns and responses
patterns = {
    r'hello|hi': "Hi, how can I help you?",
    r'what is your name\??': "I am your Python Chatbot.",
    r'how are you\??': "I'm just code, but I'm here to help!",
    r'bye|exit': "Goodbye! Have a nice day."
}

def get_response(user_input):
    for pattern, response in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I don't understand."

# Step 2: Chat loop
while True:
    user_input = input("You: ")
    if re.search(r'exit|bye', user_input, re.IGNORECASE):
        print("Bot:", patterns[r'bye|exit'])
        break
    print("Bot:", get_response(user_input))