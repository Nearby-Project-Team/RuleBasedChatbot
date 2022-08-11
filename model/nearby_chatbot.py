from database.mysql_repository import CalandarRepository
from . import can_process_functions
from model.time_builder import TimeBuilder
import configparser
import os 

class NearbyLogic:

    def __init__(self):    
        self.functionList = []
        for con in dir(can_process_functions):
            if callable(getattr(can_process_functions, con)) and not (con == "loadData"):
                self.functionList.append(getattr(can_process_functions, con))

        config_path = os.path.join(os.path.abspath('./'), "config.ini")
        config = configparser.ConfigParser()
        config.read(config_path)
        self.calendar = CalandarRepository(
            host=config["database"]["host"],
            port=int(config["database"]["port"]),
            username=config["database"]["username"],
            password=config["database"]["password"],
            db=config["database"]["database"]
        )
        
    def can_process(self, statement: str):
        for func in self.functionList:
            if not func(statement):
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
        oneOff, Repeat = self.calendar.getBothSideCalandarInfo(elderly_id, s, e)
        result = "원하시던 요청은 "
        for con in oneOff:
            text, time = con
            result += time + "의 시간에 " + text + " "
        for con in Repeat:
            text, time = con
            result += time + "의 시간에 " + text + " "
        result += "입니다."
        return result