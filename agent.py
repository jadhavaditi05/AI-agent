import random

print("🤖 ChatBot: Hello! I am your chatbot.")
print("🤖 ChatBot: You can ask me simple questions.")
print("🤖 ChatBot: Type 'bye' to exit.\n")

responses = {
    "hello": [
        "Hello! 😊",
        "Hi! How are you?",
        "Hey! Nice to meet you!"
    ],

    "how are you": [
        "I am doing great!",
        "I'm fine, thank you!",
        "I'm doing well. 😊"
    ],

    "name": [
        "My name is PyBot.",
        "You can call me PyBot."
    ],

    "help": [
        "I can answer simple questions.",
        "Try asking me about my name or how I am."
    ],

    "thanks": [
        "You're welcome! 😊",
        "No problem!",
        "Anytime!"
    ]
}

while True:
    user = input("You: ").lower().strip()

    if user in ["bye", "exit", "quit"]:
        print("🤖 ChatBot: Goodbye! 👋")
        break

    elif user in ["hello", "hi", "hey"]:
        print("🤖 ChatBot:", random.choice(responses["hello"]))

    elif "how are you" in user:
        print("🤖 ChatBot:", random.choice(responses["how are you"]))

    elif "your name" in user or "who are you" in user:
        print("🤖 ChatBot:", random.choice(responses["name"]))

    elif "help" in user or "what can you do" in user:
        print("🤖 ChatBot:", random.choice(responses["help"]))

    elif "thank" in user or "thanks" in user:
        print("🤖 ChatBot:", random.choice(responses["thanks"]))

    else:
        print("🤖 ChatBot: Sorry, I don't understand that yet.")