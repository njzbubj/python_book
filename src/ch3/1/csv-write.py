'''
Created on 2018/03/19

@author: miyazawataishi
'''
import csv, codecs

with codecs.open("test.csv", "w", "shift_jis")as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["ID", "商品名", "値段"])
    writer.writerow(["100", "りんご", 100])
    writer.writerow(["101", "みかん", 200])
