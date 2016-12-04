#!/usr/bin/python
# -*- coding: gbk -*-

import re
CR = '\n'

def UpdateFile(fname, processors):
    """文件更新 processors，写回源文件覆盖
    """
    with open(fname, 'r') as f:
        c = f.read()
    for fn in processors:
        c = fn(c)
    with open(fname, 'w') as f:
        f.write(c)

def CodeTranslate(fname, code_s, code_d):
    """转换文件编码 
    """
    coder = lambda s : s.decode(code_s, 'ignore').encode(code_d, 'ignore')
    UpdateFile(fname, [coder])

num_cl = lambda s : re.sub(r'\d+', '', s)    #删除文件中的数字
num_footer_cl = lambda s : re.sub(r'①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩', '', s)    #删除脚注
brace_cl = lambda s : s.replace('（）', '')    #删除空括号
brace2_cl = lambda s : s.replace('()', '')    #删除空括号

# =====================win linux 转换函数============
def PyHeadSet(fname, set_name):
    '''改变Py文件的编码并且改变头部申明
    '''
    head = '#!/usr/bin/python\n# -*- coding: %s -*-\n\n' % set_name
    with open(fname, 'r') as f:
        while True:
            offset = f.tell()
            line = f.readline().strip()
            if len(line) and not line.startswith('#'):    #遇到非空行且不以#开头停止
                f.seek(offset)    #退回到当前行的开始
                break
        rest = f.read()    #读出余下的字符
    
    with open(fname, 'w') as f:
        f.write(head)
        f.write(rest)

def Win2Unix(fname):
    with open(fname, 'rb') as f:
        c = f.read()
    c = c.replace('\r\n', '\n')
    with open(fname, 'wb') as f:
        f.write(c)

def Unix2Win(fname):
    with open(fname, 'rb') as f:
        c = f.read()
    c = c.replace('\n', '\r\n')
    with open(fname, 'wb') as f:
        f.write(c)

# ================Test=================
import os, glob
# os.chdir(r'F:\public\GSW')
# file_name = '柳宗元-三戒.txt'    
# UpdateFile( file_name, [num_footer_cl, brace_cl])

wd = 'D:\\FicCutFun'
os.chdir(wd)
SRC_SET = 'gbk'
DST_SET = 'utf-8'

l = glob.glob('*.py')
for i in l:
    print i
    CodeTranslate(i, SRC_SET, DST_SET)
    PyHeadSet(i, DST_SET)
    Win2Unix(i)
# os.chdir('D:\\Python2Prj\\FicCutFun')
# file_name = '杨绛-洗澡.txt'
# CodeTranslate(file_name, 'utf-8', 'gbk')

