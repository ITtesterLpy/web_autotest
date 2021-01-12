import time

from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 获取页面元素
    def base_find_element(self, feature, time=20, poll=0.3):
        return WebDriverWait(self.driver,
                             timeout=time,
                             poll_frequency=poll).until(lambda x:x.find_element(*feature))

    # 清空页面元素
    def base_clear_mtd(self, feature):
        self.base_find_element(feature).clear()

    # 输入页面元素
    def base_input_mtd(self, feature, value):
        # 清空初始值
        self.base_clear_mtd(feature)
        # 输入value
        self.base_find_element(feature).send_keys(value)

    # 点击页面元素
    def base_click_mtd(self, feature):
        self.base_find_element(feature).click()

    # 获取文本信息
    def base_get_text(self, feature):
        return self.base_find_element(feature).text

    # 获取截图图片
    def base_get_screenshot(self):
        return self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_d %H-%M-%S")))

    # 判断元素是否存在
    # def base_is_not_exist(self, feature):
    #     try:
    #         if self.base_find_element(feature):
    #             return True
    #         else:
    #             return False