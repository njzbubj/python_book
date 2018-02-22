'''
Created on 2018/02/22

@author: miyazawataishi
'''
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url, savename)
print("保存しました")
