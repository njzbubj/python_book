'''
Created on 2018/03/14

@author: miyazawataishi
'''
import requests
import json

apikey = "474d59dd890c4108f62f192e0c6fce01"
#apikey = "3a232bdb208fe88f0f9e3654153ab992"

cities = ["Tokyo,JP", "London,UK"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

k2c = lambda k: k - 273.15

for name in cities:
    url = api.format(city=name, key=apikey)
    r = requests.get(url)
    print(r.text)
    data = json.loads(r.text)

    print("ー都市：", data["name"])
    print("　天気：", data["weather"][0]["description"])
    print("　最低気温：", k2c(data["main"]["temp_min"]))
    print("　最高気温：", k2c(data["main"]["temp_max"]))
    print("")
