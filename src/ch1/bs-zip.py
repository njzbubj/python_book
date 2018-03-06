'''
Created on 2018/03/05

@author: miyazawataishi
'''
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://api.aoikujira.com/zip/xml/3630011"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

ken = soup.find("ken").string
shi = soup.find("shi").string
cho = soup.find("cho").string

print(ken, shi, cho)
