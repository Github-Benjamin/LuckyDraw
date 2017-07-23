# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/17
#  */
import web
from luckydata import checkuser,reviseuser,luckrandom,luckylog,checkusername

urls = (
    '/','Index',
    '/lucky','Lucky',
    '/luckynumber','Luckynumber',
    '/luckylog','Luckylog',
)

renter = web.template.render('templates')

class Index(object):
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        data = web.input()
        user = data.get('user')
        if user:
            luckynnumber = checkusername(user)
        else:
            pass
            luckynnumber = None
        return renter.index(user,luckynnumber)
    def POST(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        data = web.input()
        user = data.get('username')
        checkuser(user)
        raise web.seeother('/?user=%s'%user)

class Lucky(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        data = web.input()
        user = data.get('user')
        user = str(user)
        if user == "None": raise web.seeother('/')
        if user:
            playnum =  str(checkusername(user))
            if playnum.isdigit():
                playnum = int(playnum)
                reviseuser(user)
                return luckrandom(user,playnum)
            else:
                return playnum
        else:
            return  checkusername(user)

class Luckynumber(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        data = web.input()
        user = data.get('user')
        user = str(user)
        #if user == 'None': return '\n\n  User is None!\n\n  Please input the UserName!'
        if user == "None": raise web.seeother('/')
        return checkusername(user)

class Luckylog(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        data = luckylog()
        return data

if __name__ == '__main__':
    web.application(urls,globals()).run()
