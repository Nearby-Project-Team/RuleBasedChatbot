from database.mysql_repository import CalandarRepository
from database.chatting_repository import JokeRepository, FortuneRepository, AlarmRepository
from . import can_process_functions
from model.time_builder import TimeBuilder
from datetime import datetime
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
        self.joke = JokeRepository(
            host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        )
        self.fortune = FortuneRepository(
            host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        )
        self.alarm = AlarmRepository(
            host=config["database"]["host"],
            port=int(config["database"]["port"]),
            username=config["database"]["username"],
            password=config["database"]["password"],
            db=config["database"]["database"]
        )
    
    def date_preprocessing(self, time: str):
        
        pass
    
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
            result += time + "에 " + text + " "
        for con in Repeat:
            text, time = con
            result += time + "에 " + text + " "
        result += "입니다."
        return result