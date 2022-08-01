from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

class NearbyLogic(LogicAdapter):
    
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        
    def can_process(self, statement):
        content: str = statement.text
        
        return 
    
    def process(self, statement, additional_response_selection_parameters=None):
        content: str = statement.text
        
        return