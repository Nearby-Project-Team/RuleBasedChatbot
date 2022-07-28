from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def getChatbotModel(trainList: list):
    chatbot = ChatBot('nearby')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(*trainList)
    
    return chatbot