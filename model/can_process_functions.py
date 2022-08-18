import regex as re
from .load_data import loadData

def isStringMatch(_content: list, statement: str):
    for con in _content:
        if bool(re.search(con, statement)):
            return True
    return False

def isScheduleValidator(text: str):
    data = loadData("data-work-list.json")
    return isStringMatch(data, text)

def isJokeValidator(text: str):
    data = loadData("data-joke-list.json")
    return isStringMatch(data, text)

def isFourtuneValidator(text: str):
    data = loadData("data-fortune-list.json")
    return isStringMatch(data, text)

def isWeatherValidator(text: str):
    data = loadData("data-weather-list.json")
    return isStringMatch(data, text)

def isTimeValidator(text: str):
    data = loadData("data-time-list.json")
    return isStringMatch(data, text)

