import re
import requests
import datetime as dt
import os
import pandas as pd

trans_map = None

def get_coord_from_statement(statement):
    global trans_map
    if(trans_map is None):
        trans_map = pd.read_csv(os.path.abspath('./chatbot_data/weather_api_map.csv'),header=None)
    
    for _, item in trans_map.iterrows():
        if(re.search(item[0],statement) is not None):
            return (item[1],(int(item[2]),int(item[3])))
    return None

def get_weather_from_coord(coord):
    api_key = os.environ['WEATHER_API']
    time_data = dt.datetime.now() - dt.timedelta(hours=1)
    base_date = time_data.strftime('%Y%m%d')
    base_time = time_data.strftime('%H') + '00'
    nx = coord[0]
    ny = coord[1]
    query_string = fr'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={api_key}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}'
    response = requests.get(query_string,verify=False)
    response = response.json()
    item_list: list = response['response']['body']['items']['item']
    for item in item_list:
        if item['category'] == 'PTY':
            wthr = int(item['obsrValue'])
        if item['category'] == 'T1H':
            temp = float(item['obsrValue'])
    return (temp, wthr)

def number_to_temp_hangul(num):
    if(num == 0):
        return '영'
    hs = ""
    ns = ['영','일','이','삼','사','오','육','칠','팔','구']
    abs_num = abs(num)
    if(abs_num >= 10):
        t = int(abs_num)//10
        if t > 1:
            hs += ns[t]
        hs += '십'
    
    t = int(abs_num)%10
    if t > 0:
        hs += ns[t]
    
    t = int(abs_num*10)%10
    if t > 0:
        hs += "쩜" + ns[t]

    if(num<0):
        hs = '영하 ' + hs
    hs += '도'

    return hs

def index_to_weather(weather_index):
    ws = ""
    if weather_index == 0:
        ws = "비가 오지 않습니다"
    elif weather_index == 1:
        ws = "비가 내립니다"
    elif weather_index == 2:
        ws = "비와 눈이 동반하여 내립니다"
    elif weather_index == 3:
        ws = "눈이 내립니다"
    elif weather_index == 5:
        ws = "빗방울이 날립니다"
    elif weather_index == 6:
        ws = "빗방울, 눈이 날립니다"
    elif weather_index == 7:
        ws = "눈이 날립니다"
    else:
        ws = "현재 날씨를 알 수 없습니다"

    return ws  

def get_weather_string(local_name, weather_state):
    temp = weather_state[0]
    wthr = weather_state[1]

    temp = number_to_temp_hangul(temp)
    wthr = index_to_weather(wthr) 
    return "{}의 온도는 현재 {}이고, {}.".format(local_name, temp,wthr)

if __name__ == '__main__':
    coord = get_coord_from_statement('서울 날씨')
    print(coord)
    weather_obj = get_weather_from_coord(coord[1])
    print(weather_obj)
    
    print(get_weather_string('서울', (-10.2,3)))
    weather_string = get_weather_string(coord[0], weather_obj)
    print(weather_string)

    coord = get_coord_from_statement('부산진구')
    print(coord)
    weather_obj = get_weather_from_coord(coord[1])
    print(weather_obj)
    print(get_weather_string(coord[0],weather_obj))

    coord = get_coord_from_statement('강동구')
    print(coord)
    weather_obj = get_weather_from_coord(coord[1])
    print(weather_obj)
    print(get_weather_string(coord[0],weather_obj))

    coord = get_coord_from_statement('인제')
    print(coord)
    weather_obj = get_weather_from_coord(coord[1])
    print(weather_obj)
    print(get_weather_string(coord[0],weather_obj))

    coord = get_coord_from_statement('고성')
    print(coord)
