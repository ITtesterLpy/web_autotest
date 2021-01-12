from selenium import webdriver


class BaseDriver:

    # 初始化driver
    driver = None

    # 获取浏览器驱动对象
    @classmethod
    def get_driver(cls):
        # 判断driver是否为空
        if cls.driver is None:
            # 实例化driver
            cls.driver = webdriver.Chrome()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get("http://127.0.0.1/")
            # 全局等待三秒
            cls.driver.implicitly_wait(3)
        return cls.driver

    # 关闭浏览器驱动对象
    @classmethod
    def quit_driver(cls):
        # 判断driver是否不为空
        if cls.driver:
            # 退出driver
            cls.driver.quit()
            # 置空
            cls.driver = None