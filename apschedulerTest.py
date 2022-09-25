from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import logging
import os

'''
Apscheduler和logging使用参考
https://blog.csdn.net/time_money/article/details/119825381
'''


def JobFunc():
    strCurrentTime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    print('%s-Job started' % strCurrentTime)
    if datetime.datetime.now().second % 2 == 0:
        ExceptionFunc()
    # os.system('open /Applications/Google\ Chrome.app')


def ExceptionFunc():
    raise Exception("这里出错了")


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(JobFunc, 'interval', seconds=1)
    # dtCurrentTime = datetime.datetime.now()
    # dtJobTime = dtCurrentTime + datetime.timedelta(seconds=5)
    # scheduler.add_job(JobFunc, 'date', run_date=dtJobTime, timezone='Asia/Shanghai')
    scheduler.start()


if __name__ == '__main__':
    logging.getLogger('job')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='mylog.txt',
                        filemode='a')
    main()
