import nltk
from nltk.chat.util import Chat, reflections

# Define the chat pairs for greetings
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you', ['I\'m just a chatbot, but I\'m here to help! How can I assist you today?']],
    ['what is your name', ['I am a chatbot created by OpenAI.', 'I am your friendly chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'Have a great day!', 'See you later!']],
    ['how do you feel',['awesome as always']],
    ['quotes',['everything happens for a reason  it might be hard to accept but its the reality']],
['goodnight',['have a sweet dream']],
 ]


# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello! I'm your chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
