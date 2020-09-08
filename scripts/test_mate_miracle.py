# # -*- coding:utf-8 -*-
#
# import time
# from base.driver import get_driver
# from page.page import Page
# import config
# import json
#
# def get_data():
#     with open(config.path+"\data\login.json",encoding='UTF-8')as f:
#         json_data = json.load(f)
#     login_info = json_data["login_info"]
#     return login_info
#
#
# class TestMateMiracle:
#
#     def setup(self):
#         self.driver = get_driver()
#         self.page = Page(self.driver)
#         self.wait = 3
#
#     def teardown(self):
#         time.sleep(3)
#         self.driver.quit()
#
#
#     def test_mate_miracle01(self):
#
#        #王茹楠：注释的是原代码
#         # time.sleep(3)
#         #
#         # login_activity = ''
#         # #进入我的同学圈
#         # self.page.homepage.click_xiaoai_schoolmate()
#         # time.sleep(self.wait)
#         # #判断是否为登录状态,已登录则退出登录
#         # pass
#         #
#         # # 点赞按钮测试
#         # #点击点赞按钮
#         # self.page.matemiraclepage.click_digg_button()
#         #
#         # #断言点赞后是否跳转登录页面
#         # assert self.driver.current_activity == login_activity
#         # log_msg = '第一步点赞完成'
#         # print(log_msg)
#         # #返回上级页面
#         # self.page.matemiraclepage.page_back(self.wait)
#         #
#         # # 评论按钮测试
#         # # 点击评论按钮
#         # self.page.matemiraclepage.click_comment_button()
#         # # 断言点赞后是否跳转登录页面
#         # assert self.driver.current_activity == login_activity
#         # # 返回上级页面
#         # self.page.matemiraclepage.page_back(self.wait)
#         #
#         # # 加入圈子按钮测试
#         # # 点击加入圈子按钮
#         # self.page.matemiraclepage.click_join_button()
#         # # 断言点赞后是否跳转登录页面
#         # assert self.driver.current_activity == login_activity
#         # # 返回上级页面
#         # self.page.matemiraclepage.page_back(self.wait)
#
# #因为点赞成功是没有文字提示的，不能断言，优化更改的
#         #     首页点击小爱同学圈，已登录，点击关注按钮，会有关注成功的提示
#         self.page.homepage.click_xiaoai_schoolmate()
#         #进入小爱社区-点击关注按钮
#         self.page.matemiraclepage.click_follow_button()
#
#         #断言：关注成功
#         assert self.page.matemiraclepage.is_toast_exist("关注成功")
#
#
#     #
#     def test_mate_miracle02(self):
#         # 王茹楠：注释的是原代码
#         # # 获取当前activity
#         # activity = self.driver.current_activity
#         #
#         # # 进入我的同学圈
#         # self.page.homepage.click_xiaoai_schoolmate()
#         # time.sleep(self.wait)
#         #
#         # log_msg = 'Step 1:进入小爱同学圈成功！'
#         # print(log_msg)
#         #
#         # #上下滑动
#         # for i in range(2):
#         #     self.page.matemiraclepage.scroll_page_one_time()
#         # log_msg = 'Step 2:上下滑动步骤成功！'
#         # print(log_msg)
#         # #返回上级页面
#         # self.page.matemiraclepage.page_back()
#         # #断言
#         # assert self.driver.current_activity == activity
#         # log_msg = '测试执行成功'
#         # print(log_msg)
#     #进入小爱同学圈
#        #     首页点击小爱同学圈，已登录
#
#         self.page.homepage.click_xiaoai_schoolmate()
#     # 进入小爱社区-点击关注的按钮
#         self.page.matemiraclepage.click_follow_button()
#         time.sleep(3)
#     #点击已关注的按钮
#         self.page.matemiraclepage.click_Nofollow_button()
#     # 断言：取消关注成功
#         assert self.page.matemiraclepage.is_toast_exist("已取消关注")