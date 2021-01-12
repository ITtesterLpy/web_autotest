import unittest

from parameterized import parameterized

from tpshop.base.base_driver import BaseDriver
from tpshop.page.page_login_tp import PageLoginTp
from tpshop.tools.get_txt import get_txt


# 获取测试数据
def get_data():

    # 新建空列表
    arrs = []

    #读取测试数据
    for data in get_txt('login_data.txt'):
        arrs.append(tuple(data.strip().split(',')))
    return arrs[1::]


class TestLoginTp(unittest.TestCase):

    # 初始化login
    login = None

    # 开始测试
    @classmethod
    def setUpClass(cls):
        # 判断login是否为空
        if cls.login is None:
            # 获取浏览器驱动对象
            cls.driver = BaseDriver.get_driver()
            # 实例化页面对象
            cls.login = PageLoginTp(cls.driver)
            # 点击登录按钮
            cls.login.page_click_login_link()

    # 结束测试
    @classmethod
    def tearDownClass(cls):
        # 判断login不为空
        if cls.login:
            # 退出页面
            BaseDriver.quit_driver()
            # 置空login
            cls.login = None

    # 登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, success, expect):
        # 调用登录组合业务
        self.login.page_login(username, pwd, code)

        if success == 'True':
            try:
                # 获取登录成功信息
                success_msg = self.login.page_login_success_info()
                # 断言登录成功信息是否符合预期
                self.assertEqual(expect, success_msg)
                # 点击安全退出按钮
                self.login.page_click_logout_btn()
                # 点击登录连接
                self.login.page_click_login_link()
            except Exception as e:
                # 抛出异常
                raise e
        else:
            try:
                # 获取登录错误提示信息
                error_msg = self.login.page_get_prompt_info()
                # 断言异常信息是否符合预期
                self.assertIn(expect, error_msg)
            except Exception as e:
                # 抛出异常
                raise e
            finally:
                # 获取错误截图
                self.login.base_get_screenshot()