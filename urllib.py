__author__ = 'Administrator'
#coding: gbk
import urllib2
from urllib import *
import sched, time

s = sched.scheduler(time.time, time.sleep)

def main():
    req = urllib2.Request('http://bbs.kidfanschannel.net/discuz/plugin.php?identifier=get_money&module=money&action=money_list&listspec=0&page=1')
    res = urllib2.urlopen(req)
    html = res.read()
    res.close()
    content = unicode(html, 'gbk')      #��ת��unicode���޷���find����unicode
    i = content.find(u'ÿ�պ��')
    i += content[i:].find(u'����')       #�����С������Ǹ����־��Ǻ����Ŀ
    print time.strftime('%Y-%m-%d %X', time.localtime(time.time())),
    if content[i+2] != '0' :
        print '���к��'
        import webbrowser
        webbrowser.open('http://bbs.kidfanschannel.net/discuz/plugin.php?identifier=get_money&module=money&action=money_get&hid=2')
        import sys
        sys.exit()
    else:
        print '��û�к��'
    s.enter(60, 1, main, ())            #ÿ60���ѯһ��
    s.run()

if __name__ == "__main__":
    main()