from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious') 
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

chatbot.get_response("Hello, how are you doing?")

while True:
	request = input('You: ')
	response = chatbot.get_response(request)
	
	print('Bot: ', response)
