from pydantic import BaseModel

class ChattingDto(BaseModel):
    msg: str
    