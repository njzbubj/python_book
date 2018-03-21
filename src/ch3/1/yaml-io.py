'''
Created on 2018/03/19

@author: miyazawataishi
'''
import yaml

customer = [
    { "name": "Yamada", "age": "30"},
    { "name": "Tanaka", "age": "20"},
    { "name": "Suzuki", "age": "25"}
]

yaml_str = yaml.dump(customer)
print(yaml_str)
print("------")

data = yaml.load(yaml_str)

for p in data:
    print(p["name"])
