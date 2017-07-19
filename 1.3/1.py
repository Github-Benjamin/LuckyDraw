import time

userlist = []

def adduser(user,playnum=3):
    times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    dict = {
        user:playnum,
        'time':times,
    }
    userlist.append(dict)

def reviseuser(user,playnum):
    for i in userlist:
        if i.has_key(user):
            times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            i[user] = playnum
            i['time'] = times

def lookupuser(user):
    for i in userlist:
        if i.has_key(user):
            return i[user]

user = 'Benjamin'
adduser(user,3)
print userlist

reviseuser(user,33)
reviseuser(user,11)

time.sleep(3)
adduser('boy')

print lookupuser(user)
print userlist