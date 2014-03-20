__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from SocketServer import TCPServer,ThreadingMixIn,StreamRequestHandler
import time,os,commands
import cPickle,md5
#HOST = '207.198.106.114'
HOST = '118.130.49.15'
PORT = 1003
def transfertime(ret):
    '''时间转换'''
    a = filter(str.isdigit,ret)
    a = list(a)
    c = ''
    for i in range(len(a)):
        c += a[i]
        if i in (3,5):
            c += '-'
        if i==7:
            c += ' '
        if i in (9,11):
            c += ':'
    a = time.mktime(time.strptime(c,'%Y-%m-%d %H:%M:%S'))
    return a
def stopjava():
    '''关服'''
    os.popen('pkill java')
def startjava():
    '''开服'''
#    os.popen('cd /data/game/version/qmrserver1/qmrserver && /bin/sh start.sh')
    os.popen("cd /data/game/qmrserver_lianfu_10000/qmrserver && /bin/sh start.sh")
    os.popen("cd /data/game/qmrserver10/qmrserver && /bin/sh start.sh >/dev/null 2>&1")
    os.popen("cd /data/game/qmrserver20/qmrserver && /bin/sh start.sh >/dev/null 2>&1")
    os.popen("cd /data/game/qmrserver30/qmrserver && /bin/sh start.sh >/dev/null 2>&1")
    os.popen("cd /data/game/qmrserver40/qmrserver && /bin/sh start.sh >/dev/null 2>&1")
    os.popen("cd /data/game/newversion && /bin/sh start.sh >/dev/null 2>&1")
    os.popen("cd /data/game/huodong && /bin/sh start.sh >/dev/null 2>&1")


def updatejava():
    '''更新java'''
    os.popen('rsync -vzrtopg --progress --stats  /var/ftp/qmrserver/* /data/game/version/qmrserver1/qmrserver > /dev/null 2>&1')
logfile = open('name1.txt','a')
def log(msg):
    '''日志记录'''
    datenow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    logstr = '%s : %s \n' %(datenow, msg)
    #print(logstr)
    logfile.write(logstr)
def filter(file1):
    try:
        f = file(file1,'rb')
        return cPickle.load(f)
    except IOError:
        return {}
    except EOFError:
        return {}


class Server(ThreadingMixIn,TCPServer):
    '''多线程处理'''
    pass
class Handler(StreamRequestHandler):
    '''处理请求'''
    def handle(self):
        while True:
            try:
                ip = self.client_address[0]
#                print ip
                ret = self.request.recv(2048).strip()
                if ip == '221.237.152.208' or ip == '221.237.152.108' or ip == '127.0.0.1':
                    if ret == 'reboot':
                        self.request.send('请求收到，正在处理中.....')
                        stopjava()
                        time.sleep(25)
                        startjava()
                    elif ret == 'banben':
                        self.request.send('请求收到，正在处理中')
                        updatejava()
                    elif ret == 'time':
                        shijian = os.popen('date +"%Y-%m-%d %H:%M:%S"').read()
                        self.request.send(shijian)
                    elif ret == 'cata':
                        a = []
                        for dirName,subdirList,fileList in os.walk('/var/ftp/qmrserver'):
                            a.append(dirName)
                            c = '&'.join(a)
                            self.request.send('&'.join(a))
                    elif not ret:
#                        print '没有数据'
                        break
                    else:
                        self.request.send('请求收到，正在处理中....')
                        try:
                            global time1
                            time1 = transfertime(ret)
                            timett = commands.getoutput('date "+%Y-%m-%d %H:%M:%S"')
                            time2 = transfertime(timett)
                        except Exception,e:
                            print e
                            log('时间格式错误')
                            self.request.send('时间格式错误')
                        if int(time1) > int(time2):
                            os.popen('date -s "%s"' % ret).read()
                            self.request.send('时间修改成功')
                        else:
                            self.request.send('已经收到请求，正在处理中...')
                            stopjava()
                            time.sleep(20)
                            os.popen('date -s "%s"' % ret).read()
                            startjava()
                            time.sleep(10)
                else:
                    log('the source is wrong')
                    pass
            except KeyboardInterrupt:
                log('键盘错误')
server = Server((HOST,PORT),Handler)
server.serve_forever()









