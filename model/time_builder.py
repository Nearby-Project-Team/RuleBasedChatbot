from datetime import datetime
from .load_data import loadData
import regex as re

class TimeBuilder:
    
    def __init__(self, text):
        self.text = text
        self.sdate = None
        self.edate = None
        
    def isInBeforeStatement(self):
        before = loadData('data-order-dict.json')
        for con in before["before"]:
            if re.search(self.text, con):
                return True
        return False
        
    def isInAmStatement(self):
        am = loadData('data-time-dict.json')
        for con in am["am"]:
            if re.search(self.text, con):
                return True
        return False
    
    def isInPmStatement(self):
        pm = loadData('data-time-dict.json')
        for con in pm["pm"]:
            if re.search(self.text, con):
                return True
        return False
    
    def process(self):
        
        now_time = datetime.today()
        if self.isInAmStatement() and self.isInPmStatement():
            return None
        elif self.isInAmStatement():
            self.sdate = "{}-{}-{} 00:00".format(now_time.year, now_time.month, now_time.day)
            self.edate = "{}-{}-{} 12:00".format(now_time.year, now_time.month, now_time.day)
        elif self.isInPmStatement():
            self.sdate = "{}-{}-{} 12:00".format(now_time.year, now_time.month, now_time.day)
            self.edate = "{}-{}-{} 24:00".format(now_time.year, now_time.month, now_time.day)
        return self.sdate, self.edate
