# 从appium库里面导入driver对象
import pytest
from appium import webdriver
# 导入time
import time
class TestA:
    #最先执行
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
    # 最后执行
    def teardown_class(self):
        time.sleep(5)
        # 关闭app driver对象不会关闭
        self.driver.close_app()
        # 关闭驱动对象
        self.driver.quit()

    #打开设置应用

    def test_setting(self,a):
       pass




