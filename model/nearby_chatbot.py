from database.mysql_repository import CalandarRepository
from database.chatting_repository import JokeRepository, FortuneRepository, AlarmRepository
from . import can_process_functions
from model.time_builder import TimeBuilder
from datetime import datetime
import configparser
import random
import os 
import requests
from . import weather_functions as wf

class NearbyLogic:

    def __init__(self):    
        self.functionList = []
        for con in dir(can_process_functions):
            if callable(getattr(can_process_functions, con)) and not (con == "loadData") and not (con == "isStringMatch"):
                self.functionList.append(getattr(can_process_functions, con))
        
        self.chatbotUrl = "http://localhost:5000/predictions/chatbot"
        self.session = requests.session()
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
        _t = datetime.strptime(time, "%Y-%m-%d %H:%M")
        return str(_t.month) + "??? " + str(_t.day) + "??? " + str(_t.hour) + "??? " + str(_t.minute) + "???"
    
    def can_process(self, statement: str):
        for func in self.functionList:
            if func(statement):
                return True
        return False
    
    def process(self, statement: str, elderly_id: str):
        if not self.can_process(statement):
            chat_data = { 'data': statement }
            response = self.session.post(self.chatbotUrl, data=chat_data)
            _res = response.content.decode('utf-8')
            if len(_res) >= 60:
                return "??? ???????????????." 
            return _res
        
        if can_process_functions.isScheduleValidator(statement):
            timeBuilder = TimeBuilder(statement)
            res = timeBuilder.process()
            print(res)
            if not res:
                return "??? ???????????????."
            s, e = res
            oneOff, Repeat = self.calendar.getBothSideCalandarInfo(elderly_id, s, e)
            result = "???????????? ????????? "
            for con in oneOff:
                text, time = con
                time_data = self.date_preprocessing(time)
                result += time_data + "??? " + text + " "
            for con in Repeat:
                text, time = con
                print(time)
                time_data = self.date_preprocessing(time.strftime('%Y-%m-%d %H:%M'))
                result += time_data + "??? " + text + " "
            result += "?????????."
            return result
        
        if can_process_functions.isTimeValidator(statement):
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            return "????????? " + self.date_preprocessing(now) + " ?????????."
        
        if can_process_functions.isJokeValidator(statement):
            joke = self.joke.listAllJoke()
            _j = random.choice(joke)
            return _j[1]
        
        if can_process_functions.isFourtuneValidator(statement):
            fortune = self.fortune.listAllFortune()
            _f = random.choice(fortune)
            return _f[1]
        
        if can_process_functions.isWeatherValidator(statement):
            try:
                coord = wf.get_coord_from_statement(statement)
                if(coord is None):
                    return "????????? ?????? ??? ????????????. ???????????? ???????????? ????????? ???????????????. ?????? ????????? ????????? ?????? ???????????? ?????? ???????????? ?????? ??? ????????????."
                
                weather_state = wf.get_weather_from_coord(coord[1])
                return wf.get_weather_string(coord[0], weather_state)
            except Exception as e:
                print(e)
                return "?????? API ????????? ????????? ??? ??? ????????????."