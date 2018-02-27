#!/usr/bin/env python3
'''
Created on 2018/02/23

@author: miyazawataishi
'''
import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("引数がありません")
    sys.exit()
keyword = sys.argv[1]

API = "http://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt":"ini",
    "key":keyword
}
params = parse.urlencode(query)
url = API + "?" + params
print("url=", url)

with req.urlopen(url) as r:
    b = r.read()
    data = b.decode('utf-8')
    print(data)
