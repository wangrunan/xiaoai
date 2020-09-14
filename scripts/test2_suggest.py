import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestSuggest:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    #     首页点击小爱建议按钮
    def test_click_xiaoai_suggest(self):
        # 首页点击小爱建议按钮
        self.page.homepage.click_suggest_button()
        # 断言
        assert self.page.homepage.get_text(self.page.homepage.suggest_card_ttitle) == "小爱建议"

    # 点击小爱建议弹框设置按钮
    def test_suggest_card_setting(self):
        # 首页点击小爱建议按钮
        self.page.homepage.click_suggest_button()
        # 爱建议弹框点击设置按钮
        self.page.homepage.click_suggest_card_setting_button()
        # 断言
        assert self.page.suggestpage.get_text(self.page.suggestpage.suggest_tittle) == "小爱建议设置"


    # 小爱建议页点击课程建议tab
    def test_click_class_suggest_tab(self):
        # 首页点击小爱建议按钮
        self.page.homepage.click_suggest_button()
        # 爱建议弹框点击设置按钮
        self.page.homepage.click_suggest_card_setting_button()
        # 小爱建议页面点击课程建议tab
        self.page.suggestpage.click_class_suggest_tab()
        # 断言
        assert self.page.suggestpage.get_text(self.page.suggestpage.class_page_tittle) == "课程"

    # 小爱建议页点击天气变化tab
    def test_click_weather_suggest_tab(self):
        # 首页点击小爱建议按钮
        self.page.homepage.click_suggest_button()
        # 爱建议弹框点击设置按钮
        self.page.homepage.click_suggest_card_setting_button()
        # 小爱建议页面点击天气变化tab
        self.page.suggestpage.click_weather_suggest_tab()
        # 断言
        assert self.page.suggestpage.get_text(self.page.suggestpage.weather_suggest_page_tittle) == "天气变化建议"

    # 小爱建议页点击智能环境建议tab
    def test_click_intelligent_suggest_tab(self):
        # 首页点击小爱建议按钮
        self.page.homepage.click_suggest_button()
        # 爱建议弹框点击设置按钮
        self.page.homepage.click_suggest_card_setting_button()
        # 小爱建议页面点击智能环境建议tab
        self.page.suggestpage.click_intelligent_suggest_tab()
        # 断言
        assert self.page.suggestpage.get_text(self.page.suggestpage.intelligent_suggest_page_tittle) == "智能环境建议"

