import json
import os
from typing import List 

DATA_PATH = os.path.join(os.path.abspath(), '../chatbot_data')
DATA_LIST = os.listdir(DATA_PATH)
DATA_DICT = { key : DATA_PATH + '/' + key for key in DATA_LIST }

def loadData(dataType: str):
    data = json.load(DATA_DICT[dataType])
    return data