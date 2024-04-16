from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new ChatBot instance
chatbot = ChatBot("MyChatBot")

# Create a new trainer for the chatbot
trainer = ListTrainer(chatbot)

# Train the chatbot with a few conversations
trainer.train([
    "Hello",
    "Hi, how can I help you?",
    "What is your name?",
    "My name is MyChatBot. What's yours?",
    "Goodbye",
    "Bye! Have a great day!"
])

# Function to start a conversation with the chatbot
def chat():
    print("Chat with the chatbot! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot.get_response(user_input)
        print(f"MyChatBot: {response}")

# Start chatting with the chatbot
chat()
