#-*- encoding=utf-8 -*-
import pandas as pd
from snownlp import SnowNLP
import json
import csv
import random
date = [] #日期数据清单

res_list_all = []
emo_list_all = []
for da in range(2,31):
    i = "4_"+str(da)
    if(date.count(i)>0):
        vlist = []
        f = pd.read_csv('purified_data//'+i+'.csv',engine='python')
        for sent in range(len(f['text'])):
            vlist += SnowNLP(f['text'][sent]).words
        
        res_dict = {}
        #进行词频统计
        for ii in vlist:
            res_dict[ii] = res_dict.get(ii,0) + 1
        res_list = list(res_dict.items())
        #降序排序
        res_list.sort(key = lambda x:x[1], reverse = True)
        fin_res_list = []

        #去除单个字的词
        for item in res_list:
            if(len(item[0])>=2):
                fin_res_list.append(item)
        fin_res_list = fin_res_list[:12]
        res_list_all.append(fin_res_list)
        
        f2 = pd.read_csv('new'+i+'.csv',engine='python')
        emo_list = []
        for sent in range(len(f2['text'])):
            ans = SnowNLP(f['text'][sent])
            emo_list += [ans.sentiments]
        emo_list_all.append(emo_list)

for da in range(1,28):
    i = "5_"+str(da)
    if(date.count(i)>0):
        vlist = []
        f = pd.read_csv('new'+i+'.csv',engine='python')
        for sent in range(len(f['text'])):
            vlist += SnowNLP(f['text'][sent]).words
        
        res_dict = {}
        #进行词频统计
        for ii in vlist:
            res_dict[ii] = res_dict.get(ii,0) + 1
        res_list = list(res_dict.items())
        #降序排序
        res_list.sort(key = lambda x:x[1], reverse = True)
        fin_res_list = []

        #去除单个字的词
        for item in res_list:
            if(len(item[0])>=2):
                fin_res_list.append(item)
        fin_res_list = fin_res_list[:12]
        res_list_all.append(fin_res_list)

        f2 = pd.read_csv('new'+i+'.csv',engine='python')
        emo_list = []
        for sent in range(len(f2['text'])):
            ans = SnowNLP(f['text'][sent])
            emo_list += [ans.sentiments]
        emo_list_all.append(emo_list)


path = 'total_count.txt'
file1=open(path, 'w',encoding='utf8')
for fin_r in res_list_all:
    file1.write('[\''+str(fin_r[0][0])+'\'')
    for item in fin_r[1:]:
        file1.write(','+'\''+str(item[0])+'\'')
    file1.write(']\n')
for fin_r in res_list_all: 
    file1.write('['+'\''+str(fin_r[0][1])+'\'')
    for item in fin_r[1:]:
        file1.write(','+'\''+str(item[1])+'\'')
    file1.write(']\n')

path2 = 'total_senti.txt'
file2=open(path2, 'w',encoding='utf8')
for emo in emo_list_all:
    file2.write('['+str(emo[0]))
    for senti in emo[1:]:
        file2.write(',')
        file2.write(str(senti))
    file2.write('],\n')
