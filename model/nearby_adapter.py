from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter
import can_process_functions as preFunctions

class NearbyLogic(LogicAdapter):
    
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
    
        self.functionList = []
        for con in dir(preFunctions):
            if callable(con):
                self.functionList.append(con)
    
    def can_process(self, statement):
        content: str = statement.text
        result = True
        for func in self.functionList:
            if not func(content):
                result = False                
        return result
    
    def process(self, statement, additional_response_selection_parameters=None):
        content: str = statement.text
        
        return