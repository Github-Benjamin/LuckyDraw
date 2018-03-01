# coding:utf-8
# /**
#  * Created by Benjamin on 2017/7/17.
#  */

import web
import json
import random

urls = (
    '/','Index',
    '/playbtn','Playbtn',
    '/lucky','Lucky',
)

renter = web.template.render('templates')

class Index(object):
    def GET(self):
        #return 'Hello World!'
        return renter.two()

class Playbtn(object):
    def GET(self):
        return '<script> alert("Test") </script>'

def jsondata(id,angle,text):
    data = {
        'id': id,
        'angles':angle,
        'name': text,
    }
    s = json.dumps(data, indent=2, ensure_ascii=False)
    return s

def luckrandom():
    id = random.randint(1,6)
    if id == 1:
        return jsondata(id,0, '恭喜您抽中理财金2000元！')
    if id == 2:
        return jsondata(id,60, '很遗憾未中奖，谢谢参与！')
    if id == 3:
        return jsondata(id,120, '恭喜您抽中理财金5200元！')
    if id == 4:
        return jsondata(id,180, '恭喜您抽中100元京东卡一张！')
    if id == 5:
        return jsondata(id,240, '很遗憾未中奖，谢谢参与！')
    if id == 6:
        return jsondata(id,300, '恭喜您抽中理财金1000元！')
    else:
        return jsondata('Null',0, '数据异常！')

class Lucky(object):
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return luckrandom()

if __name__ == '__main__':
    web.application(urls,globals()).run()
