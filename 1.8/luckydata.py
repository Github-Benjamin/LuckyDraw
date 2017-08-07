# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/23
#  */
import json
import time
import random
import sys
import re
from decimal import *
reload(sys)
sys.setdefaultencoding('utf8')

config = {'1':'恭喜您抽中理财金2000元！','2':'很遗憾未中奖，谢谢参与！','3':'恭喜您抽中理财金5200元！','4':'恭喜您抽中100元京东卡一张！','5':'很遗憾未中奖，谢谢参与！','6':'恭喜您抽中理财金1000元！'}

def save(data):
    s = json.dumps(data,indent=2,ensure_ascii=False)
    f = open('userlist.txt','w+')
    f.write(s)
    f.close()

def load():
    f = open('userlist.txt', 'r')
    s = f.read()
    return json.loads(s)

def adduser(user,playnum):
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    dict = {
        user:playnum,
        'time':times,
    }
    return dict

def lookupuser(data,user):
    for i in data:
        if i.has_key(user):
            return i[user]

def checkusername(user):
    if user==None or user == 'None':
        return jsondata('Null', 'Null', 0, '用户名为空', 0)
    else:
        a = load()
        b = lookupuser(a, user)
        if b!=None:
            if b == 0:
                return 0
            else:
                return b
        else:
            return jsondata('Null', 'Null', 0, '用户不存在,请输入用户名开始抽奖！', 0)

def checkuser(user):
    if user==None or user == 'None':
        return jsondata('Null', 'Null', 0, '用户名为空', 0)
    else:
        a = load()
        b = lookupuser(a, user)
        if b!=None:
            if b == 0:
                return 0
            else:
                return b
        else:
            a.append(adduser(user, 3))
            save(a)
            a = load()
            b = lookupuser(a, user)
            return b

def reviseuser(user):
    userlist = load()
    for i in userlist:
        if i.has_key(user):
            times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            if checkuser(user)>0:
                playnum = int(checkuser(user)) - 1
                i[user] = playnum
                i['time'] = times
                save(userlist)

def jsondata(user='',id='',angle='',text='',playnum=''):
    data = {
        'user':user,
        'id': id,
        'angles':angle,
        'idname': text,
        'playnum':playnum,
    }
    s = json.dumps(data, indent=2, ensure_ascii=False)
    return s

def logsave(data):
    s = json.dumps(data,indent=2,ensure_ascii=False)
    f = open('luckylog.txt','w+')
    f.write(s)
    f.close()

def logload():
    f = open('luckylog.txt', 'r')
    s = f.read()
    return json.loads(s)

# usr idname playnum time
def logjsondata(user='',text='',playnum=''):
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    data = {'user':user,'idnum': text,'playnum':playnum,'time':times,}
    return data

def savelog(user,idnum,playnum):
    data = logload()
    data.append(logjsondata(user,idnum,playnum))
    logsave(data)

def luckylog():
    datalist = []
    data = logload()
    data = data[-10:]
    for i in data:
         a = i['idnum']
         data = {'user': i['user'], 'idname': config[str(a)], 'time': i['time']}
         datalist.append(data)
    data = json.dumps(datalist, indent=2, ensure_ascii=False)
    return data

def mylucky(user):
    data = logload()
    mylucky = []
    for i in data:
        if i['user'] == user:
            a = i['idnum']
            data = {'idname': config[str(a)], 'time': i['time']}
            mylucky.append(data)
    if mylucky:
        return json.dumps(mylucky,indent=2, ensure_ascii=False)
    else:
        return json.dumps([{"idname":"暂无中奖记录!",'time':'',}],indent=2, ensure_ascii=False)

# 预留手机短信验证码
def vcode(user):
    vcode = random.randint(1000,9999)
    return vcode

# 判断是否为中文字符
def checkuserdata(user):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    user = u'%s'%user
    match = zhPattern.search(user)
    return match

# 接入中奖概率配置文件相关信息
import admin
list = admin.loadconf()

def luckrandom(user, playnum):
    num = Decimal(sum(list)).quantize(Decimal('0.00'))
    if num == 1:
        for x in range(6):
            if x == 0:
                one = list[x]
            if x == 1:
                two = one+list[x]
            if x == 2:
                three = two+list[x]
            if x == 3:
                four = three+list[x]
            if x == 4:
                five = four+list[x]
            if x == 5:
                six = five+list[x]
        one = Decimal(one * 100000000).quantize(Decimal('0'))
        two = Decimal(two * 100000000).quantize(Decimal('0'))
        three = Decimal(three * 100000000).quantize(Decimal('0'))
        four = Decimal(four * 100000000).quantize(Decimal('0'))
        five = Decimal(five * 100000000).quantize(Decimal('0'))
        six = Decimal(six * 100000000).quantize(Decimal('0'))
        if playnum > 0:
            idrandom = random.randint(0, 100000000)
            if idrandom <= one:
                id = 1
                savelog(user, id, playnum)
                return jsondata(user, id, 0, str(config[str(id)]), playnum)
            if one < idrandom <= two:
                id = 2
                return jsondata(user, id, 60, str(config[str(id)]), playnum)
            if two < idrandom <= three:
                id = 3
                savelog(user, id, playnum)
                return jsondata(user, id, 120, str(config[str(id)]), playnum)
            if three < idrandom <= four:
                id = 4
                savelog(user, id, playnum)
                return jsondata(user, id, 180, str(config[str(id)]), playnum)
            if four < idrandom <= five:
                id = 5
                return jsondata(user, id, 240, str(config[str(id)]), playnum)
            if five < idrandom <= six:
                id = 6
                savelog(user, id, playnum)
                return jsondata(user, id, 300, str(config[str(id)]), playnum)
            else:
                return jsondata('Null', 0, '数据异常！', playnum)
        else:
            return jsondata(user, 'Null', 0, '抽奖次数不足', playnum)
    else:
        return 'Number Error!'