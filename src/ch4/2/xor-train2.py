'''
Created on 2018/03/22

@author: miyazawataishi
'''
import pandas as pd
from sklearn import svm, metrics

xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
    ]

xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:, 0:1]
xor_label = xor_df.ix[:, 2]

clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)
print("予測結果：", pre)

as_score = metrics.accuracy_score(xor_label, pre)
print("正解率＝", as_score)
