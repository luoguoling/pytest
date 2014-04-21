__author__ = 'luoguoling'
import os
import logging
def log1():
    logging.basicConfig(filename=os.path.join(os.getcwd(),'log21.txt'),level=logging.WARN,filemode='a',format='%(name)s-%(asctime)s - %(levelname)s:%(message)s ')
    log = logging.getLogger('root')
    log2 = logging.getLogger('root.bb')
    return log,log2
log1()[0].error('error')
log1()[1].critical('cuowu')
