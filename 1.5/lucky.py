# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/17
#  */
import web,json
from luckydata import checkuser,reviseuser,luckrandom,luckylog,checkusername,mylucky

urls = (
    '/','Index',
    '/lucky','Lucky',
    '/luckynumber','Luckynumber',
    '/luckylog','Luckylog',
    '/mylucky','Mylucky',
)

renter = web.template.render('templates')

class Index(object):
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        ip = web.ctx.ip
        data = web.input()
        user = data.get('user')
        if user:
            luckynnumber = checkusername(user)
            if len(str(luckynnumber))>2:
                a = json.loads(luckynnumber)
                if a['id'] == 'Null':
                    user = None
                    return renter.index(user, luckynnumber)
            return renter.index(user, luckynnumber)
        else:
            user = None
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

class Mylucky(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        data = web.input()
        user = data.get('user')
        user = str(user)
        if user == "None": raise web.seeother('/')
        return mylucky(user)

if __name__ == '__main__':
    web.application(urls,globals()).run()

#app = web.application(urls, globals())
#app = app.wsgifunc()
