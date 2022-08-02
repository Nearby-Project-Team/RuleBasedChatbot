from pydantic import BaseModel

class ChattingDto(BaseModel):
    msg: str
    elderly_id: str
    