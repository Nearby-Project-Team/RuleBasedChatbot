from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def getChatbotModel(trainList: list):
    chatbot = ChatBot(
        'nearby',
        logic_adapters=[
            {
                'import_path': 'nearby_adapter.NearbyLogic'
            }
        ]
    )
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(*trainList)
    
    return chatbot