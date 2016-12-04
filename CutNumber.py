#!/usr/bin/python
# -*- coding: gbk -*-

import os
from FicKit import *

#================Part 1=====================
def GetTitles(content, start, stop, opt=0):
    """查找content里编号所在的起始位置，编号为[start-stop]
    Head ===== Number Space Title
    opt = 0  head
    opt = 1 title    
    """    
    titles = []
    for i in range(start, stop+1):
        num_txt = NumChina(i)
        para_tag_txt = '第' + num_txt + '回 '    #章回命名的规则，注意空白符是否为真的空格
        print para_tag_txt
        idx = content.index(para_tag_txt)    #查找对应的索引值
        idx2 = content.index(CR, idx)
        head = content[idx : idx2+1]        #将回车符也算在title里
        if opt == 0:
            titles.append(head)
        else:
            number, title = head.split(' ', 1)
            titles.append(title)
    return titles

def FindTagIdx(content, start, stop):
    """查找content里编号所在的起始位置，编号为[start-stop]
    
    """
    idx_sep = []
    for i in range(start, stop+1):
        num_txt = NumChina(i)
        para_tag_txt = '第' + num_txt + '部'    #章回命名的规则，注意空白符是否为真的空格
        idx = content.index(para_tag_txt)    #查找对应的索引值
        idx_sep.append(idx)
    idx_sep.append(len(content))    #文件总长度
    return idx_sep

def SaveSepFiles(content, start, stop, idx_sep):
    """将content整个文本内容按照编号起始位置数组分割成为单个的文本文件
    文件的编号为[start-stop].txt
    
    """
    for i in range(0, stop-start+1):    #start - PARA_STOP中
        si = str(i+start)
        print si
        print idx_sep[i], idx_sep[i+1]
        fi_name = si + '.txt'
        fi = open(fi_name, 'w')
        fi.write(content[idx_sep[i]:idx_sep[i+1]-1])
        fi.close()

def SlashFile(fname,  wd, start, stop):
    '''分解文件成为成为单章节的小文件
    '''
    with open(fname, 'r') as fd:
        content = fd.read()
    if not os.path.exists(wd):
        os.makedirs(wd)
    os.chdir(wd)
    
    idx_sep = FindTagIdx(content, start, stop)
    SaveSepFiles(content, start, stop, idx_sep)

os.chdir('D:\\Python2Prj\\FicCutFun')
fname = '杨绛-洗澡.txt' 
wd = '.\\Out'
start = 1
stop = 3
SlashFile(fname,  wd, start, stop)
       



