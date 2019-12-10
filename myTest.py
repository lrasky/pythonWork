# import threading
# def action(max):
#     for i in range(max):
#         print(threading.current_thread().getName()+ ' ' + str(i))
# threading.Thread(target= action, args= (100,), name= ('新线程')).start()
# for i in range(100):
#     if i == 20:
#         jt = threading.Thread(target= action, args= (100,), name= ('被join的线程'))
#         jt.start()
#         jt.join()//在这个地方 主线程join了jt线程 所以主线程暂停 jt线程开始执行。当jt线程执行结束后主线程开始执行.
#     print(threading.current_thread().getName() + ' ' + str(i))

# import time
# for i in range(10):
#     print('当前时间'+ time.ctime())
#     time.sleep(1)


# class Account:
#     def __init__(self,money,account_number):
#         self.account_number = account_number
#         self.money = money
#
# import threading,time
# def draw(account_number,draw_money):
#     if account_number.money > draw_money:
#         print('取钱成功')
#         time.sleep(0.01)
#         account_number.money -= draw_money
#         print('当前账户余额为:'+ str(account_number.money))
#     else:
#         print('取钱失败')
#
# acco = Account(1000,'001')
# threading.Thread(target= draw, args=(acco,600,),name= '第一个线程').start()
# threading.Thread(target= draw, args=(acco,600,),name= '第二个线程').start()

# import threading,time
# class Account:
#     def __init__(self,money,account_number):
#         self.account_number = account_number
#         self._money = money
#         self.lock = threading.RLock()
#     def getMoney(self):
#         return self._money
#
#
#     def draw(self,draw_money):
#         self.lock.acquire()
#         try:
#             if self._money > draw_money:
#                 print('取钱成功')
#                 time.sleep(1)
#                 self._money -= draw_money
#                 print('当前账户余额为:'+ str(self.getMoney()))
#             else:
#                 print('取钱失败')
#         finally:
#             self.lock.release()
#
# acco = Account(1000,'001')
# def drawMoney(acco,money):
#     return Account.draw(acco,money)
# threading.Thread(target= drawMoney, args=(acco,600,),name= '第一个线程').start()
# threading.Thread(target= drawMoney, args=(acco,600,),name= '第二个线程').start()

# import threading,time
# class Account:
#     def __init__(self,money,account_number):
#         self.account_number = account_number
#         self._money = money
#         self.lock = threading.RLock()
#     def getMoney(self):
#         return self._money
#
#
#     def draw(self,draw_money):
#         self.lock.acquire()
#         try:
#             if self._money > draw_money:
#                 print('取钱成功')
#                 time.sleep(1)
#                 self._money -= draw_money
#                 print('当前账户余额为:'+ str(self.getMoney()))
#             else:
#                 print('取钱失败')
#         finally:
#             self.lock.release()
#
# acco = Account(1000,'001')
# threading.Thread(target= acco.draw, args=(600,),name= '第一个线程').start()
# threading.Thread(target= acco.draw, args=(600,),name= '第二个线程').start()

# import threading, time
# class A:
#     def __init__(self):
#         self.lock = threading.RLock()
#     def foo(self,b):
#         self.lock.acquire()
#         try:
#             print('当前线程名:'+ threading.current_thread().getName()+ ' 进入A实例的foo方法')
#             time.sleep(0.1)
#             print('当前线程名:'+ threading.current_thread().getName()+ ' 企图进入B实力的last方法')
#             b.last()
#         finally:
#             self.lock.release()
#     def last(self):
#         try:
#             self.lock.acquire()
#             print('进入A类的last方法内部')
#         finally:
#             self.lock.release()
# class B:
#     def __init__(self):
#         self.lock = threading.RLock()
#     def bar(self,a):
#         try:
#             self.lock.acquire()
#             print('当前线程名:'+ threading.current_thread().getName()+ ' 进入B实例的bar方法')
#             time.sleep(0.1)
#             print('当前线程名:'+ threading.current_thread().getName()+ ' 企图进入A实例的last方法')
#             a.last()
#         finally:
#             self.lock.release()
#     def last(self):
#         try:
#             self.lock.acquire()
#             print('进入B类的last方法内部')
#         finally:
#             self.lock.release()
# a = A()
# b = B()
# def init():
#     threading.current_thread().name = '主线程'
#     a.foo(b)
#     print('进入主线程后')
# def action():
#     threading.current_thread().name = '副线程'
#     b.bar(a)
#     print('进入副线程后')
# threading.Thread(target= action).start()
# init()

