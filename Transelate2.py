#!/usr/bin/python
# -*- coding: gbk -*-

import re
CR = '\n'

def UpdateFile(fname, processors):
    """�ļ����� processors��д��Դ�ļ�����
    """
    with open(fname, 'r') as f:
        c = f.read()
    for fn in processors:
        c = fn(c)
    with open(fname, 'w') as f:
        f.write(c)

def CodeTranslate(fname, code_s, code_d):
    """ת���ļ����� 
    """
    coder = lambda s : s.decode(code_s, 'ignore').encode(code_d, 'ignore')
    UpdateFile(fname, [coder])

num_cl = lambda s : re.sub(r'\d+', '', s)    #ɾ���ļ��е�����
num_footer_cl = lambda s : re.sub(r'��|��|��|��|��|��|��|��|��|��', '', s)    #ɾ����ע
brace_cl = lambda s : s.replace('����', '')    #ɾ��������
brace2_cl = lambda s : s.replace('()', '')    #ɾ��������

# =====================win linux ת������============
def PyHeadSet(fname, set_name):
    '''�ı�Py�ļ��ı��벢�Ҹı�ͷ������
    '''
    head = '#!/usr/bin/python\n# -*- coding: %s -*-\n\n' % set_name
    with open(fname, 'r') as f:
        while True:
            offset = f.tell()
            line = f.readline().strip()
            if len(line) and not line.startswith('#'):    #�����ǿ����Ҳ���#��ͷֹͣ
                f.seek(offset)    #�˻ص���ǰ�еĿ�ʼ
                break
        rest = f.read()    #�������µ��ַ�
    
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
# file_name = '����Ԫ-����.txt'    
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
# file_name = '���-ϴ��.txt'
# CodeTranslate(file_name, 'utf-8', 'gbk')

