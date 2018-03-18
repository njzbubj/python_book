'''
Created on 2018/03/13

@author: miyazawataishi
'''
import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

text = r.text
print(text)

bin = r.content
print(bin)
