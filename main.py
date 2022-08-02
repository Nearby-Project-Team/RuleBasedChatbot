from requests import request
from model.ai_chatbot import getChatbotModel
from fastapi import FastAPI
from dto.chatting_dto import ChattingDto

app = FastAPI()
AIChatModel = getChatbotModel([
                                "chatterbot.corpus.korean"
                            ])



@app.post('/chat')
async def chatbot_response(message: ChattingDto):
    _u = message.msg
    print(_u)
    res = AIChatModel.get_response(_u)
    print(res)
    return { "response": str(res) }
    

