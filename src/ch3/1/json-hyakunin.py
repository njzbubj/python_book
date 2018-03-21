'''
Created on 2018/03/19

@author: miyazawataishi
'''
import urllib.request as req
import os.path, random
import json

url = "http://api.aoikujira.com/hyakunin/get.php?fmt=json"
savename = "hyakunin.json"
if not os.path.exists(url):
    req.urlretrieve(url, savename)

data = json.load(open(savename, "r", encoding="utf-8"))

r = random.choice(data)
print(r['kami'], r['simo'])
