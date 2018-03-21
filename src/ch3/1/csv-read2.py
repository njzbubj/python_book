'''
Created on 2018/03/19

@author: miyazawataishi
'''
import csv, codecs

filename = "test.csv"
fp = codecs.open(filename, "r", "shift_jis")

reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])
