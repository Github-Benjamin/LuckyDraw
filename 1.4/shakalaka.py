# coding:utf-8
import json
import time
import random

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

def checkuser(user):
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
                playnum = checkuser(user) - 1
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


def luckrandom(user, playnum):
    id = random.randint(1, 6)
    if playnum > 0:
        if id == 1:
            return jsondata(user, id, 0, '恭喜您抽中理财金2000元！', playnum)
        if id == 2:
            return jsondata(user, id, 60, '很遗憾未中奖，谢谢参与！', playnum)
        if id == 3:
            return jsondata(user, id, 120, '恭喜您抽中理财金5200元！', playnum)
        if id == 4:
            return jsondata(user, id, 180, '恭喜您抽中100元京东卡一张！', playnum)
        if id == 5:
            return jsondata(user, id, 240, '很遗憾未中奖，谢谢参与！', playnum)
        if id == 6:
            return jsondata(user, id, 300, '恭喜您抽中理财金1000元！', playnum)
        else:
            return jsondata('Null', 0, '数据异常！', playnum)
    else:
        return jsondata(user, 'Null', 0, '抽奖次数不足', playnum)


