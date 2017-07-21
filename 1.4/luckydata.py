# coding:utf-8
import time
import random
import json

def userlists(data):
    f = file('userlist.txt','w+')
    f.write(data)
    f.close()

userlist = [{'Benjamin': 3, 'time': '2017-07-19 17:56:47'}]

def adduser(user,playnum=3):
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    dict = {
        user:playnum,
        'time':times,
    }
    userlist.append(dict)
    return dict

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

def jsondata(user='',id='',angle='',text='',playnum=''):
    data = {
        'user:':user,
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



b = 0

if b!=None:
    print 0
else:
    print 1