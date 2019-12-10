import sys
from datetime import datetime
from random import randint


def guide_page(guide_word):
    print('****************{}****************'.format(guide_word))
    start = input('请输入起始值:')
    end = input('请输入终止值:')
    print('产生的随机数字区间为：{}'.format([start, end]))
    return set_final_num(start, end)


def all_num(n): ##判断字符串是否全部为数字
    if n.isdigit():
        return True
    else:
        return False


def num_legal(ls):##判断两个边界是否符合规定
    if ls[0] >= ls[1]:
        print('please restart program')
        sys.exit()
    else:
        return 1


def set_final_num(num1, num2): ##在给定的边界生成一个随机数
    ls = []
    ls.append(num1)
    ls.append(num2)
    print(ls)
    for i in ls:
        if not all_num(str(i)):
            print('请输入数字')
            sys.exit()
    if (num_legal(ls) == 1):
        return randint(int(num1), int(num2))
    else:
        print('please restart program')
        sys.exit()


def write_record(times, value): ##写入日志
    with open('record.txt','a+', encoding= 'utf-8') as f:
        f.write('{}:第{}次您猜测的数字为：{}\n'.format(datetime.now(), times, value),)


def main(rand1):
    temp = int(rand1)
    t = 0
    while True:
        i = int(input('请输入您猜的数字:'))
        if i < guide_page.start:
            print('请输入处于范围内的数字')
        elif i < guide_page.start:
            print('请输入处于范围内的数字')
        elif i < temp:
            print('*************')
            print('猜错了,比这个大')
            t += 1
            write_record(t, i)
        elif i > temp:
            print('*************')
            print('猜错了,比这个小')
            t += 1
            write_record(t, i)
        elif i == temp:
            print('*************')
            t += 1
            print('恭喜您只用了{}次就猜对了'.format(t))
            write_record(t, i)
            break



if __name__ == '__main__':
    main(guide_page('欢迎来到德莱联盟'))
