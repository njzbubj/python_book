'''
Created on 2018/02/22

@author: miyazawataishi
'''
import urllib.request

url="http://uta.pw/shodou/img/28/214.png"
savename="test2.png"

mem=urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("保存しました")
