import regex as re
from .load_data import loadData

def isScheduleValidator(text: str):
    data = loadData("data-work-list.json")
    for con in data:
        if bool(re.search(con, text)):
            return True
    return False

def isJokeValidator(text: str):
    data = loadData("data-joke-list.json")
    for con in data:
        if bool(re.search(con, text)):
            return True
    return False

def isFourtuneValidator(text: str):
    data = loadData("data-fortune-list.json")
    for con in data:
        if bool(re.search(con, text)):
            return True
    return False

def isWeatherValidator(text: str):
    data = loadData("data-weather-list.json")
    for con in data:
        if bool(re.search(con, text)):
            return True
    return False

def isTimeValidator(text: str):
    data = loadData("data-time-list.json")
    for con in data:
        if bool(re.search(con, text)):
            return True
    return False