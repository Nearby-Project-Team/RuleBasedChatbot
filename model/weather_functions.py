import re
import requests
import datetime as dt

def get_coord_from_statement(statement):
    target_cities = ["서울", "부산","인천","대구","대전",
    "광주","울산","세종",
    "경기","강원","충청","충청북","충청남",
    "전라","전라북","전라남",
    "경상","경상북","경상남","제주"]
    trans_coord = [(60, 127),(98, 76), (55, 124), (89, 90), (67, 100),
    (58, 74),(102, 84),(66, 103),
    (60, 120),(73, 134),(69, 107),(69, 107),(68, 100),
    (63, 89),(63, 89),(51, 67),
    (89, 91),(89, 91),(91, 77),(52, 38)
    ]
    for i in range(len(target_cities)):
        if(re.search(target_cities[i],statement) is not None):
            return trans_coord[i]
    return None

def get_weather_from_coord(coord):
    api_key = r'api_key'
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

def get_weather_string(weather_state):
    temp = weather_state[0]
    wthr = weather_state[1]

    temp = number_to_temp_hangul(temp)
    wthr = index_to_weather(wthr) 
    return "현재 {}이고, {}.".format(temp,wthr)

if __name__ == '__main__':
    coord = get_coord_from_statement('서울 날씨')
    print(coord)
    weather_obj = get_weather_from_coord(coord)
    print(weather_obj)
    
    print(get_weather_string((-10.2,3)))
    weather_string = get_weather_string(weather_obj)
    print(weather_string)

