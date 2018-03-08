'''
Created on 2018/03/08

@author: miyazawataishi
'''
from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print(urljoin(base, "/hoge.html"))
print(urljoin(base, "http://kujirahand.com/wiki"))
print(urljoin(base, "//uta.pw/shodou"))