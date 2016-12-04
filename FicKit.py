#!/usr/bin/python
# -*- coding: gbk -*-

CR = '\n'
P2Space = '　　'

def CharsetDetect(s):
    """检测字符串s的编码是utf8还是gbk
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
    # 对零的处理
    if x == 0:
        return '零'
    number_map = {
        0:'零',
        1:'一',
        2:'二',
        3:'三',
        4:'四',
        5:'五',
        6:'六',
        7:'七',
        8:'八',
        9:'九'
    }
    unit = ['个', '十', '百', '千']
    
    nw = []
    while x:
        x, y = divmod(x, 10)    #用迭代求余数方法转换为单个的数字
        nw.append(number_map[y])
    su = len(nw) - 1
    su_old = su
    m = []
    while nw:
        cur = nw.pop()
        if cur == '零':
            if len(nw) != 0:    #零后面不需要用单位，但最后一位的零不读
                m.append(cur)
        else:
            if len(nw) != 0:    #非零如果不是最后一位，加单位
                m.append(cur + unit[su])
            else:
                m.append(cur)
        su -= 1
    #    对一十 一、 一十 二、这种特殊情况的处理
    if su_old == 1:
        if m[0] == '一十':
            m[0] = '十'
    return ''.join(m)

def NumChinaParseInt(s):
    number_map = {
        u'零' : 0,
        u'一' : 1,
        u'二' : 2,
        u'三' : 3,
        u'四' : 4,
        u'五' : 5,
        u'六' : 6,
        u'七' : 7,
        u'八' : 8,
        u'九' : 9
    }
    unit_map =  {
        u'十': 10,
        u'百': 100,
        u'千': 1000
    }
    
    s = s.lstrip('零')    #去掉开头零
    s = s.decode('gbk')    #转码为unicode
    n = len(s)
    i = 0    #字符串索引
    total = 0    #解析结果
    if s[0] != u'十':    #不以十开头 
        bNumber = True
    else:
        bNumber = False
        ni = 1
    while i<n:
        c = s[i]
        if bNumber:    #读到的为数字
            ni =  number_map[c]
            if ni !=  0:
                bNumber = False
        else:
            ui = unit_map[c]
            total += ni*ui
            bNumber = True
        if i == n-1:
            if bNumber == True:    #最后一位为单位，期待数字
                return total
            else:    #最后一位为数字，期待单位
                return total+ni
        i += 1
 
# print ChinaParseInt('一千一百五十二')
# print ChinaParseInt('一千零五十二')
# print ChinaParseInt('一千零五十')
# print ChinaParseInt('一千一百零二')
# print ChinaParseInt('一千零二') 
# print ChinaParseInt('十二') 
# print ChinaParseInt('十')
