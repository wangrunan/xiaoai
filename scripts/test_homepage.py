import time

from base.base_action import BaseAction
from base.driver import get_driver
from page.page import Page


class TestHomePage:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()


    # 点击音乐资源
    def test_click_music_button(self):
        # 首页点击音乐资源
        self.page.homepage.click_music_button()
        # 断言
        assert self.page.homepage.get_text(self.page.homepage.more_recommend_button) == "更多推荐"
        assert self.page.homepage.get_text(self.page.homepage.more_list_button) == "更多榜单"

    # 点击音乐资源-更多推荐
    def test_click_more_recommend(self):
        # 首页点击音乐资源
        self.page.homepage.click_music_button()
        # 点击更多推荐
        self.page.homepage.click_more_recommend_button()
        # 断言
        assert self.page.homepage.get_text(self.page.homepage.recommend_tittle) == "推荐歌单"

    #     点击音乐资源-更多榜单
    def test_click_more_list(self):
        # 首页点击音乐资源
        self.page.homepage.click_music_button()
        # 点击更多榜单
        self.page.homepage.click_more_list_button()
        # 断言
        assert self.page.homepage.get_text(self.page.homepage.list_tittle) == "排行榜"

    # 点击音乐资源-更多分类
    def test_click_more_class(self):
        # 首页点击音乐资源
        self.page.homepage.click_music_button()
        # 点击更多榜单
        self.page.homepage.click_more_class_button()
        # 断言
        assert self.page.homepage.get_text(self.page.homepage.all_list_tittle) == "全部分类"

    # 点击小爱同学圈
    def test_xiaoai_schoolmate(self):
        #     首页点击小爱同学圈
        self.page.homepage.click_xiaoai_schoolmate()
        time.sleep(3)
        #断言
        assert self.page.homepage.get_text(self.page.homepage.xiaoai_schoolmate_tittle) == "小米社区"

    # 点击蓝牙耳机圈
    def test_bluetooth_headset(self):
        #     点击蓝牙耳机圈
        self.page.homepage.click_bluetooth_headset()
        time.sleep(3)
        #断言
        assert self.page.homepage.get_text(self.page.homepage.bluetooth_headset_tittle) == "小米社区"

    # 点击小爱课程表
    def test_class_schedule(self):
        #     点击小爱课程表
        self.page.homepage.click_class_schedule()
        time.sleep(3)
        #断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    # 点击全部技能页
    def test_all_skill(self):
        #     点击全部技能页
        self.page.homepage.click_all_skill()
        time.sleep(3)
        # 断言
        assert self.page.homepage.get_text(self.page.homepage.all_skill_tittle) == "全部技能页"


    #点击更多音乐
    def test_more_music(self):
        #点击更多音乐
        self.page.homepage.click_more_music()
        #断言
        assert self.page.homepage.get_text(self.page.homepage.more_recommend_button) == "更多推荐"

    # 8.23新增（熊浩）
    #点击音乐资源-推荐歌单-播放全部-关闭-返回首页
    def test_open_muisc_close(self):
        # 首页点击音乐资源
        self.page.homepage.click_music_button()
        #点击推荐歌单
        self.page.homepage.click_more_recommend_music()
        # 点击 播放全部
        self.page.homepage.click_play_all_music()
        #断言
        assert self.page.homepage.get_text(self.page.homepage.close_button) == '关闭'
        time.sleep(2)
        #点击关闭按钮
        self.page.homepage.click_close_button()
        time.sleep(2)
        #点击返回按钮
        self.page.homepage.click_return_button()
        # #断言
        assert self.driver.current_activity == ".presenter.main.MainTabActivity"

    # 音乐资源页显示四个模块标题正确
    def test_muisc_show(self):
        # 首页点击音乐资源
        self.page.homepage.click_music_button()
        #断言
        assert self.page.homepage.get_text(self.page.homepage.music_show1) == "小爱同学，放首歌"
        assert self.page.homepage.get_text(self.page.homepage.music_show2) == "小爱同学，我想听..."
        assert self.page.homepage.get_text(self.page.homepage.music_show3) == "小爱同学，播放热门歌曲"
        # self.driver.get_window_size()  # 获取手机分辨率
        # width = self.driver.get_window_size()["width"]
        # height = self.driver.get_window_size()["height"]
        # self.driver.swipe(100, height * 0.8, 100, height * 0.2, 5000)
        # assert self.page.homepage.get_text(self.page.homepage.music_show4) == "小爱同学，放首适合工作的歌"
        assert self.page.homepage.get_text_scroll(self.page.homepage.music_show4) == "小爱同学，放首适合工作的歌"

    #9.6 刘锐
        # 点击键盘输入为空
    def test_input_null(self):
         # 点击键盘
        self.page.homepage.click_keyboard()
         # 点击发送
        self.page.sessionpage.click_send_button()
         # 断言
        assert self.page.homepage.is_toast_exist("输入为空")

    # 点击小球-进入悬浮窗-点击收音球进入首页
    def click_globule_reception(self):
        time.sleep(3)
        # 点击小球
        self.page.homepage.click_globule()
         # 点击收音状态的小球
        self.page.homepage.click_globule_reception()
        # 断言
        assert self.driver.current_activity == '.presenter.main.MainTabActivity'

#09.02王茹楠源代码

    # 点击今日热点
    def test_today_hot_spots(self):

        #强制sleep3秒
        time.sleep(3)

        # 调用page.homepage页面的croll_page_one_time()方法 滑动屏幕
        self.page.homepage.scroll_page_one_time()

        #调用page.homepage页面的click_today_hot_spots()方法 点击今日热点
        self.page.homepage.click_today_hot_spots()
        time.sleep(2)
        # 调用page.homepage页面的get_text  断言页面是否跳转到今日热点
        # assert self.page.homepage.get_text(self.page.homepage.today_hot_spots_tittle)=='今日热点'
        assert len(self.page.homepage.get_text(self.page.homepage.today_hot_spots_tittle)) > 0

    # 小爱同学推荐-探索更多
    def test_explore_more(self):

        # 调用page.homepage页面的click_explore_more()方法点击小爱同学推荐-探索更多
        self.page.homepage.click_explore_more()

        # 调用page.homepage页面的get_text  断言页面是否跳转到小爱同学推荐
        assert self.page.homepage.get_text(self.page.homepage.explore_more_title) == '小爱同学推荐'