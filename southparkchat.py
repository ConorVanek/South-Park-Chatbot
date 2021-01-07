from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

with open("southparkdialogue.txt", encoding="utf8") as file_in:
    train_data = []
    for line in file_in:
        lines = line.rstrip()
        train_data.append(lines)



chatbot = ChatBot(
    "Terminal",
    input_adapter="chatterbot.input.TerminalAdapter", #allows a user to type into their terminal to communicate with the chat bot.
    output_adapter="chatterbot.output.TerminalAdapter" # print chatbot responce
)

trainer = ListTrainer(ChatBot)
#chatbot.set_trainer(ListTrainer) Old format
trainer.train(train_data)
#chatbot.train(train_data) Old Format


print("Type your question here...")
while True:
    try:
        chatbot_input = chatbot.get_response(None)
    # Press ctrl-c or ctrl-d to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break