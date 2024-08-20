import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define the chatbot's responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"who are you?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry",
        ["It's alright.", "No problem",]
    ],
    [
        r"I am (good|well|okay|ok)",
        ["Nice to hear that.", "Alright, great!",]
    ],
    [
        r"what is your age?",
        ["I'm a computer program, so I don't have an age.",]
    ],
    [
        r"what do you want?",
        ["I want to help you and chat with you!",]
    ],
    [
        r"who created you?",
        ["I was created by a Python enthusiast.", "I was created by a programmer like you.",]
    ],
    [
        r"where are you from?",
        ["I'm from the virtual world.",]
    ],
    [
        r"how is the weather ",
        ["I don't have access to weather information currently.",]
    ],
    [
        r"bye",
        ["Bye, take care. See you soon!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you please rephrase?",]
    ],
]

chatbot = Chat(pairs, reflections)

# Function to run the chatbot
def chatbot_conversation():
    print("Hi, I'm your AI chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Bye, take care. See you soon!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot_conversation()
