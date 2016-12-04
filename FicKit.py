#!/usr/bin/python
# -*- coding: gbk -*-

CR = '\n'
P2Space = '����'

def CharsetDetect(s):
    """����ַ���s�ı�����utf8����gbk
    """
    try:
        set_name = 'utf-8'
        us = s.decode(set_name)
    except UnicodeDecodeError:
        set_name = 'gbk'
        us = s.decode(set_name)
    finally:
        return set_name, us
        
def NumChina(x):
    # ����Ĵ���
    if x == 0:
        return '��'
    number_map = {
        0:'��',
        1:'һ',
        2:'��',
        3:'��',
        4:'��',
        5:'��',
        6:'��',
        7:'��',
        8:'��',
        9:'��'
    }
    unit = ['��', 'ʮ', '��', 'ǧ']
    
    nw = []
    while x:
        x, y = divmod(x, 10)    #�õ�������������ת��Ϊ����������
        nw.append(number_map[y])
    su = len(nw) - 1
    su_old = su
    m = []
    while nw:
        cur = nw.pop()
        if cur == '��':
            if len(nw) != 0:    #����治��Ҫ�õ�λ�������һλ���㲻��
                m.append(cur)
        else:
            if len(nw) != 0:    #��������������һλ���ӵ�λ
                m.append(cur + unit[su])
            else:
                m.append(cur)
        su -= 1
    #    ��һʮ һ�� һʮ ����������������Ĵ���
    if su_old == 1:
        if m[0] == 'һʮ':
            m[0] = 'ʮ'
    return ''.join(m)

def NumChinaParseInt(s):
    number_map = {
        u'��' : 0,
        u'һ' : 1,
        u'��' : 2,
        u'��' : 3,
        u'��' : 4,
        u'��' : 5,
        u'��' : 6,
        u'��' : 7,
        u'��' : 8,
        u'��' : 9
    }
    unit_map =  {
        u'ʮ': 10,
        u'��': 100,
        u'ǧ': 1000
    }
    
    s = s.lstrip('��')    #ȥ����ͷ��
    s = s.decode('gbk')    #ת��Ϊunicode
    n = len(s)
    i = 0    #�ַ�������
    total = 0    #�������
    if s[0] != u'ʮ':    #����ʮ��ͷ 
        bNumber = True
    else:
        bNumber = False
        ni = 1
    while i<n:
        c = s[i]
        if bNumber:    #������Ϊ����
            ni =  number_map[c]
            if ni !=  0:
                bNumber = False
        else:
            ui = unit_map[c]
            total += ni*ui
            bNumber = True
        if i == n-1:
            if bNumber == True:    #���һλΪ��λ���ڴ�����
                return total
            else:    #���һλΪ���֣��ڴ���λ
                return total+ni
        i += 1
 
# print ChinaParseInt('һǧһ����ʮ��')
# print ChinaParseInt('һǧ����ʮ��')
# print ChinaParseInt('һǧ����ʮ')
# print ChinaParseInt('һǧһ�����')
# print ChinaParseInt('һǧ���') 
# print ChinaParseInt('ʮ��') 
# print ChinaParseInt('ʮ')
