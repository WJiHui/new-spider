#!/usr/bin/env python
# encoding:utf-8
import os
import datetime
import logging


class MyLog(object):
    """
    每天创建一个以当前日期为名的文件夹
    """

    def __init__(self, method=1, logname=None):
        self.logname = logname
        self.logger = None
        self.today = datetime.datetime.now().strftime('%Y-%m-%d')
        self.log_path = os.path.join(os.path.dirname(__file__), 'logs')
        self.mkdir_path(self.log_path)
        if method == 1:
            self.init_log1()
        elif method == 2:
            self.init_log2()

    def mkdir_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def init_log1(self):
        """
        创建日志 logs/2018-1-1.log 
        这种方式记录的日志信息只能在一个文件中
        """
        logging.basicConfig(
            filemode='a+',
            level=logging.INFO,
            filename=os.path.join(self.log_path, self.today+'.log'),
            datefmt='%m-%d %H:%M:%S',
            format="%(asctime)s %(levelname)s %(filename)s %(lineno)d: %(message)s"
        )
        self.logger=logging

    def init_log2(self):
        """
        创建多个实例就可以创建多个日志
        logs/2018-1-1/test1.log 
        logs/2018-1-1/test2.log 
        """
        today_path = os.path.join(self.log_path, self.today)
        self.mkdir_path(today_path)
        filename = os.path.join(today_path, self.logname + '.log')
        formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)s %(filename)s %(lineno)d: %(message)s',
            datefmt='%m-%d %H:%M:%S')
        fh = logging.FileHandler(filename, mode='a+')
        # fh.setLevel(logging.ERROR)  #
        # 如果设置了文件处理器水平的，优先级比日志水平高
        fh.setFormatter(formatter)

        self.logger = logging.getLogger(self.logname)
        # 返回一个logger对象，如果没有指定名字将返回root logger, 并且先加入的日志文件会记录后面所有信息
        self.logger.addHandler(fh)
        self.logger.setLevel(logging.INFO)

    def info(self, info, print_=False):
        if print_:
            print(self.logname + ': info :' + info)
        self.logger.info(info)

    def error(self, info, print_=False):
        if print_:
            print(self.logname + ': error' + info)
        self.logger.error(info)


def test1():
    log = MyLog()
    log.info('info')
    log.error('error')


def test2():
    log = MyLog(2, 'test1')
    log.info('info1')
    log.error('error1')
    log = MyLog(2, 'test2')
    log.info('info2')
    log.error('error2')


if __name__ == "__main__":
    # test1()
    test2()
