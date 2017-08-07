# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/23
#  */
import json
import sys
from decimal import *
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

def saveconf(data):
    f = open('luckyconfig.txt','w+')
    f.write(data)
    f.close()

def loadconf():
    f = open('luckyconfig.txt', 'r')
    s = f.read()
    list = []
    for i in s.split(','):
        list.append(i)
    lista = []
    for i in range(6):
        lista.append(float(list[i]))
    return lista


# 核对本地配置文件概率数是否正确的函数检查，目前未调用
def checknumconf():
    list = load()
    try:
        sumlist = float(list[0])+float(list[1])+float(list[2])+float(list[3])+float(list[4])+float(list[5])
        num = Decimal(sumlist).quantize(Decimal('0.00'))
        if num == 1:
            return 1
    except:
        return 0