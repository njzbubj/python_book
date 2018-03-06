'''
Created on 2018/03/06

@author: miyazawataishi
'''
from bs4 import BeautifulSoup
fp = open("books.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)
sel("#nu")
sel("li#nu")
sel("ul > li#nu")
sel("#bible #nu")
sel("#bible > #nu")
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(3)")

print(soup.select("li")[2].string)
print(soup.find_all("li")[2].string)
