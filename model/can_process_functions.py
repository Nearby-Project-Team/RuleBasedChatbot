from xmlrpc.client import Boolean
import regex as re
from load_data import loadData

def isScheduleValidator(text: str):
    data = loadData("data-work.json")
    for con in data:
        if re.search(text, con):
            return True
    return False

