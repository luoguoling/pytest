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
    content = unicode(html, 'gbk')      #不转成unicode就无法用find查找unicode
    i = content.find(u'每日红包')
    i += content[i:].find(u'还有')       #“还有”后面那个数字就是红包数目
    print time.strftime('%Y-%m-%d %X', time.localtime(time.time())),
    if content[i+2] != '0' :
        print '：有红包'
        import webbrowser
        webbrowser.open('http://bbs.kidfanschannel.net/discuz/plugin.php?identifier=get_money&module=money&action=money_get&hid=2')
        import sys
        sys.exit()
    else:
        print '：没有红包'
    s.enter(60, 1, main, ())            #每60秒查询一次
    s.run()

if __name__ == "__main__":
    main()