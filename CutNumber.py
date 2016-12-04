#!/usr/bin/python
# -*- coding: gbk -*-

import os
from FicKit import *

#================Part 1=====================
def GetTitles(content, start, stop, opt=0):
    """����content�������ڵ���ʼλ�ã����Ϊ[start-stop]
    Head ===== Number Space Title
    opt = 0  head
    opt = 1 title    
    """    
    titles = []
    for i in range(start, stop+1):
        num_txt = NumChina(i)
        para_tag_txt = '��' + num_txt + '�� '    #�»������Ĺ���ע��հ׷��Ƿ�Ϊ��Ŀո�
        print para_tag_txt
        idx = content.index(para_tag_txt)    #���Ҷ�Ӧ������ֵ
        idx2 = content.index(CR, idx)
        head = content[idx : idx2+1]        #���س���Ҳ����title��
        if opt == 0:
            titles.append(head)
        else:
            number, title = head.split(' ', 1)
            titles.append(title)
    return titles

def FindTagIdx(content, start, stop):
    """����content�������ڵ���ʼλ�ã����Ϊ[start-stop]
    
    """
    idx_sep = []
    for i in range(start, stop+1):
        num_txt = NumChina(i)
        para_tag_txt = '��' + num_txt + '��'    #�»������Ĺ���ע��հ׷��Ƿ�Ϊ��Ŀո�
        idx = content.index(para_tag_txt)    #���Ҷ�Ӧ������ֵ
        idx_sep.append(idx)
    idx_sep.append(len(content))    #�ļ��ܳ���
    return idx_sep

def SaveSepFiles(content, start, stop, idx_sep):
    """��content�����ı����ݰ��ձ����ʼλ������ָ��Ϊ�������ı��ļ�
    �ļ��ı��Ϊ[start-stop].txt
    
    """
    for i in range(0, stop-start+1):    #start - PARA_STOP��
        si = str(i+start)
        print si
        print idx_sep[i], idx_sep[i+1]
        fi_name = si + '.txt'
        fi = open(fi_name, 'w')
        fi.write(content[idx_sep[i]:idx_sep[i+1]-1])
        fi.close()

def SlashFile(fname,  wd, start, stop):
    '''�ֽ��ļ���Ϊ��Ϊ���½ڵ�С�ļ�
    '''
    with open(fname, 'r') as fd:
        content = fd.read()
    if not os.path.exists(wd):
        os.makedirs(wd)
    os.chdir(wd)
    
    idx_sep = FindTagIdx(content, start, stop)
    SaveSepFiles(content, start, stop, idx_sep)

os.chdir('D:\\Python2Prj\\FicCutFun')
fname = '���-ϴ��.txt' 
wd = '.\\Out'
start = 1
stop = 3
SlashFile(fname,  wd, start, stop)
       



