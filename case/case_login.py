# -*- encoding=utf8 -*-
__author__ = "Jian"

import pytest
from base.base_login import Base_file
from page.index import IndexPage
from page.login_page import LoginPage
from page.my_page import MyPage
from tools.read_data_login import login_data, list_login
from tools.read_logindata_xlsx import list_login_xlsx

# 实例化page包的对象
my_page = MyPage()
index_page = IndexPage()
login_page = LoginPage()



class TestCase():


    # 手机号+密码登录
    @pytest.mark.parametrize('username, password',list_login_xlsx)
    def test_login(self, start_kuke, username, password):
        # 到‘我的’页面
        my_page.to_mypage(start_kuke)
        # 通过手机号密码登录
        login_page.choose_tel_password(start_kuke)
        login_page.input_tel_pw(start_kuke, username, password)
        login_page.checkagree_longin(start_kuke)






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




