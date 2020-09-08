from appium import webdriver



def get_driver(no_reset = True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'E6EDU20521033136'
    # toast
    desired_caps['automationName'] = 'Uiautomator2'
    #是否重置应用 True:不重置 False:重置
    desired_caps['noReset'] = no_reset
    desired_caps['appPackage'] = 'com.xiaomi.xiaoailite'
    desired_caps['appActivity'] = '.presenter.main.MainTabActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


