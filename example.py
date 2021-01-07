from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

train_data = []

with open("southparkdialogue.txt", encoding="utf8") as file_in:
   train_data = []
   for line in file_in:
       lines = line.rstrip()
       train_data.append(lines)


# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

trainer = ListTrainer(chatbot)

trainer.train(train_data)



while True:
    try:
        bot_input = chatbot.get_response(input())
        print('\n')
        print(bot_input)
        print('\n')

    except(KeyboardInterrupt, EOFError, SystemExit):
        break