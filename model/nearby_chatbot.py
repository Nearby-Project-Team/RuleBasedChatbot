from database.mysql_repository import CalandarRepository
import can_process_functions as preFunctions

class NearbyLogic:

    def __init__(self):    
        self.functionList = []
        for con in dir(preFunctions):
            if callable(con):
                self.functionList.append(con)
    
    def can_process(self, statement: str):
        content: str = statement.text
        for func in self.functionList:
            if not func(content):
                return False                
        return True
    
    def process(self, statement: str):
        if not self.can_process(statement):
            return "잘 모르겠어요."
        
        
        return 