# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/17
#  */
import web
import json
import random
import time

urls = (
    '/','Index',
    '/lucky','Lucky',
    '/luckynumber','Luckynumber',
)

renter = web.template.render('templates')
userlist = [3]

class Index(object):
    def GET(self):
        return renter.index()
    def POST(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        data = web.input()
        username = data.get('username')
        userlist.append(username)
        times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        #print username,times
        raise web.seeother('/')

def jsondata(id='',angle='',text='',playnum=''):
    data = {
        'id': id,
        'angles':angle,
        'name': text,
        'playnum':playnum,
    }
    s = json.dumps(data, indent=2, ensure_ascii=False)
    return s

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

def playnum():
    if userlist[0]>0:
        playnum = userlist[0]
        playnum = playnum - 1
        userlist[0] = playnum
        return playnum
    else:
        return -1

class Lucky(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return luckrandom(playnum())

class Luckynumber(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        data = {'luckynnumber':userlist[0],}
        data = json.dumps(data, indent=2, ensure_ascii=False)
        return data

if __name__ == '__main__':
    web.application(urls,globals()).run()
