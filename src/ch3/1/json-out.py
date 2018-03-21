'''
Created on 2018/03/19

@author: miyazawataishi
'''
import json

price = {
    "date": "2018-03-18",
    "price": {
        "Apple": 80,
        "Orange": 90
        }
    }

s = json.dumps(price)
print(s)
