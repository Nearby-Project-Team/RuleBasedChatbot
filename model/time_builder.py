from datetime import datetime
import regex as re

class TimeBuilder:
    
    def __init__(self, text):
        self.text = text
        self.sdate = None
        self.edate = None
        
    def isInBeforeStatement(self):
        if re.search(self.text, "이전"):
            return True
        return False
        
    def process(self):
        
        return self.sdate, self.edate
