import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestMyPrize:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
        #8.29何巧，新增3条下我的奖品页面
# 点击我的奖品页面-点击实物奖品，跳转页面
    def test_myprize_01(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"我的奖品"按钮
        self.page.centerpage.click_my_prize()
        #点击实物奖品
        self.page.myprizepage.click_Prizeinkind_tab()
        #断言-1.页面标题是——实物奖品
        assert self.page.myprizepage.get_title_text()=="实物奖品"

# 点击我的奖品页面-点击红包奖品，跳转页面
    def test_myprize_02(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"我的奖品"按钮
        self.page.centerpage.click_my_prize()
        #点击实物奖品
        self.page.myprizepage.click_Redenvelopeprize_tab()
        #断言-1.页面标题是——红包奖品
        assert self.page.myprizepage.get_title_text()=="红包奖品"
# 点击我的奖品页面-点击卡券奖品，跳转页面
    def test_myprize_03(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        # 点击"我的奖品"按钮
        self.page.centerpage.click_my_prize()
        #点击实物奖品
        self.page.myprizepage.click_Cardvoucherprize_tab()
        #断言-1.页面标题是——卡券奖品
        assert self.page.myprizepage.get_title_text()=="卡券奖品"