'''
Created on 2018/03/19

@author: miyazawataishi
'''
filename = "a.bin"
data = 100
with open(filename, "wb") as f:
    f.write(bytearray([data]))