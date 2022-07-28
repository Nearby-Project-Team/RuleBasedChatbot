from requests import request
from model.chatbot import getChatbotModel
from typing import Union
from fastapi import FastAPI
from dto.chattingDto import ChattingDto

app = FastAPI()
chatModel = getChatbotModel("chatterbot.corpus.english.greetings",
                            "chatterbot.corpus.english.conversations")

@app.post('/chat')
async def chatbot_response(message: ChattingDto):
    _u = message.msg
    res = chatModel.get_response(_u)
    return res
    

