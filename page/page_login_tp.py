from selenium.webdriver.common.by import By

from tpshop.base.base_action import BaseAction


class PageLoginTp(BaseAction):

    """
    登录页面配置信息
    """
    login_link = By.LINK_TEXT, '登录'
    login_user = By.CSS_SELECTOR, '#username'
    login_pwd = By.CSS_SELECTOR, '#password'
    login_verify_code = By.CSS_SELECTOR, 'input[placeholder="验证码"]'
    login_btn = By.CSS_SELECTOR, '#loginform > div > div.login_bnt > a'
    login_prompt_info = By.XPATH, '//*[@id="layui-layer1"]/div[2]/text()'
    login_confirm_btn = By.CSS_SELECTOR, '#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a'
    logout_btn = By.LINK_TEXT, '安全退出'
    login_nickname = By.CSS_SELECTOR, 'body > div.tpshop-tm-hander.home-index-top.p > div > div > div > div.fl.islogin.hide > a.red.userinfo'

    # 点击登录连接
    def page_click_login_link(self):
        self.base_click_mtd(PageLoginTp.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input_mtd(PageLoginTp.login_user, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input_mtd(PageLoginTp.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.base_input_mtd(PageLoginTp.login_verify_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click_mtd(PageLoginTp.login_btn)

    # 获取提示信息
    def page_get_prompt_info(self):
        return self.base_get_text(PageLoginTp.login_prompt_info)

    # 点击提示信息确认按钮
    def page_click_confirm_btn(self):
        self.base_click_mtd(PageLoginTp.login_confirm_btn)

    # 获取登录成功信息
    def page_login_success_info(self):
        return self.base_get_text(PageLoginTp.login_nickname)

    # 登录成功后，点击退出按钮
    def page_click_logout_btn(self):
        self.base_click_mtd(PageLoginTp.logout_btn)

    # 调用登录组合业务方法
    def page_login(self, username, pwd, code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(code)
        self.page_click_login_btn()