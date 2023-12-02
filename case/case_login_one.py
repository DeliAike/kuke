# -*- encoding=utf8 -*-
__author__ = "Jian"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from base.base_login import Base_file
from page.index import index_page

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/emulator-5554?cap_method=MINICAP&ori_method=ADBORI&touch_method=MINITOUCH&",])
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 实例化base对象
base = Base_file()
# 实例化首页功能对象
index = index_page()
# script content

class MyPage():


    #初始化
    index.init_kuke()

    # 到‘我的’页面
    def to_mypage(self):
        start_app("com.kuke")
        sleep(5)
        base.click_to(poco, "com.kuke:id/iv_five_icon")

    # 回首页
    def to_home(self):
        base.click_to(poco, "com.kuke:id/ok")

    def kill_app(self):
        # 返回系统页面
        # home()
        # 杀死进程
        stop_app("com.kuke")

    # 通过手机号密码登录
    def to_loginpage(self, user, password):
        base.click_to(poco, "com.kuke:id/iv_five_icon")
        base.click_to(poco, "com.kuke:id/textview1")
        base.click_to(poco, "com.kuke:id/toolbar_right")
        base.click_to(poco, "com.kuke:id/passwordLoginphoneNumber")
        base.enter_text(poco, "com.kuke:id/passwordLoginphoneNumber", user)
        base.click_to(poco, "com.kuke:id/passwordLoginpPassword")
        base.enter_text(poco, "com.kuke:id/passwordLoginpPassword", password)
        base.click_to(poco, "com.kuke:id/protocolCheckBox2")
        base.click_to(poco, "com.kuke:id/passwordLoginBT")

    # 退出账号
    def logout(self):
        base.click_to(poco, "com.kuke:id/iv_five_icon")
        base.move_page(poco, 0, -0.2)
        base.click_to(poco, "com.kuke:id/setting")
        base.click_to(poco, "com.kuke:id/sign_out")
        base.click_to(poco, "com.kuke:id/ok")
#
# start_app("com.kuke")
#
# # 通过图片点击进入“库课网校”
# # poco("库课网校").click()
#
# # 等待广告
# # wait(Template(r"tpl1701162771708.png", record_pos=(-0.014, 0.809), resolution=(1080, 1920)))
# sleep(5)
#
# # 点击我的
# # poco("com.kuke:id/iv_five_icon").click()
# base.click_to(poco, "com.kuke:id/iv_five_icon")
#
# # 点击账号
# # poco("com.kuke:id/textview1").click()
# base.click_to(poco, "com.kuke:id/textview1")
#
# # 选择账号密码登录方式
# # poco("com.kuke:id/toolbar_right").click()
# base.click_to(poco, "com.kuke:id/toolbar_right")
#
# # 选择 --> 输入账号
# # poco("com.kuke:id/passwordLoginphoneNumber").click()
# base.click_to(poco, "com.kuke:id/passwordLoginphoneNumber")
# # poco("com.kuke:id/passwordLoginphoneNumber").set_text('18538078682')
# base.enter_text(poco, "com.kuke:id/passwordLoginphoneNumber", '18538078682')
#
# # 选择 --> 输入账号
# # poco("com.kuke:id/passwordLoginpPassword").click()
# base.click_to(poco, "com.kuke:id/passwordLoginpPassword")
# # poco("com.kuke:id/passwordLoginpPassword").set_text('y112233445566')
# base.enter_text(poco, "com.kuke:id/passwordLoginpPassword", 'y112233445566')
#
# # 勾选用户协议
# # poco("com.kuke:id/protocolCheckBox2").click()
# base.click_to(poco, "com.kuke:id/protocolCheckBox2")
#
# # 点击登录
# base.click_to(poco, "com.kuke:id/passwordLoginBT")
# # poco("com.kuke:id/passwordLoginBT").click()
#
#
# # 滑动
# # poco("android.view.View").swipe([0, -0.2])
# base.move_page(poco, 0, -0.2)
# # poco(text='在线咨询').swipe([0, -0.2])
# # poco.swipe([0.5,0.5], [0.5,0.1])
#
# # 点击设置
# # poco("com.kuke:id/setting").click()
# base.click_to(poco, "com.kuke:id/setting")
#
# # 点击退出
# base.click_to(poco, "com.kuke:id/sign_out")
# # poco("com.kuke:id/sign_out").click()
# #
# # 出现弹窗 --> 点击确认
# # poco("com.kuke:id/ok").click()
# base.click_to(poco, "com.kuke:id/ok")
#
# # 点击首页
# # poco("com.kuke:id/iv_first_icon").click()
# base.click_to(poco, "com.kuke:id/iv_first_icon")
#
# # 返回系统页面
# home()
#
# # 杀死进程
# stop_app("com.kuke")
#
#


# keyevent('KEYCODE_HOME')




