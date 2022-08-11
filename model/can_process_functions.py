import regex as re
from .load_data import loadData

def isScheduleValidator(text: str):
    data = loadData("data-work-list.json")
    for con in data:
        res = re.findall(con, text)
        print(res)
        if res:
            return True
    return False

