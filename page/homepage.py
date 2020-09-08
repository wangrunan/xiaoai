import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

#首面
class HomePage(BaseAction):

    # 键盘
    keyboard = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/iv_query_keyboard']"

    # 个人中心按钮
    center_button = By.XPATH,"//*[@resource-id='com.xiaomi.xiaoailite:id/iv_login']"

    # 音乐资源按钮
    music_button = By.XPATH,"//*[@text='音乐资源']"

    # 更多推荐按钮
    more_recommend_button = By.XPATH,"//*[@text='更多推荐']"

    #音乐资源页更多推荐下面的推荐歌单
    more_recommend_music = By.XPATH,'//*[@resource-id="root"]/android.view.View[1]/android.view.View[3]/android.view.View[3]'

    # 推荐歌单页标题
    recommend_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 更多榜单
    more_list_button = By.XPATH,"//*[@text='更多榜单']"

    # 排行榜页面标题
    list_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 更多分类
    more_class_button = By.XPATH,"//*[@text='更多分类']"

    # 全部分类页面标题
    all_list_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"


    def click_keyboard(self):
        self.click(self.keyboard)

    def click_center_button(self):
        self.click(self.center_button)

    def click_music_button(self):
        self.click(self.music_button)

    #点击更多推荐
    def click_more_recommend_button(self):
        self.click(self.more_recommend_button)
    #点击推荐歌单
    def click_more_recommend_music(self):
        self.click(self.more_recommend_music)
    #     点击更多榜单
    def click_more_list_button(self):
        self.click(self.more_list_button)
        # self.find_element_with_scroll(self.more_list_button).click()
    #点击更多分类
    def click_more_class_button(self):
        self.find_element_with_scroll(self.more_class_button).click()


    #小爱同学圈按钮
    xiaoai_schoolmate = By.XPATH,"//*[@text='小爱同学圈']"
    # 小爱同学圈页面标题
    xiaoai_schoolmate_tittle = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"

    #蓝牙耳机圈
    bluetooth_headset = By.XPATH, "//*[@text='蓝牙耳机圈']"
    # 蓝牙耳机页面标题
    bluetooth_headset_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 小爱课程表
    class_schedule = By.XPATH, "//*[@text='小爱课程表']"

    # 全部技能
    all_skill = By.XPATH, "//*[@text='全部技能']"
    # 全部技能页标题
    all_skill_tittle = By.ID,"com.xiaomi.xiaoailite:id/toolbar_title"

    # 点击小爱同学圈
    def click_xiaoai_schoolmate(self):
        self.click(self.xiaoai_schoolmate)
    # 点击蓝牙耳机圈
    def click_bluetooth_headset(self):
        self.click(self.bluetooth_headset)
    # 点击小爱课程表
    def click_class_schedule(self):
        self.click(self.class_schedule)
    # 全部技能
    def click_all_skill(self):
        self.click(self.all_skill)

    #小爱建议按钮
    suggest_button = By.ID,"com.xiaomi.xiaoailite:id/iv_ai_suggestion"

    def click_suggest_button(self):
        self.click(self.suggest_button)

    #小爱建议弹窗卡片标题
    suggest_card_ttitle = By.ID,"com.xiaomi.xiaoailite:id/tv_title"

    #小爱建议弹窗卡片设置按钮
    suggest_card_setting_button = By.ID,"com.xiaomi.xiaoailite:id/iv_setting"

    def click_suggest_card_setting_button(self):
        self.click(self.suggest_card_setting_button)

    #小爱建议 -  更多音乐
    more_music = By.XPATH, "//*[@text='更多音乐']"

    def click_more_music(self):
        self.click(self.more_music)
    #播放全部按钮
    play_all_music = By.ID,'com.xiaomi.xiaoailite:id/iv_play_icon'
    def click_play_all_music(self):
        self.click(self.play_all_music)

    #关闭按钮
    close_button = By.XPATH,'//*[@resource-id="com.xiaomi.xiaoailite:id/btn_close"]'
    #点击关闭按钮
    def click_close_button(self):
        self.click(self.close_button)
    #返回按钮
    return_button = By.XPATH,'//android.widget.ImageButton'
    #点击返回按钮
    def click_return_button(self):
        self.click(self.return_button)

    #音乐资源页模块1
    music_show1 = By.XPATH,'//*[@text="小爱同学，放首歌"]'
    # 音乐资源页模块2
    music_show2 = By.XPATH, '//*[@text="小爱同学，我想听..."]'
    # 音乐资源页模块3
    music_show3 = By.XPATH, '//*[@text="小爱同学，播放热门歌曲"]'
    # 音乐资源页模块4
    music_show4 = By.XPATH, '//*[@text="小爱同学，放首适合工作的歌"]'

#9.6 刘锐 新增
   #首页小球
    globule =By.ID,'com.xiaomi.xiaoailite:id/idle_ball_background'

    #收音状态的小球
    globule_reception = By.ID,'com.xiaomi.xiaoailite:id/recording_state_recording'

    #点击小球
    def click_globule(self):
        self.click(self.globule)
        # self.driver.tap([(462,1612), (618,1768)], 500)

    # 点击收音状态的小球
    def click_globule_reception(self):
        self.click(self.globule_reception)

#09.02王茹楠新增

    #小爱推荐页面今日热点的定位
    today_hot_spots = By.XPATH,"//*[@resource-id='id584782680621581312']//*[@index='0']//*[@index='0']"
    # 今日热点页面标题
    today_hot_spots_tittle = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"

    # 点击今日热点
    def click_today_hot_spots(self):
        self.click(self.today_hot_spots)

    #小爱同学推荐-探索更多的的定位
    explore_more= By.XPATH,"//*[@resource-id='id572862681380298752']//*[@text='探索更多']"

    # 小爱同学推荐页面标题
    explore_more_title = By.ID, "com.xiaomi.xiaoailite:id/toolbar_title"

    # 点击小爱同学推荐-探索更多
    def click_explore_more(self):
        self.click(self.explore_more)
