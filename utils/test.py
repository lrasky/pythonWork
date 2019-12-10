from datetime import datetime

from utils import myTest2
from utils.trans.tools import gen_trans_id


def test_trans_tool():
    id1 = gen_trans_id()
    id2 = gen_trans_id(datetime(2015, 10, 30, 23, 11, 11))
    print(id1)
    print(id2)


if __name__ == '__main__':
    test_trans_tool()
    myTest2.tools.hello()