# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/23
#  */
import json
import time
import random
import sys
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

def luckylog(data):
    f = file('luckylog.txt', 'a')
    f.write(str(data)+'\n')

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

def luckrandom(user, playnum):
    idrandom = random.randint(0, 100000000)
    print idrandom
    if playnum > 0:
        if idrandom <=20000000:
            id = 1
            savelog(user,id,playnum)
            return jsondata(user, id, 0, str(config[str(id)]), playnum)
        if idrandom >20000000 and idrandom <= 40000000:
            id = 2
            return jsondata(user, id, 60, str(config[str(id)]), playnum)
        if idrandom > 40000000 and idrandom <= 48000000:
            id = 3
            savelog(user, id, playnum)
            return jsondata(user, id, 120, str(config[str(id)]), playnum)
        if idrandom > 45000000 and idrandom <= 50000000:
            id = 4
            savelog(user, id, playnum)
            return jsondata(user, id, 180, str(config[str(id)]), playnum)
        if idrandom > 50000000 and idrandom<=70000000:
            id = 5
            return jsondata(user, id, 240, str(config[str(id)]), playnum)
        if idrandom > 70000000 and idrandom <= 100000000:
            id = 6
            savelog(user, id, playnum)
            return jsondata(user, id, 300, str(config[str(id)]), playnum)
        else:
            return jsondata('Null', 0, '数据异常！', playnum)
    else:
        return jsondata(user, 'Null', 0, '抽奖次数不足', playnum)