from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# 登录页
class LoginPage(BaseAction):
    # 用户名输入框
    user_input = By.ID,"com.xiaomi.xiaoailite:id/userId"

    # 密码输入框
    password = By.ID,"com.xiaomi.xiaoailite:id/password"

    # 登录按钮
    login_button = By.ID,"com.xiaomi.xiaoailite:id/sign_in_btn"

    # 返回按钮
    back_button = By.XPATH,"//*[@content-desc='转到上一层级']"

    # 输入错误提示
    error_hint = By.ID,"com.xiaomi.xiaoailite:id/textinput_error"



    def input_user(self, username):
        self.input(self.user_input, username)

    def input_password(self, password):
        self.input(self.password, password)

    def click_login_button(self):
        self.click(self.login_button)

    def click_back_button(self):
        self.click(self.back_button)

