#导包
import unittest
#定义测试套件
import time

from config import BASE_DIR
from script.test_cart import TestCart
from script.test_login import TestLogin
from script.test_order import TestOrder
from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverUtil

suite = unittest.TestSuite()
#添加测试用例
DriverUtil.set_auto_quit(False)
suite.addTest(unittest.makeSuite(TestLogin))

suite.addTest(unittest.makeSuite(TestCart))
suite.addTest(unittest.makeSuite(TestOrder))
#执行测试套件
# suite = unittest.TestLoader().discover('./script',pattern='t*.py')
report_path=BASE_DIR+'/report/report{}.html'.format(time.strftime("%Y%m%d-%H%M%S"))
with open(report_path,'wb')as f:
    HTMLTestRunner(f,title="tpshop自动化测试报告",description="Win10.Chrome").run(suite)

DriverUtil.set_auto_quit(True)
DriverUtil.quit_driver()
