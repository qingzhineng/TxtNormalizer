#!/usr/bin/python
# -*- coding: gbk -*-

from FicKit import *
import codecs, os, glob

uP2Space = P2Space.decode('gbk')
RES_SUBFIX = '.ret'

#=============Frame Work=============
def FileChange(fs_name, line_fns):
    name_short, name_ext = os.path.splitext(fs_name)
    ft_name = name_short + RES_SUBFIX
    
    with open(fs_name, 'r') as fs, open(ft_name, 'w') as ft:
        for line in fs:
            for fn in line_fns:
                line = fn(line)
                if line is None or line == '':
                    break
            if line is not None and line != '':
                ft.write(line)

def FileChangeU(fs_name, line_fns):
    name_short, name_ext = os.path.splitext(fs_name)
    ft_name = name_short + RES_SUBFIX
    
    with codecs.open(fs_name, 'r', 'gbk') as fs, codecs.open(ft_name, 'w', 'gbk') as ft:
        for line in fs:
            for fn in line_fns:
                line = fn(line)
                if line is None or line == '':
                    break
            if line is not None and line != '':
                ft.write(line)



#==============Processors=================
def AddP2Space(line):
    '''ɾ�����У���ֻ�лس����ŵ���
    ������ǿ��У���ɾ��һ��ͷβ�Ŀո񣬲���β�����²��ϻس�
    ��ͷ�����2�����Ŀո�
    '''
    line = line.strip()
    if not len(line):    #��ȥ����
        return None
    if not line.startswith(P2Space):
        line = P2Space+line+CR
    return line

def AddP2SpaceCR(line):
    line = line.strip()
    if len(line) and not line.startswith(P2Space):    #���ǿ��У����Ҳ�һ˫�ո�ͷ
        line = P2Space+line
    line += CR
    return line


def StripLine(line):
    '''��ȥǰ��Ŀհ׷���ɾ������
    �Ա�AddP2Spaceֻ��û�м�ǰ��Ŀո�
    '''
    line = line.strip()
    if len(line):
        return line+CR
    else:
        return None

AddTail = lambda line: line + CR


#============Unicode===================
def AddP2SpaceU(line):
    line = line.strip()    #�Ѿ���uP2Space��strip����
    if not len(line):    #��ȥ����
        return None
    # if not line.startswith(uP2Space): #�����ж��ˣ�strip�󶼲�������uP2Space��ͷ��
    line = uP2Space+line+CR
    return line

def AddP2SpaceCRU(line):
    line = line.strip()    #�Ѿ���uP2Space��strip����
    if len(line):
        # if not line.startswith(uP2Space): #�����ж��ˣ�strip�󶼲�������uP2Space��ͷ��
        line = uP2Space+line
    line += CR
    return line





#===============Test===============
# os.chdir('F:\\public\\Test')
# txt_list = glob.glob('*.txt')

# for i in txt_list:
    # FileChange(i, AddP2SpaceCR) 

os.chdir('F:\\NetTxt')
file_name = 'Ǯ����.txt'
FileChange(file_name, [AddP2Space, AddTail])