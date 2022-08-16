from database.chatting_repository import JokeRepository, FortuneRepository, AlarmRepository
import configparser
import argparse
import os 

parser = argparse.ArgumentParser(description='This SW is for inserting data in the DB')
parser.add_argument('--table', help='Table where manager insert the data.')

def Joke(host, port, username, password, db):
    while True:
        try :
            _c = input("Command > ")
            with JokeRepository(host=host, port=port, username=username, password=password, db=db) as jRepository:
                if _c == "1":
                    _d = input("Statement > ")
                    jRepository.insertJoke(_d)
                    jRepository.complete()
                elif _c == "2":
                    data = jRepository.listAllJoke()
                    for con in data:
                        print("ID: ", con[0], " , Joke: ", con[1])
                else :
                    raise ValueError("Invalid Command") 
        except KeyboardInterrupt:
            print("Quit")
            break

def Fortune(host, port, username, password, db):
    while True:
        try :
            _c = input("Command > ")
            with FortuneRepository(host=host, port=port, username=username, password=password, db=db) as fRepository:
                if _c == "1":
                    _d = input("Statement > ")
                    fRepository.insertFortune(_d)
                    fRepository.complete()
                elif _c == "2":
                    data = fRepository.listAllFortune()
                    for con in data:
                        print("ID: ", con[0], " , Fortune: ", con[1])
                else :
                    raise ValueError("Invalid Command")
        except KeyboardInterrupt:
            print("Quit")
            break

def Alarm(host, port, username, password, db):
    while True:
        try :
            _c = input("Command > ")
            with AlarmRepository(host=host, port=port, username=username, password=password, db=db) as aRepository:
                if _c == "1":
                    _d = input("Statement > ")
                    _s = input("Alarm Type > ")
                    aRepository.insertAlarm(_d, _s)
                    aRepository.complete()
                elif _c == "2":
                    data = aRepository.listAllAlarm()
                    for con in data:
                        print("ID: ", con[0], " , Alarm: ", con[1], " , Alarm Type: ", con[2])
                else :
                    raise ValueError("Invalid Command")
        except KeyboardInterrupt:
            print("Quit")
            break

if __name__ == "__main__":
    args = parser.parse_args()
    table = args.table
    if table is None:
        raise ValueError("Invalid Table Type!")
    config_path = os.path.join(os.path.abspath('./'), "config.ini")
    config = configparser.ConfigParser()
    config.read(config_path)
    print("Enter {}s to make data".format(table))
    print("Command 1 > Insert Data into the DB")
    print("Command 2 > List up data in the DB")
    if table == "create":
        with JokeRepository(host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        ) as jRepository:
            jRepository.createTable()
            jRepository.complete()
        with FortuneRepository(host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        ) as fRepository:
            fRepository.createTable()
            fRepository.complete()
        with AlarmRepository(host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        ) as aRepository:
            aRepository.createTable()
            aRepository.complete()
    if table == "joke":
        Joke(host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        )
    if table == "fortune":
        Fortune(host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        )
    if table == "alarm":
        Alarm(host=config["chatbot"]["host"],
            port=int(config["chatbot"]["port"]),
            username=config["chatbot"]["username"],
            password=config["chatbot"]["password"],
            db=config["chatbot"]["database"]
        )