from requests import request
from model.ai_chatbot import getChatbotModel
from model.nearby_chatbot import NearbyLogic
from dto.chatting_dto import ChattingDto
from fastapi import FastAPI

app = FastAPI()
AIChatModel = getChatbotModel([
                                "chatterbot.corpus.korean"
                            ])

RuleChatModel = NearbyLogic()

@app.post('/chat')
async def chatbot_response(message: ChattingDto):
    _u = message.msg
    print(_u)
    res = RuleChatModel.process(_u)
    print(res)
    return { "response": str(res) }
    

