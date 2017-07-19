# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/17
#  */
import web
import json
import time
from luckydata import luckrandom,playnum

urls = (
    '/','Index',
    '/lucky','Lucky',
    '/luckynumber','Luckynumber',
)

renter = web.template.render('templates')
userlist = [3]

class Index(object):
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        data = web.input()
        username = data.get('user')
        userlist.append(username)
        return renter.index()
    def POST(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        data = web.input()
        username = data.get('username')
        userlist.append(username)
        times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        #print username,times
        raise web.seeother('/?user=%s'%username)

class Lucky(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return luckrandom(playnum('Benjamin'))

class Luckynumber(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        data = {'luckynnumber':0,}
        data = json.dumps(data, indent=2, ensure_ascii=False)
        return data

if __name__ == '__main__':
    web.application(urls,globals()).run()
