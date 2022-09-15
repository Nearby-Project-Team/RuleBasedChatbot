# RuleBasedChatbot

### Install Dependencies

***

```sh
pip3 install -r requirements.txt
```

### Start Chatbot server

***

```sh
python3 server.py
```

### Seed Data to the Database

***

You can seed data to the database with manager SW

```sh
python3 chatbot_manger.py --table <Table Name>
```

### Rule-base Chatbot Rule List

|Rule|Description|Keyword|Usage|
|-|-|-|-|
|Schedule|Return a schedule list of the elderly user. | ```일```, ```할일```, ```해야할 일```, ```일정``` | ```일정 알려줘``` |
|Current Time|Return current time. | ```지금 몇시야```, ```몇시인지 알려줘``` | ```지금 몇시야?``` |
|Joke|Return a funny phrase randomly. | ```농담``` | ```농담 해줘``` |
|Fortune|Return a good phrase randomly.| ```운세``` | ```운세 알려줘``` |
|Weather|Find weather and temperature in the location.| (```온도``` or ```날씨```) + ```지역``` | ```서울 날씨 알려줘```, ```대전시 온도 알려줘``` |
