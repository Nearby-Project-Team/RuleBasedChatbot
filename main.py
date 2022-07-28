from requests import request
from model.chatbot import getChatbotModel
from fastapi import FastAPI
from dto.chattingDto import ChattingDto

app = FastAPI()
chatModel = getChatbotModel([
                            "chatterbot.corpus.korean"
                            ])

@app.post('/chat')
async def chatbot_response(message: ChattingDto):
    _u = message.msg
    print(_u)
    res = chatModel.get_response(_u)
    print(res)
    return { "response": str(res) }
    

