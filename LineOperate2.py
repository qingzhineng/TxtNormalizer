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
    '''删除空行，即只有回车符号的行
    如果不是空行，则删除一行头尾的空格，并在尾部重新补上回车
    在头部添加2个中文空格
    '''
    line = line.strip()
    if not len(line):    #剔去空行
        return None
    if not line.startswith(P2Space):
        line = P2Space+line+CR
    return line

def AddP2SpaceCR(line):
    line = line.strip()
    if len(line) and not line.startswith(P2Space):    #不是空行，而且不一双空格开头
        line = P2Space+line
    line += CR
    return line


def StripLine(line):
    '''剔去前后的空白符并删除空行
    对比AddP2Space只是没有加前面的空格
    '''
    line = line.strip()
    if len(line):
        return line+CR
    else:
        return None

AddTail = lambda line: line + CR


#============Unicode===================
def AddP2SpaceU(line):
    line = line.strip()    #已经把uP2Space给strip掉了
    if not len(line):    #剔去空行
        return None
    # if not line.startswith(uP2Space): #无需判断了，strip后都不会有以uP2Space开头了
    line = uP2Space+line+CR
    return line

def AddP2SpaceCRU(line):
    line = line.strip()    #已经把uP2Space给strip掉了
    if len(line):
        # if not line.startswith(uP2Space): #无需判断了，strip后都不会有以uP2Space开头了
        line = uP2Space+line
    line += CR
    return line





#===============Test===============
# os.chdir('F:\\public\\Test')
# txt_list = glob.glob('*.txt')

# for i in txt_list:
    # FileChange(i, AddP2SpaceCR) 

os.chdir('F:\\NetTxt')
file_name = '钱神论.txt'
FileChange(file_name, [AddP2Space, AddTail])