from database.mysql_repository import CalandarRepository
import can_process_functions as preFunctions
from model.time_builder import TimeBuilder
import configparser
import os 

class NearbyLogic:

    def __init__(self):    
        self.functionList = []
        for con in dir(preFunctions):
            if callable(con):
                self.functionList.append(con)

        config_path = os.path.join(os.path.abspath(), "../config.ini")
        config = configparser.ConfigParser()
        config.read(config_path)
        self.calendar = CalandarRepository(
            host=config["database"]["host"],
            port=config["database"]["port"],
            username=config["database"]["username"],
            password=config["database"]["password"],
            db=config["database"]["database"]
        )
        
    def can_process(self, statement: str):
        content: str = statement.text
        for func in self.functionList:
            if not func(content):
                return False                
        return True
    
    def process(self, statement: str, elderly_id: str):
        if not self.can_process(statement):
            return "잘 모르겠어요."
        
        timeBuilder = TimeBuilder(statement)
        res = timeBuilder.process()
        if not res:
            return "잘 모르겠어요."
        s, e = res
        contentList = self.calendar.getBothSideCalandarInfo(elderly_id, s, e)
        result = "원하시던 요청은 "
        for con in contentList:
            text, time = con
            result += time.isoformat(timespec='auto') + "의 시간에 " + text + " "
        result += "입니다."
        return result