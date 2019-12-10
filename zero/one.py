# lst = [23, 45, 22, 44, 25, 66, 78]
# # 生成所有奇数组成的列表
# lst1 = [lst[i] for i in range(len(lst)) if lst[i] %2 ==0]
# print(lst1)
# # 输出结果[28, 50, 27, 49, 30, 71, 83]
# lst2 = [lst[i]+5 for i in range(len(lst))]
# print(lst2)

# def goose():
#     # 向控制台输出唐诗《咏鹅》诗句
#     print('鹅,鹅,鹅，曲项向天歌。白毛浮绿水，红掌拨清波。')
#     print('*'*50)
#     # 向控制台输出50个*号分隔符
# goose()
# goose()
# goose()
#
# # 调用函数实现效果

# def oper(num, num1, num2):
#     # if条件判断num小于100的情况
#     if num < 100:
#         print(num1 * num2)
#     # 对num1和num2进行乘法运算，并输出结果
#
#     else:
#         print(num1 + num2)
#     # 对num1和num2进行加法运算，并输出结果
# oper(110,11,11)
#     # 调用函数，向函数内传入1314, 52, 0和5, 2, 0两组数据测试结果

# def login(username, password):
# # 使用if语句，判断用户名和密码为“imooc”和“123456”
#     if username == 'imooc':
#         if password == '123456':
#             return '登陆成功'
# # 返回登录成功
#     else:
#         return '请重新输入'
# # 使用else子句处理用户名和密码非“imooc”和“123456”的情况
#
# # 返回请重新登录
#
# # 调用函数，向函数内传入'imooc','123456'和'mooc','123456'两组数据测试结果
# print(login('imooc','123456'))
# 打印函数测试结果

# dict1 = {'name':'1',
#         'age':'1',
#         'height':'1',
#         'weight':'1',
#         'hr':'1',
#         'hbp':'1',
#         'glu':'1'}
# def health_check(name, age, height, weight, hr, hbp, glu):
#     print(dict1['name'])
#     print(name)
# health_check(**dict1)


# def info(*, desc,birth, name='imooc'):
#     # 使用format格式化字符串向控制台输出——imooc-程序员的梦工厂出生于2013年8月
#     print('{p1}-{}{}'.format(desc,birth,p1= name))
# # 调用函数，向函数内传入（"程序员的梦工厂"，"2013年8月"）
# info(desc= '程序员的梦工厂',birth= '2013年8月')

# def seq(num, num1, num2):
# #     # if判断num小于88
# #     if num < 88:
# #     # 返回num1与num2的积
# #         return num1 * num2
# #     else:
# #     # 返回num1与num2之和
# #         return num1 + num2
# #     # 定义变量tuple1的值为(5,2,1)
# # tuple1 = (5,2,1)
# #     # 调用函数，传入参数tuple1，并打印函数返回值
# # print(seq(*tuple1))

# def fun_dict(name, hiredate, tel, dept):
# # 使用format格式化字符串，使得向控制台输出结果——小葫芦隶属于技术部，电话:18795642135, 入职日期：2017-9-23,并向控制台输出结果
#     print('{}隶属{p1}电话：{p3}入职日期{p2}'.format(name,p2= hiredate,p3= tel,p1= dept))
#
# # 创建字典dict1为{'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
# dict1 = {'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
# # 使用字典dict1作为参数传入函数fun_dict
# fun_dict(**dict1)

# from datetime import datetime
# # 得到当前日期时间（两种方法）
# print(datetime.now())
# print(datetime.today())
# # 得到当前日期
# nowDate = datetime.now().date()
# print(nowDate)
# # 得到当前时间
# nowTime = datetime.now().time()
# print(nowTime)
# # 得到当前年份用year_变量接收
# year_ = datetime.now().year
# # 得到当前月份用month_变量接收
# month_ = datetime.now().month
# # 得到当前天用day_变量接收
# day_ = datetime.now().day
# # 使用-拼接年月日得到当前日期
# nowStrTime = '{}-{}-{}'.format(year_,month_,day_)
# print(nowStrTime)

# import datetime,time
# # 自定义日期时间为2019-10-10 8:10
# data_time = datetime.datetime(2019, 10, 10, 8, 10)
# # 打印自定义的日期时间对象
# print(data_time)
# # 使用time模块的sleep函数停顿2秒
# time.sleep(2)
# # 自定义日期2019-11-11
# date_ = datetime.date(2019, 11, 11)
# # 打印自定义的日期对象
# print(date_)
# # 自定义时间11:11
# time_ = datetime.time(11,11)
# # 打印自定义的时间对象
# print(time_)


# from datetime import datetime
# # 定义一个str_字符串为2019-09-10 8:10:56
# str_ = '2019-09-10 8:10:5'
# # 将str_转换为日期函数2019-09-10 8:10:56
# str_date = datetime.strptime(str_, '%Y-%m-%d %H:%M:%S')
# print(str_date)
# # 定义now_变量接收当前的日期时间
# now_ = datetime.now()
# print(now_)
# # 将当前日期时间格式化为——四位的年份/月/日 时:分:秒
# date_str = now_.strftime('%Y/%m/%d %H:%M:%S')
# print(date_str)


from datetime import datetime, timedelta
# 定义now_变量接收当前日期时间
now_= datetime.now()
# 计算距当前日期时间3天36小时12分钟之前的日期时间
now_before= now_ - timedelta(days= 5,hours= 36, minutes= 12)
# 计算10天之后的日期时间
now_after= now_ + timedelta(days= 10)
print(now_before)
print(now_after)