# import threading
# class Account:
#     def __init__(self,account_id,balance):
#         self.accoint_id = account_id
#         self._balance = balance
#         self.condition = threading.Condition()
#         self._flag = False
#     def getBalance(self):
#         return self._balance
#     def draw(self,money):
#         try:
#             self.condition.acquire()
#             if not self._flag:
#                 self.condition.wait()
#             else:
#                 print(threading.current_thread().getName() + ' 取钱成功')
#                 self._balance -= money
#                 print('账户余额：' + str(self._balance))
#                 self._flag = False
#                 self.condition.notify_all()
#         finally:
#             self.condition.release()
#     def deposit(self,money):
#         try:
#             self.condition.acquire()
#             if self._flag:
#                 self.condition.wait()
#             else:
#                 print(threading.current_thread().getName()+' 存钱成功')
#                 self._balance += money
#                 print('账户余额： '+ str(self._balance))
#                 self._flag = True
#                 self.condition.notify_all()
#         finally:
#             self.condition.release()
#
# def draw_money(account,money,max):
#     for i in range(max):
#         account.draw(money)
# def deposit_money(account,money,max):
#     for i in range(max):
#         account.deposit(money)
# acco = Account('001',0)
# threading.Thread(target= draw_money, args= (acco,1000,100),name= '取钱',).start()
# threading.Thread(target= deposit_money, args= (acco,1000,100,), name= '存钱甲').start()
# threading.Thread(target= deposit_money, args= (acco,1000,100,), name= '存钱乙').start()
# threading.Thread(target= deposit_money, args= (acco,1000,100,), name= '存钱丙').start()

# import queue
# bg = queue.Queue(2)
# # bg.put('python')
# # bg.put('python')
# print('1111')
# # bg.put('python')
# bg.get()
# print('22222222')

# import threading,time,queue
# def produce(bg):
#     for i in range(9999):
#         str_trump = ('python', 'Kotlin', 'Swift')
#         print(threading.current_thread().getName()+' 生产者准备生产组元素')
#         time.sleep(0.1)
#         bg.put(str_trump[i%3])
#         print(threading.current_thread().getName() + ' 组元素生产完成')
# def consume(bg):
#     while True:
#         print(threading.current_thread().getName()+ ' 消费者准备消费组元素')
#         time.sleep(0.1)
#         t = bg.get()
#         print(threading.current_thread().getName()+ '组元素消费完成 '+ t)
# bg = queue.Queue(1)
# threading.Thread(target= produce,args= (bg,), name= '生产者甲').start()
# threading.Thread(target= produce,args= (bg,), name= '生产者乙').start()
# threading.Thread(target= produce,args= (bg,), name= '生产者丙').start()
# threading.Thread(target= consume, args= (bg,), name= '消费者').start()

# import threading,time
# event = threading.Event()
# def cal(name):
#     print('%s 启动' % threading.current_thread().getName())
#     print(' %s 准备开始计算状态' %name)
#     event.wait()
#     print('%s 收到通知了' %threading.current_thread().getName())
#     print('%s 正式开始计算' %name)
# threading.Thread(target= cal, args=('甲',)).start()
# threading.Thread(target= cal, args=('乙',)).start()
# time.sleep(2)
# print('------')
# print('主程序发出事件')
# event.set()

# import threading
# class Account:
#     def __init__(self,id,balance):
#         self.id = id
#         self._balance = balance
#         self.lock = threading.RLock()
#         self.event = threading.Event()
#     def getBalance(self):
#         return self._balance
#     def draw(self,draw_money):
#         self.lock.acquire()
#         print(self.event.is_set())
#         if self.event.is_set():
#             print(threading.current_thread().getName()+ '取钱' + str(draw_money))
#             self._balance -= draw_money
#             print('账户余额为：' + str(self._balance))
#             self.event.clear()
#             self.lock.release()
#             self.event.wait()
#         else:
#             self.lock.release()
#             self.event.wait()
#     def deposit(self,des_money):
#         self.lock.acquire()
#         print(self.event.is_set())
#         if not self.event.is_set():
#             print(threading.current_thread().getName()+ '存钱:' + str(des_money))
#             self._balance += des_money
#             print('账户余额为：' + str(self._balance))
#             self.event.set()
#             self.lock.release()
#             self.event.wait()
#         else:
#             self.lock.release()
#             self.event.wait()
# acco = Account('001',100)
# def draw(money):
#     acco.draw(money)
# def deposit(money):
#     acco.deposit(money)
# # for i in range(10):
# threading.Thread(target= deposit,args= (100,)).start()
# threading.Thread(target= draw,args= (100,)).start()

# from concurrent.futures import ThreadPoolExecutor
# import threading,time
# def action(max):
#     my_sum = 0
#     for i in range(max):
#         print(threading.current_thread().name + ' ' + str(i))
#         my_sum += i
#     return my_sum
# pool = ThreadPoolExecutor(max_workers= 2)
# future1 = pool.submit(action,50)
# future2 = pool.submit(action,100)
# print(future1.done())
# time.sleep(3)
# print(future2.done())
# print(future1.result())
# print(future2.result())
# pool.shutdown()

# from concurrent.futures import ThreadPoolExecutor
# import threading,time
# def action(max):
#     my_sum = 0
#     for i in range(max):
#         print(threading.current_thread().name + ' '+ str(i))
#         my_sum += i
#     return my_sum
# with ThreadPoolExecutor(max_workers = 4) as pool:
#     result = pool.map(action,(50,100,150))
#     print('----------------------------------------------')
#     for i in result:
#         print(i)

# a = [x for x in range(10)]
# print('a:'+'b',a)
# b = (x for x in range(8))
# print(b)
id_limit = []
for i in range(1000, 1007):
    id_limit.append(i)
print(id_limit)
for i in range(7):
    print(i)