# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/17
#  */
import web,json
from luckydata import checkuser,reviseuser,luckrandom,luckylog,checkusername,mylucky
from admin import alluserdata,deluser,edituser

urls = (
    '/','Index',
    '/lucky','Lucky',
    '/luckynumber','Luckynumber',
    '/luckylog','Luckylog',
    '/mylucky','Mylucky',
    '/admin','Admin',
    '/alluserdata','Alluserdata',
    '/deluser','Deluser',
    '/edituser','Edituser',
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
            if len(str(luckynnumber))>4:
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

class Admin(object):
    def GET(self):
        return renter.admin()

class Alluserdata(object):
    def GET(self):
        return alluserdata()

class Deluser(object):
    def GET(self):
        data = web.input()
        user = data.get('user')
        user = str(user)
        deluser(user)
        raise web.seeother('/admin')

class Edituser(object):
    def GET(self):
        raise web.seeother('/admin')
    def POST(self):
        data = web.input()
        user = data.get('user')
        times = data.get('times')
        user = str(user)
        times = str(times)
        edituser(user,times)
        raise web.seeother('/admin')

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

def internalerror():
    return web.internalerror("Bad, bad server. No donut for you.")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.notfound = notfound
    app.internalerror = internalerror
    app.run()

# app = web.application(urls, globals())
# app.notfound = notfound
# app.internalerror = internalerror
# app = app.wsgifunc()
