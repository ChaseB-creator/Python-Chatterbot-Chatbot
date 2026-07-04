

# This project is going to have 4 different chatbots, 
# each having their own unique personalities and interests.

# The user will choose which chatbot they want to talk to.

# ----------------------Chatbot types--------------------------
# The first chatbot will be a optimistic inspirational chatbot.
# -------------------------------------------------------------

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer

chatbot1 = ChatBot('OptimisticBot')

# This data is for Optimistic bot.
# trainer1 = ListTrainer(chatbot1)

trainer = ChatterBotCorpusTrainer(chatbot1)
print("You can now start chatting with our first bot! (type 'exit' to end the conversation).")

while True:

    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot1.get_response(user_input)
    print(f"OptimisticBot: {response}")