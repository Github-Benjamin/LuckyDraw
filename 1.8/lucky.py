# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/17
#  */
import web,json
from luckydata import checkuser,reviseuser,luckrandom,luckylog,checkusername,mylucky,checkuserdata
from admin import alluserdata,deluser,edituser,saveconf,loadconf

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
    '/checkuserluckylog','Checkuserluckylog',
    '/luckyconf', 'Luckyconf',
    '/logout','Logout',
)

renter = web.template.render('templates')

class Index(object):
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        ip = web.ctx.ip
        user = session.user
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
        user = data.get('user')
        if checkuserdata(user):
            raise web.seeother('/')
        else:
            session.user = user
            checkuser(user)
            raise web.seeother('/')

class Lucky(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        user = session.user
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

class Logout(object):
    def GET(self):
        # session.kill()
        session.user = None
        raise web.seeother('/')

class Luckynumber(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        user = session.user
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
        user = session.user
        if str(user) == "None": raise web.seeother('/')
        return mylucky(user)

class Checkuserluckylog(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        admin = session.admin
        if admin == 'Benjamin':
            data = web.input()
            user = data.get('user')
            return mylucky(user)
        else:
            raise web.seeother('/admin')

class Admin(object):
    def GET(self):
        user = session.admin
        return renter.admin(user)
    def POST(self):
        data = web.input()
        admin = data.get('admin')
        pwd = data.get('pwd')
        if admin == 'Benjamin' and pwd == 'Benjamin':
            session.admin = admin
            raise web.seeother('/admin')
        else:
            raise web.seeother('/admin')

class Alluserdata(object):
    def GET(self):
        user = session.admin
        if user == 'Benjamin':
            return alluserdata()
        else:
            raise web.seeother('/admin')

class Deluser(object):
    def GET(self):
        user = session.admin
        if user == 'Benjamin':
            data = web.input()
            user = data.get('user')
            user = str(user)
            deluser(user)
            raise web.seeother('/admin')
        else:
            raise web.seeother('/admin')

class Edituser(object):
    def GET(self):
        raise web.seeother('/admin')
    def POST(self):
        user = session.admin
        if user == 'Benjamin':
            data = web.input()
            user = data.get('user')
            times = data.get('times')
            user = str(user)
            times = str(times)
            edituser(user,times)
            raise web.seeother('/admin')
        else:
            raise web.seeother('/admin')

class Luckyconf(object):
    def GET(self):
        user = session.admin
        if user == 'Benjamin':
            list = loadconf()
            return renter.luckyconf(list)
        else:
            raise web.seeother('/admin')
    def POST(self):
        user = session.admin
        if user == 'Benjamin':
            data = web.input()
            one = data.get('one')
            two = data.get('two')
            three = data.get('three')
            four = data.get('four')
            five = data.get('five')
            six = data.get('six')
            sumnum = float(one)+float(two)+float(three)+float(four)+float(five)+float(six)
            data = '%s,%s,%s,%s,%s,%s' % (one, two, three, four, five, six)
            if sumnum == 1:
                saveconf(data)
                raise web.seeother('/luckyconf')
            else:
                return 'Data Error'

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

def internalerror():
    return web.internalerror("Bad, bad server. No donut for you.")

if __name__ == "__main__":
    web.config.debug = False
    web.config.session_parameters['timeout'] = 10*60
    app = web.application(urls, globals())
    app.notfound = notfound
    app.internalerror = internalerror
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None,'admin':None})
    app.run()

# web.config.debug = False
# web.config.session_parameters['timeout'] = 10*60
# app = web.application(urls, globals())
# app.notfound = notfound
# app.internalerror = internalerror
# session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None,'admin':None})
# app = app.wsgifunc()
