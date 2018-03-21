'''
Created on 2018/03/19

@author: miyazawataishi
'''
import yaml
from bokeh.colors.groups import yellow

yaml_str = """
Date: 2018-03-18
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 80
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 100
    -
        item_id: 1002
        name: Apple
        color: red
        price: 70
"""

data = yaml.load(yaml_str)

for item in data['PriceList']:
    print(item["name"], item["price"])
