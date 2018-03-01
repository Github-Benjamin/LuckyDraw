# coding:utf-8
import time
import random
import json

userlist = [{'Benjamin': 3, 'time': '2017-07-19 17:56:47'}]

def adduser(user,playnum=3):
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    dict = {
        user:playnum,
        'time':times,
    }
    userlist.append(dict)

def reviseuser(user,playnum):
    for i in userlist:
        if i.has_key(user):
            times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            i[user] = playnum
            i['time'] = times

def lookupuser(user):
    for i in userlist:
        if i.has_key(user):
            return i[user]

def jsondata(id='',angle='',text='',playnum=''):
    data = {
        'id': id,
        'angles':angle,
        'name': text,
        'playnum':playnum,
    }
    s = json.dumps(data, indent=2, ensure_ascii=False)
    return s

def playnum(user):
    playnum = lookupuser(user)
    if playnum>0:
        playnum = playnum - 1
        reviseuser(user,playnum)
        return lookupuser(user)
    else:
        return -1

def luckrandom(playnum):
    id = random.randint(1,6)
    if playnum>=0:
        if id == 1:
            return jsondata(id,0, '恭喜您抽中理财金2000元！',playnum)
        if id == 2:
            return jsondata(id,60, '很遗憾未中奖，谢谢参与！',playnum)
        if id == 3:
            return jsondata(id,120, '恭喜您抽中理财金5200元！',playnum)
        if id == 4:
            return jsondata(id,180, '恭喜您抽中100元京东卡一张！',playnum)
        if id == 5:
            return jsondata(id,240, '很遗憾未中奖，谢谢参与！',playnum)
        if id == 6:
            return jsondata(id,300, '恭喜您抽中理财金1000元！',playnum)
        else:
            return jsondata('Null',0, '数据异常！',playnum)
    else:
        return jsondata('Null', 0, '抽奖次数不足', playnum)
