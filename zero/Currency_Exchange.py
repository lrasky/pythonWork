while True:
    service_menu = {1:'人民币转换美元',2:'美元转换人民币',3:'人民币转换欧元',0:'结束程序'} ##定义菜单字典函数
    print('******欢迎使用货币转换服务系统*********')
    for k,v in service_menu.items():
        print('{},{}'.format(k,v))
    You_Choice =[]
    You_Choice = int(input('请您选择需要的服务:'))
    if You_Choice == 1:
        print('当前人民币与美元的汇率为 1：7')
        money = float(input('请输入您要转换的人民币金额:'))
        print('您要转换的人民币金额为:{}元'.format(money))
        print('兑换成美元为：{:.2f}$'.format(money*7))
    elif You_Choice == 2:
        print('当前人民币与美元的汇率为 1：7')
        money = float(input('请输入您要转换的美元金额:'))
        print('您要转换的美元金额为:{}$'.format(money))
        print('兑换成人民币为：{:.2f}￥'.format(money/7))
    elif You_Choice == 3:
        print('当前人民币与欧元的汇率为 1：9')
        money = float(input('请输入您要转换的人民币金额:'))
        print('您要转换的人民币金额为:{}元'.format(money))
        print('兑换成欧元为：{:.2f}欧元'.format(money*9))
    elif You_Choice == 0:
        break
    else:
        print('您输入的信息有误，请重新输入')