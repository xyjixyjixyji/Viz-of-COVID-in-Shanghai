# -*- coding:utf-8 -*-
import pandas as pd
import re
import csv
date = [] #日期数据清单
for i in date:
    f = pd.read_csv(i+'.csv',engine='python')
    f_ = []
    f = f.dropna(axis=0)
    for sent in f['text']:
        s = re.split(r'[，。？ ！.+@…]', sent)
        f_ += s
    while '' in f_:
        f_.remove('')
    dict = {'text':f_}
    df = pd.DataFrame(dict)
    df.to_csv('new'+i+'.csv')
