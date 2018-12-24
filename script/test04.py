# 从appium库里面导入driver对象
import pytest
from appium import webdriver
# 导入time
import time


class TestA:

    def setup_class(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'  # 平台名称
        desired_caps['platformVersion'] = '5.1'  # 平台版本
        desired_caps['deviceName'] = '192.168.56.101:5555'  # 设备号
        # app信息
        desired_caps['appPackage'] = 'com.android.settings'  # 应用的包名
        desired_caps['appActivity'] = '.Settings'  # 代表启动的activity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 声明driver对象

    def teardown_class(self):
       time.sleep(5)
       self.driver.close_app()
       self.driver.quit()

    #业务 点击搜索按钮 ----> 定位到搜索的文本框 --->向文本框输入内容(函数数据参数化往里面传数据)
    @pytest.mark.parametrize("keys", [1, 2])
    def test_setting(self,keys):
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys(keys)

