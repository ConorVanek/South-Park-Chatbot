from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



# with open("southparkdialogue.txt", encoding="utf8") as file_in:
#    train_data = []
#    for line in file_in:
#        lines = line.rstrip()
#        train_data.append(lines)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot = ChatBot('southpark')
trainer = ListTrainer(ChatBot)

dialogue_path = 'C:/Users/Public/Documents/southparkdialogue/southparkdialogue.txt'

trainer.train(conversation)


response = chatbot.get_response('Hello there, children!')
print(response)