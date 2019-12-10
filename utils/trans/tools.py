from datetime import datetime
import random


def gen_trans_id(date = None):
    '''
    根据所传入的时间得到一个唯一的交易流水id
    :param date:传入一个日期
    :return:返回一个流水id
    '''

    # 如果没有传入日期则使用当前日期
    if date == None:
        date = datetime.now()
    return date.strftime('%Y%m%d%H%M%S%f') + str(random.randint(100000,999999))