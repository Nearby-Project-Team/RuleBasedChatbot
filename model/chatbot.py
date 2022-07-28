from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def getChatbotModel(*trainList):
    chatbot = ChatBot('nearby')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(*trainList)
    
    return chatbot