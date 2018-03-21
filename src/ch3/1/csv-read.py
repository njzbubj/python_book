'''
Created on 2018/03/19

@author: miyazawataishi
'''
import codecs

filename = "test.csv"
csv = codecs.open(filename, "r", "shift_jis").read()

data = []
rows = csv.split("¥r¥n")
for row in rows:
    if row == "": continue
    cells = row.split(",")
    data.append(cells)

for c in data:
    print(c[1], c[2])
