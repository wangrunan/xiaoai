import time

from base.driver import get_driver
from page.page import Page


class TestDomain:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
# calculate_tax
    #query：月薪一万要交多少税;
    def test_calculate_tax_01(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“月薪一万要交多少税”
        self.page.sessionpage.input_keyboard_input("月薪一万要交多少税")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"
        assert "缴纳个税" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    #query：计算个税; 十万;
    def test_calculate_tax_02(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“计算个税”
        self.page.sessionpage.input_keyboard_input("计算个税")

        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 返回
        self.driver.press_keycode(4)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“十万”
        self.page.sessionpage.input_keyboard_input("十万")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"
        assert "缴纳个税" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

# voice  声音
    # query：吸尘器的声音
    def test_voice_01(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“吸尘器的声音”
        self.page.sessionpage.input_keyboard_input("吸尘器的声音")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "听声音"

    # query：海浪声
    def test_voice_02(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“海浪声”
        self.page.sessionpage.input_keyboard_input("海浪声")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "听声音"

    #query：山猫的叫声
    def test_voice_03(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“山猫的叫声”
        self.page.sessionpage.input_keyboard_input("山猫的叫声")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "听声音"

# ask_recipe  烹饪
    #query：过油肉是哪个地方的菜;
    def test_ask_recipe_01(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“过油肉是哪个地方的菜”
        self.page.sessionpage.input_keyboard_input("过油肉是哪个地方的菜")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "菜谱"
        assert "晋菜" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_text)

    # query：做蛋挞需要注意什么;
    def test_ask_recipe_02(self):

        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“做蛋挞需要注意什么”
        self.page.sessionpage.input_keyboard_input("做蛋挞需要注意什么")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "菜谱"
        assert "烹调技巧" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_text)

    # query：鱼香肉丝的食材;
    def test_ask_recipe_03(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“鱼香肉丝的食材”
        self.page.sessionpage.input_keyboard_input("鱼香肉丝的食材")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "菜谱"
        assert "食材" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_text)

    # query：宫爆鸡丁的做法;
    def test_ask_recipe_04(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“宫爆鸡丁的做法”
        self.page.sessionpage.input_keyboard_input("宫爆鸡丁的做法")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "菜谱"
        assert "食材" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_text)

# open_application  打开应用

# class  课程表
#     query:打开课程表
    def test_class_01(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开课程表”
        self.page.sessionpage.input_keyboard_input("打开课程表")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    #     query:今天还有课吗
    def test_class_02(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天还有课吗”
        self.page.sessionpage.input_keyboard_input("今天还有课吗")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    #     query:数学老师是谁
    def test_class_03(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“数学老师是谁”
        self.page.sessionpage.input_keyboard_input("数学老师是谁")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    #     query:下节英语课在哪上
    def test_class_04(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“下节英语课在哪上”
        self.page.sessionpage.input_keyboard_input("下节英语课在哪上")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

    #     query:下周有几节课
    def test_class_05(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“下周有几节课”
        self.page.sessionpage.input_keyboard_input("下周有几节课")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"
# 聂露 9.6
    def test_class_06(self):
        time.sleep(6)
        self.page.homepage.click_keyboard()
        self.page.sessionpage.input_keyboard_input("明天有张老师的课吗")
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        assert self.driver.current_activity == ".widgets.web.WebActivity"


# weather  天气
    # query：海南今天的湿度;
    def test_weather_01(self):
        time.sleep(2)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“海南今天的湿度”
        self.page.sessionpage.input_keyboard_input("海南今天的湿度")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "湿度" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：这几天天气怎么样;
    def test_weather_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“这几天天气怎么样”
        self.page.sessionpage.input_keyboard_input("这几天天气怎么样")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "空气质量" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：鹿儿岛天气;
    def test_weather_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“鹿儿岛天气”
        self.page.sessionpage.input_keyboard_input("鹿儿岛天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "抱歉" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：下周天气怎么样;
    def test_weather_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“下周天气怎么样”
        self.page.sessionpage.input_keyboard_input("下周天气怎么样")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "小米天气"
        assert "下周" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query：最近五天的天气;
    def test_weather_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“最近五天的天气”
        self.page.sessionpage.input_keyboard_input("最近五天的天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "小米天气"
        assert "最近五天" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)


    # query：今天三亚的紫外线指数;
    def test_weather_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天三亚的紫外线指数”
        self.page.sessionpage.input_keyboard_input("今天三亚的紫外线指数")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "紫外线" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：北京最近的洗车指数;
    def test_weather_07(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“北京最近的洗车指数”
        self.page.sessionpage.input_keyboard_input("北京最近的洗车指数")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "洗车" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：本周天气;

    # query：今天上海天气;
    def test_weather_08(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天上海天气”
        self.page.sessionpage.input_keyboard_input("今天上海天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "上海" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：纽约天气怎么样;
    def test_weather_09(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“纽约天气怎么样”
        self.page.sessionpage.input_keyboard_input("纽约天气怎么样")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "纽约" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：未来一周天津的天气;
    def test_weather_10(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“未来一周天津的天气”
        self.page.sessionpage.input_keyboard_input("未来一周天津的天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "小米天气"
        assert "未来一周" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query：近十六天天气;
    def test_weather_11(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“近十六天天气”
        self.page.sessionpage.input_keyboard_input("近十六天天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "抱歉" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：未来十二天天气;
    def test_weather_12(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“未来十二天天气”
        self.page.sessionpage.input_keyboard_input("未来十二天天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "小米天气"
        assert "未来十二天" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)


    # query：最近几天的运动指数;
    def test_weather_13(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“最近几天的运动指数”
        self.page.sessionpage.input_keyboard_input("最近几天的运动指数")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"

    # query：明天的空气质量;
    def test_weather_14(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“明天的空气质量”
        self.page.sessionpage.input_keyboard_input("明天的空气质量")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "明天" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：现在天气;
    def test_weather_15(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“现在天气”
        self.page.sessionpage.input_keyboard_input("现在天气")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "小米天气"
        assert "现在" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# scence  场景化
    #query：我走了;
    def test_scence_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我走了”
        self.page.sessionpage.input_keyboard_input("我走了")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "拜拜" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：晚上好;
    def test_scence_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“晚上好”
        self.page.sessionpage.input_keyboard_input("晚上好")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "晚上" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


   # query：节日快乐;
    def test_scence_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“节日快乐”
        self.page.sessionpage.input_keyboard_input("节日快乐")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "问题" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：早上好;
    def test_scence_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“早上好”
        self.page.sessionpage.input_keyboard_input("早上好")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "一天" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：祝我生日快乐;
    def test_scence_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“生日快乐”
        self.page.sessionpage.input_keyboard_input("祝我生日快乐")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "生日快乐" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


    # query：我回来了;
    def test_scence_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我回来了”
        self.page.sessionpage.input_keyboard_input("我回来了")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "欢迎回家" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


# internalPlatform  升级

# auto  汽车
    #query：丰田霸道怎么样;
    def test_auto_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“丰田霸道怎么样”
        self.page.sessionpage.input_keyboard_input("丰田霸道怎么样")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "老司机"
        assert "其他参数" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    # query：奔驰有哪些型号;
    def test_auto_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“奔驰有哪些型号”
        self.page.sessionpage.input_keyboard_input("奔驰有哪些型号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "老司机"
        assert "奔驰" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query：十万能买什么车;
    def test_auto_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“十万能买什么车”
        self.page.sessionpage.input_keyboard_input("十万能买什么车")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "汽车之家"

    # query：二十万的宝马;
    def test_auto_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“二十万的宝马”
        self.page.sessionpage.input_keyboard_input("二十万的宝马")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "汽车之家"

    # query：新款奥迪;
    def test_auto_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“新款奥迪”
        self.page.sessionpage.input_keyboard_input("新款奥迪")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "汽车之家"

    # query：奔驰有哪些车型;
    def test_auto_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“奔驰有哪些车型”
        self.page.sessionpage.input_keyboard_input("奔驰有哪些车型")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "老司机"

# play_music  音乐


#ask_date 询问日期
    # query:今天几号
    def test_today_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        #对话页输入“今天几号”
        self.page.sessionpage.input_keyboard_input("今天几号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"



    # query：明天是不是周五
    def test_tomorrow_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        #对话页输入“明天是不是周五”
        self.page.sessionpage.input_keyboard_input("明天是不是周五")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert "是" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：今天离元旦还有多久
    def test_new_year_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天离元旦还有多久”
        self.page.sessionpage.input_keyboard_input("今天离元旦还有多久")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"
        assert "元旦" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：正月初一是几号
    def test_one_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“正月初一是几号”
        self.page.sessionpage.input_keyboard_input("正月初一是几号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"
        assert "正月初一" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：清明节是几号
    def test_qingming_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“清明节是几号”
        self.page.sessionpage.input_keyboard_input("清明节是几号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"
        assert "清明节" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


    # query：美国今天周几
    def test_America__today_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“美国今天周几”
        self.page.sessionpage.input_keyboard_input("美国今天周几")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"


    # query：现在离二零二一年还有多久
    def test_from_2021_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“现在离二零二零年还有多久”
        self.page.sessionpage.input_keyboard_input("现在离二零二一年还有多久")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "二零二一年" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：大前天是几号
    def test_three_day_ago_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“大前天是几号”
        self.page.sessionpage.input_keyboard_input("大前天是几号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"
        assert "大前天" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)



    # query：九月十号是周几
    def test_week_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“九月十号是周几”
        self.page.sessionpage.input_keyboard_input("九月十号是周几")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"
        assert "九月十号" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)



    # query：大大前天阴历是几号
    def test_four_day_ago_date(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“大大前天阴历是几号”
        self.page.sessionpage.input_keyboard_input("大大前天阴历是几号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"
        assert "农历" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# 聂露 9.6
# query：今天星期几
    def test_calendar(self):
        time.sleep(5)
        self.page.homepage.click_keyboard()
        self.page.sessionpage.input_keyboard_input("今天星期几")
        self.page.sessionpage.click_send_button()
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"
        assert "今天是" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# poem  古诗词
    # query:来一首唐诗; 暂停;
    def test_to_a_poem(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“来一首唐诗”
        self.page.sessionpage.input_keyboard_input("来一首唐诗")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 点击暂停播放按钮
        self.page.sessionpage.click_big_card_play_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "诗词歌赋"



    # query:出师表; 暂停;
    def test_to_chushibiao_poem(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“出师表”
        self.page.sessionpage.input_keyboard_input("出师表")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 点击暂停播放按钮
        self.page.sessionpage.click_big_card_play_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "诗词歌赋"
        assert "出师表" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_content_tittle)



    # query:床前明月光的下一句是什么;
    def test_next_line_poem(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“床前明月光的下一句是什么”
        self.page.sessionpage.input_keyboard_input("床前明月光的下一句是什么")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert "疑是地上霜" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

# 计算数量
    #query：把五百五十五元变成大写
    def test_count_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“把五百五十五元变成大写”
        self.page.sessionpage.input_keyboard_input("把五百五十五元变成大写")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"


    #query：100除以0是多少;
    def test_count_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“100除以0是多少”
        self.page.sessionpage.input_keyboard_input("100除以0是多少")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"

    # query：十一乘以十二;
    def test_count_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“十一乘以十二”
        self.page.sessionpage.input_keyboard_input("十一乘以十二")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"

    # query：十乘以十;
    def test_count_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“十乘以十”
        self.page.sessionpage.input_keyboard_input("十乘以十")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"
        assert self.page.sessionpage.get_text(self.page.sessionpage.tts_reply) == "答案是一百"
#9.6 熊浩
    def test_count_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“十乘以十”
        self.page.sessionpage.input_keyboard_input("身高1米6标准体重是多少")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"
        assert self.page.sessionpage.get_text(self.page.sessionpage.tts_reply) == "标准体重为54.0千克"

    def test_count_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“十乘以十”
        self.page.sessionpage.input_keyboard_input("爸爸的小姨叫什么")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"
        assert self.page.sessionpage.get_text(self.page.sessionpage.tts_reply) == "你可以喊他祖姨母"

# 开方平台
    # query：数字对战:退出
    def test_open_platfrom_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“数字对战”
        self.page.sessionpage.input_keyboard_input("数字对战")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        #断言
        assert "欢迎进入游戏" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)
        #  点击返回
        self.driver.press_keycode(keycode=4)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“退出”
        self.page.sessionpage.input_keyboard_input("退出")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "再见" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #query:我爱猜歌名; 退出
    def test_open_platfrom_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我爱猜歌名”
        self.page.sessionpage.input_keyboard_input("我爱猜歌名")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".ai.request.openplatform.OpenPlatformActivity"

    # query:成语接龙; 退出
    def test_open_platfrom_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“成语接龙”
        self.page.sessionpage.input_keyboard_input("成语接龙")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".ai.request.openplatform.OpenPlatformActivity"

    # query:种树; 退出
    def test_open_platfrom_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“种树”
        self.page.sessionpage.input_keyboard_input("种树")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "小树" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query:打开最强大脑; 退出
    def test_open_platfrom_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开最强大脑”
        self.page.sessionpage.input_keyboard_input("打开最强大脑")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".ai.request.openplatform.OpenPlatformActivity"


# ask_custom
    #query：梦到猪是什么意思
    def test_ask_custom_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“梦到猪是什么意思”
        self.page.sessionpage.input_keyboard_input("梦到猪是什么意思")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "科技紫薇"
        assert "周公解梦" in self.page.sessionpage.get_text(self.page.sessionpage.small_card_content_tittle)


    # query：1994年属什么的;
    def test_ask_custom_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“1994年属什么的”
        self.page.sessionpage.input_keyboard_input("1994年属什么的")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "科技紫薇"
        assert "生肖狗" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：生肖猪的性格怎么样;
    def test_ask_custom_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“生肖猪的性格怎么样”
        self.page.sessionpage.input_keyboard_input("生肖猪的性格怎么样")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "科技紫薇"
        assert "生肖猪" in self.page.sessionpage.get_text(self.page.sessionpage.small_card_content_tittle)

# ask_attraction
    #query：台北故宫需要玩多久;
    def test_ask_attraction_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“台北故宫需要玩多久”
        self.page.sessionpage.input_keyboard_input("台北故宫需要玩多久")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "马蜂窝"
        assert "游玩时间" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query：黄鹤楼门票多少钱;
    def test_ask_attraction_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“黄鹤楼门票多少钱”
        self.page.sessionpage.input_keyboard_input("黄鹤楼门票多少钱")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "马蜂窝"
        assert "票价" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    #query：颐和园简介;
    def test_ask_attraction_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“颐和园简介”
        self.page.sessionpage.input_keyboard_input("颐和园简介")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "马蜂窝"
        assert "颐和园" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)


    # query：洛杉矶有什么好玩的;
    def test_ask_attraction_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“洛杉矶有什么好玩的”
        self.page.sessionpage.input_keyboard_input("洛杉矶有什么好玩的")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "马蜂窝"
        assert "好莱坞" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    #query：台湾有哪些小吃;
    def test_ask_attraction_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“台湾有哪些小吃”
        self.page.sessionpage.input_keyboard_input("台湾有哪些小吃")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "马蜂窝"
        assert "卤肉饭" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

#ask_film
    # query：最近有什么好看的电影;
    def test_ask_film(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“最近有什么好看的电影”
        self.page.sessionpage.input_keyboard_input("最近有什么好看的电影")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "近期热映电影" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# 百科
    #百科一下中秋节;（节日）
    def test_cyclopedia_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“百科一下中秋节”
        self.page.sessionpage.input_keyboard_input("百科一下中秋节")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "百度百科"
        assert "中秋节" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    #query: 百科一下雷军;（人物）
    def test_cyclopedia_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“百科一下雷军”
        self.page.sessionpage.input_keyboard_input("百科一下雷军")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "百度百科"
        assert "雷军" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query:胡歌的代表作;（主要作品）
    def test_cyclopedia_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“胡歌的代表作”
        self.page.sessionpage.input_keyboard_input("胡歌的代表作")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "百度百科" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        assert "代表作品" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query:百科一下小米公司;（公司）
    def test_cyclopedia_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“百科一下小米公司”
        self.page.sessionpage.input_keyboard_input("百科一下小米公司")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "百度百科"
        assert "小米" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query:詹姆斯哈登是谁;（人物）
    def test_cyclopedia_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“詹姆斯哈登是谁”
        self.page.sessionpage.input_keyboard_input("詹姆斯哈登是谁")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "百度百科·人物"
        assert "詹姆斯·哈登" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query:百科一下马到成功;
    def test_cyclopedia_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“百科一下马到成功”
        self.page.sessionpage.input_keyboard_input("百科一下马到成功")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "百度百科"
        assert "马到成功" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

# ask_time
    #query:纽约现在几点了;
    def test_ask_time_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“纽约现在几点了”
        self.page.sessionpage.input_keyboard_input("纽约现在几点了")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "时钟"

    #query：现在几点了;
    def test_ask_time_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“现在几点了”
        self.page.sessionpage.input_keyboard_input("现在几点了")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "时钟"

# help
    #query： 你会干什么
    def test_help(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你会干什么”
        self.page.sessionpage.input_keyboard_input("你会干什么")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.driver.current_activity == ".widgets.web.WebActivity"

#estates(房产)
    # query：佛奥俊贤雅居的房价;
    def test_estates_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“佛奥俊贤雅居的房价”
        self.page.sessionpage.input_keyboard_input("佛奥俊贤雅居的房价")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "贝壳找房"
        assert "均价" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #query：保利时代的房价;
    def test_estates_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“保利时代的房价”
        self.page.sessionpage.input_keyboard_input("保利时代的房价")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "贝壳找房"
        assert "均价" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

#soundboxnews 疫情
    #query:肺炎疫情
    def test_epidemic(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“肺炎疫情”
        self.page.sessionpage.input_keyboard_input("肺炎疫情")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert "确诊" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# customer
    #  Air2耳机如何充电;
    def test_customer_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“Air2耳机如何充电”
        self.page.sessionpage.input_keyboard_input("Air2耳机如何充电")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "客户服务"

    # 小米蓝牙音箱小爱版如何充电;
    def test_customer_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“小米蓝牙音箱小爱版如何充电”
        self.page.sessionpage.input_keyboard_input("小米蓝牙音箱小爱版如何充电")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "客户服务"

    # 	App内连接蓝牙设备失败;
    def test_customer_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“App内连接蓝牙设备失败”
        self.page.sessionpage.input_keyboard_input("App内连接蓝牙设备失败")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "客户服务"

#8.29日，熊浩新增2条
    #手机发烫怎么办
    def test_customer_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“手机发烫怎么办”
        self.page.sessionpage.input_keyboard_input("手机发烫怎么办")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "客户服务"
#小米和红米有什么区别
    def test_customer_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“小米和红米有什么区别”
        self.page.sessionpage.input_keyboard_input("小米和红米有什么区别")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "客户服务"


#mobilecontrolios  执行技能回答
    # query：屏幕亮一点

    # 屏幕暗一点


    # 关闭GPS
    def test_mobilecontrolios_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“关闭GPS”
        self.page.sessionpage.input_keyboard_input("关闭GPS")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(2)
        # 断言
        assert self.driver.current_activity == ".Settings$LocationSettingsActivity"

    # 打开GPS
    def test_mobilecontrolios_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开GPS”
        self.page.sessionpage.input_keyboard_input("打开GPS")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "已打开" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

#translation 翻译
    # query：今天天气真好用日语怎么说;
    def test_translation_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天天气真好用日语怎么说”
        self.page.sessionpage.input_keyboard_input("今天天气真好用日语怎么说")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "翻译"

    # query：我爱你的法文是什么;
    def test_translation_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我爱你的法文是什么”
        self.page.sessionpage.input_keyboard_input("我爱你的法文是什么")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "翻译"

    # query：苹果的英文怎么说;;
    def test_translation_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“苹果的英文怎么说”
        self.page.sessionpage.input_keyboard_input("苹果的英文怎么说")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "翻译"

# ask_medical  医疗
    #query：怎么预防颈椎病;
    def test_ask_medical_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“怎么预防颈椎病”
        self.page.sessionpage.input_keyboard_input("怎么预防颈椎病")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "百科名医"
        assert "颈椎病" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


    # query：阿司匹林有什么副作用吗;
    def test_ask_medical_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“阿司匹林有什么副作用吗”
        self.page.sessionpage.input_keyboard_input("阿司匹林有什么副作用吗")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "春雨医生"
        assert "不良反应" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    #query：肠胃炎怎么办;
    def test_ask_medical_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“肠胃炎怎么办”
        self.page.sessionpage.input_keyboard_input("肠胃炎怎么办")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "春雨医生"
        assert "肠胃炎" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)


    #query：怎么治疗失眠;
    def test_ask_medical_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“怎么治疗失眠”
        self.page.sessionpage.input_keyboard_input("怎么治疗失眠")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "百科名医"
        assert "失眠" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


    #query：扁桃体炎有什么症状;
    def test_ask_medical_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“扁桃体炎有什么症状”
        self.page.sessionpage.input_keyboard_input("扁桃体炎有什么症状")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "百科名医"
        assert "扁桃体炎" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)


    #query：怎么预防脊椎病;
    def test_ask_medical_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“怎么预防脊椎病”
        self.page.sessionpage.input_keyboard_input("怎么预防脊椎病")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "春雨医生"
        assert "脊椎病" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    #query：肺结核都有什么症状;
    def test_ask_medical_07(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“肺结核都有什么症状”
        self.page.sessionpage.input_keyboard_input("肺结核都有什么症状")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "百科名医"
        assert "肺结核" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# ask_restriction限行尾号
    #query：北京今天的限行尾号;
    def test_ask_restriction_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“北京今天的限行尾号”
        self.page.sessionpage.input_keyboard_input("北京今天的限行尾号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "不限行" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #query：北京今天限行到几点;
    def test_ask_restriction_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“北京今天限行到几点”
        self.page.sessionpage.input_keyboard_input("北京今天限行到几点")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "限行" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #query：我的车牌号是多少;

    #query：武汉今天的限行尾号;
    def test_ask_restriction_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“武汉今天的限行尾号”
        self.page.sessionpage.input_keyboard_input("武汉今天的限行尾号")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "暂不支持" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #query：北京今天限行尾号是6吗;
    def test_ask_restriction_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“北京今天限行尾号是6吗”
        self.page.sessionpage.input_keyboard_input("北京今天限行尾号是6吗")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "不限行" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# remind  日程
    #query：下午2点半提醒我喝水;
    def test_remind_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“下午2点半提醒我喝水”
        self.page.sessionpage.input_keyboard_input("下午2点半提醒我喝水")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "日历"

    #query：停止闹钟;
    def test_remind_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“停止闹钟”
        self.page.sessionpage.input_keyboard_input("停止闹钟")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "超出了小爱当前的能力范围" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# joke  笑话
    # query：来个笑话;
    def test_joke_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“来个笑话”
        self.page.sessionpage.input_keyboard_input("来个笑话")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "一点资讯"

#9.6 聂露
    def test_child_joke(self):
        time.sleep(3)
        self.page.homepage.click_keyboard()
        self.page.sessionpage.input_keyboard_input("儿童笑话")
        self.page.sessionpage.click_send_button()
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "笑话"
        assert "好哒" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# area_convert 换算
    # 一平方米等于多少平方厘米;
    def test_area_convert_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“一平方米等于多少平方厘米”
        self.page.sessionpage.input_keyboard_input("一平方米等于多少平方厘米")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"

# miot  智能家庭


# chat  闲聊
    #query：你爸爸妈妈是谁;
    def test_chatt_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你爸爸妈妈是谁”
        self.page.sessionpage.input_keyboard_input("你爸爸妈妈是谁")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "工程师" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：陪我聊天; 你叫什么名字;
    def test_chatt_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“陪我聊天”
        self.page.sessionpage.input_keyboard_input("陪我聊天")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".ai.request.openplatform.OpenPlatformActivity"
        # 点击返回
        self.driver.press_keycode(4)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你叫什么名字”
        self.page.sessionpage.input_keyboard_input("你叫什么名字")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "小爱" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


    # query：你几岁了;
    def test_chatt_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“你几岁了”
        self.page.sessionpage.input_keyboard_input("你几岁了")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "年龄" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# map


# ask_stock  查询股票
    #query：小米股票涨了吗;
    def test_ask_stock_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“小米股票涨了吗”
        self.page.sessionpage.input_keyboard_input("小米股票涨了吗")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "股票"
        assert "小米集团" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：推荐一支股票;;
    def test_ask_stock_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“推荐一支股票”
        self.page.sessionpage.input_keyboard_input("推荐一支股票")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "抱歉" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query：今天沪市大盘走势如何
    def test_ask_stock_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“今天沪市大盘走势如何”
        self.page.sessionpage.input_keyboard_input("今天沪市大盘走势如何")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "股票"
        assert "上证指数" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

# ask_station  电台


# person  人
    #query：三国演义是谁写的;
    def test_person_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“三国演义是谁写的”
        self.page.sessionpage.input_keyboard_input("三国演义是谁写的")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "罗贯中" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    # query：刘德华是谁;
    def test_person_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“刘德华是谁”
        self.page.sessionpage.input_keyboard_input("刘德华是谁")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "百度百科·人物"

    #query：泰坦尼克号的主演;
    def test_person_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“泰坦尼克号的主演”
        self.page.sessionpage.input_keyboard_input("泰坦尼克号的主演")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "人物·视频"


# qa   问答
    #query：世界上最长的河流;
    def test_qa_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“世界上最长的河流是什么”
        self.page.sessionpage.input_keyboard_input("世界上最长的河流")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "智能问答"
        # assert "尼罗河" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    # query：端午节为什么要吃粽子;
    def test_qa_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“端午节为什么要吃粽子”
        self.page.sessionpage.input_keyboard_input("端午节为什么要吃粽子")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "智能问答"


    #query：太阳系有哪些行星;
    def test_qa_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“太阳系有哪些行星”
        self.page.sessionpage.input_keyboard_input("太阳系有哪些行星")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon) == "智能问答"
        assert "火星" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)


# followme   跟我学
    #query：跟我学叫我哥哥;
    def test_followme_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“跟我学叫我哥哥”
        self.page.sessionpage.input_keyboard_input("跟我学叫我哥哥")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.tts_reply) == "哥哥"

    # query：跟我学; 哥哥; 退出;
    def test_followme_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“跟我学”
        self.page.sessionpage.input_keyboard_input("跟我学")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "我可以学你说话" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)
        # 返回
        self.driver.press_keycode(4)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“哥哥”
        self.page.sessionpage.input_keyboard_input("哥哥")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.tts_reply) == "哥哥"

# ask_constellation  星座
    #query：天蝎座优点;
    def test_ask_constellation_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“天蝎座优点”
        self.page.sessionpage.input_keyboard_input("天蝎座优点")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "优点" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    # query：金牛座的工作运势;
    def test_ask_constellation_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“金牛座的工作运势”
        self.page.sessionpage.input_keyboard_input("金牛座的工作运势")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "事业运势" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    #query：水瓶座的幸运颜色;
    def test_ask_constellation_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“水瓶座的幸运颜色”
        self.page.sessionpage.input_keyboard_input("水瓶座的幸运颜色")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "整体运势" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    #query：水瓶座本周运势;
    def test_ask_constellation_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“水瓶座本周运势”
        self.page.sessionpage.input_keyboard_input("水瓶座本周运势")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "整体运势" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

    # query：天蝎座和白羊座;
    def test_ask_constellation_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“天蝎座和白羊座”
        self.page.sessionpage.input_keyboard_input("天蝎座和白羊座")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "争锋相对型" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)

# money_convert  换算
    # query：一百日元是多少人民币;
    def test_money_convert_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“一百日元是多少人民币”
        self.page.sessionpage.input_keyboard_input("一百日元是多少人民币")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "汇率转换" in self.page.sessionpage.get_text(self.page.sessionpage.small_card_content_tittle)
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"

    # 一升等于多少米;
    def test_money_convert_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“一升等于多少米”
        self.page.sessionpage.input_keyboard_input("一升等于多少米")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "无法进行转换" in self.page.sessionpage.get_text(self.page.sessionpage.samall_card_text)
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"

# ask_openplatform  小冰
    # query：召唤小冰
    def test_ask_openplatform_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“召唤小冰”
        self.page.sessionpage.input_keyboard_input("召唤小冰")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".ai.request.openplatform.OpenPlatformActivity"
        #返回
        self.driver.press_keycode(4)
        assert self.driver.current_activity == ".presenter.main.MainTabActivity"


# stock  股票
    #query:查询大盘走势
    def test_stock_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“查询大盘走势”
        self.page.sessionpage.input_keyboard_input("查询大盘走势")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "股市行情" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "股票"

# relative_convert  关系
    #query：爸爸的爸爸的女儿的儿子
    def test_relative_convert_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“爸爸的爸爸的女儿的儿子”
        self.page.sessionpage.input_keyboard_input("爸爸的爸爸的女儿的儿子")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "亲戚计算" in self.page.sessionpage.get_text(self.page.sessionpage.small_card_content_tittle)
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "计算器"


# 刘锐(放到test_openapp里面了，如果一个手机可以跑，可以取消注释）
# 打开app
    #  query:打开计算器
    def test_open_app_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开计算器”
        self.page.sessionpage.input_keyboard_input("打开计算器")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".Calculator"

    #  query:打开照相机
    def test_open_app_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开照相机”
        self.page.sessionpage.input_keyboard_input("打开照相机")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".camera"

    #  query:打开相册
    def test_open_app_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开相册”
        self.page.sessionpage.input_keyboard_input("打开相册")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == "com.huawei.gallery.app.GalleryMain"

    #  query:打开设置
    def test_open_app_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开设置”
        self.page.sessionpage.input_keyboard_input("打开设置")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".HWSettings"

    #  query:打开微信
    def test_open_app_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开微信”
        self.page.sessionpage.input_keyboard_input("打开微信")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".plugin.account.ui.LoginPasswordUI"

    #  query:打开日历
    def test_open_app_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开日历”
        self.page.sessionpage.input_keyboard_input("打开日历")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".AllInOneActivity"

    #  query:打开地图  （已下载高德地图）
    def test_open_app_07(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开地图”
        self.page.sessionpage.input_keyboard_input("打开地图")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == "com.autonavi.map.activity.NewMapActivity"

    #  query:打开微博（未安装微博）
    def test_open_app_08(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开微博”
        self.page.sessionpage.input_keyboard_input("打开微博")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "下载" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #  query:打开文件管理
    def test_open_app_09(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开文件”
        self.page.sessionpage.input_keyboard_input("打开文件管理")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".filemanager.FileManager"

# 尚景
#     音乐
    #   query：我想听浮夸
    def test_music_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我想听浮夸”
        self.page.sessionpage.input_keyboard_input("我想听浮夸")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 点击暂停
        self.page.sessionpage.click_big_card_play_button()
        # 断言
        assert "QQ音乐" in self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon)



    #   query：声音大一点
    def test_music_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“声音大一点”
        self.page.sessionpage.input_keyboard_input("声音大一点")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "好的" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #   query：声音小一点
    def test_music_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“声音小一点”
        self.page.sessionpage.input_keyboard_input("声音小一点")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "好的" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # query:收藏歌曲(未播放）
    def test_music_04(self):
        time.sleep(3)
        # 点击键盘
        self.page.homepage.click_keyboard()
        # 输入内容
        self.page.sessionpage.input_keyboard_input("收藏歌曲")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "好的" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    # 收藏歌曲（播放) (QQ音乐未登录)
    def test_music_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我想听浮夸”
        self.page.sessionpage.input_keyboard_input("我想听浮夸")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 点击暂停
        self.page.sessionpage.click_big_card_play_button()
        # 按返回键
        self.driver.press_keycode(4)
        time.sleep(3)
        # 再次输入
        self.page.homepage.click_keyboard()
        self.page.sessionpage.input_keyboard_input("收藏歌曲")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "失败" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #   query：播放刘德华的专辑
    def test_music_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“播放刘德华的专辑”
        self.page.sessionpage.input_keyboard_input("播放刘德华的专辑")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 点击暂停
        self.page.sessionpage.click_big_card_play_button()
        # 断言
        assert "QQ音乐" in self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon)

    #   query：随机播放
    def test_music_07(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“随机播放”
        self.page.sessionpage.input_keyboard_input("随机播放")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "随机" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #   query：单曲循环
    def test_music_08(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“单曲循环”
        self.page.sessionpage.input_keyboard_input("单曲循环")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "单曲循环" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #   query：列表循环
    def test_music_09(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“列表循环”
        self.page.sessionpage.input_keyboard_input("列表循环")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "列表循环" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #   query：上一首
    def test_music_10(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“上一首”
        self.page.sessionpage.input_keyboard_input("上一首")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "好的" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)

    #   query：下一首
    def test_music_11(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“下一首”
        self.page.sessionpage.input_keyboard_input("下一首")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "好的" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


# 熊浩
    #query：国内新闻
    def test_news(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“国内新闻”
        self.page.sessionpage.input_keyboard_input("国内新闻")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == ".widgets.web.BrowserActivity"

    # query：帮我找一下手机
    def test_insignificance_query(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“帮我找一下手机”
        self.page.sessionpage.input_keyboard_input("帮我找一下手机")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "不支持" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


# 词典
    #query：淼怎么读
    def test_dictionary_01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“淼怎么读”
        self.page.sessionpage.input_keyboard_input("淼怎么读")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典"== self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    #query：美怎么组词
    def test_dictionary_02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“美怎么组词”
        self.page.sessionpage.input_keyboard_input("美怎么组词")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "美" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)
    #query：大夫的拼音
    def test_dictionary_03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“大夫的拼音”
        self.page.sessionpage.input_keyboard_input("大夫的拼音")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "大夫" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)
    #query：臭味相投的拼音
    def test_dictionary_04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“臭味相投的拼音”
        self.page.sessionpage.input_keyboard_input("臭味相投的拼音")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "臭味相投" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)
    #query：丁开头的成语有什么
    def test_dictionary_05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“丁开头的成语有什么”
        self.page.sessionpage.input_keyboard_input("丁开头的成语有什么")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "丁" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)
    #query：包含二的成语
    def test_dictionary_06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“包含二的成语”
        self.page.sessionpage.input_keyboard_input("包含二的成语")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "二" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)
    #query：千钧一发的钧是什么意思
    def test_dictionary_07(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“千钧一发的钧是什么意思”
        self.page.sessionpage.input_keyboard_input("千钧一发的钧是什么意思")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "千钧一发" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)
    #query：饕餮的出处
    def test_dictionary_08(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“饕餮的出处”
        self.page.sessionpage.input_keyboard_input("饕餮的出处")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "饕餮" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query：美丽的近义词
    def test_dictionary_09(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“美丽的近义词”
        self.page.sessionpage.input_keyboard_input("美丽的近义词")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "美丽" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)

    # query：丑陋的反义词
    def test_dictionary_10(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“丑陋的反义词”
        self.page.sessionpage.input_keyboard_input("丑陋的反义词")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "字词典" == self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)
        # assert "丑陋" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_tts_reply)


#     熊浩
    #query：手机有多少电量
    def test_phone_battery(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“手机有多少电量”
        self.page.sessionpage.input_keyboard_input("手机有多少电量")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert "手机剩余电量" in self.page.sessionpage.get_text(self.page.sessionpage.tts_reply)


# 客户端支持语音直达重置native页面
    #未登录 query:我要反馈
    def test_feedback_1(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 点击返回按钮
            self.page.centerpage.click_back_button()
            # 首页点击键盘
            self.page.homepage.click_keyboard()
            # 对话页输入“我要反馈”
            self.page.sessionpage.input_keyboard_input("我要反馈")
            # 对话页点击发送
            self.page.sessionpage.click_send_button()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"
            return
        #退出登录
        self.page.centerpage.click_out_login()
        #点击好的
        self.page.centerpage.click_ok_button()
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我要反馈”
        self.page.sessionpage.input_keyboard_input("我要反馈")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == "com.xiaomi.passport.ui.internal.AddAccountActivity"

    # 登录 query:我要反馈
    def test_feedback_2(self):
        # 首页点击个人中心按钮
        self.page.homepage.click_center_button()
        if self.page.centerpage.if_login():  # 登录：False,未登录：True
            # 未登陆，登录账号
            self.page.centerpage.click_login_tab()
            self.page.loginpage.input_user("15527619642")
            self.page.loginpage.input_password("t1005033132")
            self.page.loginpage.click_login_button()
            # 点击返回按钮
            self.page.centerpage.click_back_button()
            # 首页点击键盘
            self.page.homepage.click_keyboard()
            # 对话页输入“我要反馈”
            self.page.sessionpage.input_keyboard_input("我要反馈")
            # 对话页点击发送
            self.page.sessionpage.click_send_button()
            time.sleep(3)
            # 断言
            assert self.driver.current_activity == "com.xiaomi.bluetooth.activity.QuestionFeedBackActivity"
            return
        # 点击返回按钮
        self.page.centerpage.click_back_button()
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我要反馈”
        self.page.sessionpage.input_keyboard_input("我要反馈")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert self.driver.current_activity == "com.xiaomi.bluetooth.activity.QuestionFeedBackActivity"


    # 8.23新增（谭经标）
# 作文
    # query：我想找议论文
    def test_composition01(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我想找议论文”
        self.page.sessionpage.input_keyboard_input("我想找议论文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    # query：三年级500字作文
    def test_composition02(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“三年级500字作文”
        self.page.sessionpage.input_keyboard_input("三年级500字作文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    # query：小学六年级的记叙文
    def test_composition03(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“小学六年级的记叙文”
        self.page.sessionpage.input_keyboard_input("小学六年级的记叙文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    # query：我的爸爸作文
    def test_composition04(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我的爸爸作文”
        self.page.sessionpage.input_keyboard_input("我的爸爸作文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

#8.29新增（谭经标）
    # query：我的爸爸三年级作文
    def test_composition05(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我的爸爸三年级作文”
        self.page.sessionpage.input_keyboard_input("我的爸爸三年级作文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    # query：我的爸爸小学作文
    def test_composition06(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我的爸爸小学作文”
        self.page.sessionpage.input_keyboard_input("我的爸爸小学作文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    # query：我的爸爸500字作文
    def test_composition07(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我的爸爸500字作文”
        self.page.sessionpage.input_keyboard_input("我的爸爸500字作文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    # query：我的爸爸三年级500字作文
    def test_composition08(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“我的爸爸三年级500字作文”
        self.page.sessionpage.input_keyboard_input("我的爸爸三年级500字作文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        time.sleep(3)
        # 断言
        assert "第一范文网" in self.page.sessionpage.get_text(self.page.sessionpage.big_card_icon)

    # 8.23新增（尚景）
    # 翻译类query
    # 翻译小卡优化(query 苹果的英文)
    def test_apple_english(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“苹果的英文”
        self.page.sessionpage.input_keyboard_input("苹果的英文")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        assert self.page.sessionpage.get_text(self.page.sessionpage.small_card_icon) == "翻译"


    # query打开翻译进入翻译页面
    def test_query_translation(self):
        time.sleep(3)
        # 首页点击键盘
        self.page.homepage.click_keyboard()
        # 对话页输入“打开翻译”
        self.page.sessionpage.input_keyboard_input("打开翻译")
        # 对话页点击发送
        self.page.sessionpage.click_send_button()
        # 断言
        # ren_msg = self.page.sessionpage.ren_translation_title()
        # assert "对话翻译" == ren_msg
        assert self.page.sessionpage.is_toast_exist('对话翻译')




