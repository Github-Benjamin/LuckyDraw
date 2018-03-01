# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/23
#  */
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def save(data):
    s = json.dumps(data,indent=2,ensure_ascii=False)
    f = open('userlist.txt','w+')
    f.write(s)
    f.close()

def load():
    f = open('userlist.txt', 'r')
    s = f.read()
    return json.loads(s)

def alluserdata():
    return json.dumps(load(), indent=2, ensure_ascii=False)

def deluser(user):
    data = load()
    a = 0
    for i in data:
        if i.has_key(user):
            del data[int(a)]
            save(data)
            return 'del succes'
        a += 1
    return 'del faild'

def edituser(user,times):
    data = load()
    for i in data:
        if i.has_key(user):
            i[user] = times
            save(data)
            return 'edit succes'
    return 'edit faild'
