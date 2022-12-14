from model.nearby_chatbot import NearbyLogic
from dto.chatting_dto import ChattingDto
from fastapi import FastAPI
import uvicorn

app = FastAPI()
RuleChatModel = NearbyLogic()

@app.post('/chat')
async def chatbot_response(message: ChattingDto):
    _u = message.msg
    elderly_id = message.elderly_id
    print(_u)
    res = RuleChatModel.process(_u, elderly_id)
    print(res)
    return { "response": str(res) }
    
if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        port=8000,
        host="0.0.0.0",
        reload=True
    )