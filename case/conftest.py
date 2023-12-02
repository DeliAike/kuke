import os

import pytest
from airtest.core.api import auto_setup
from airtest.core.helper import set_logdir
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from page.index import IndexPage
from page.login_page import LoginPage
from page.my_page import MyPage
from page.setting_page import SettingPage
from tools.file_base_path import BASE_PATH_REPORT_LOG, PROJECT_PATH
from tools.tools_page import Tools

tool = Tools()
setting_page = SettingPage()
index_page = IndexPage()
my_page = MyPage()
login_page = LoginPage()

# -------------  测试登录的夹具  -------------------
# @pytest.fixture(scope='function')
def start_kuke():
    set_logdir(BASE_PATH_REPORT_LOG+"log")
    # 实例化poco对象
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    auto_setup(__file__, devices=[
        "android://127.0.0.1:5037/emulator-5554?cap_method=MINICAP&ori_method=ADBORI&touch_method=MINITOUCH&"])
    # 初始化打开应用
    index_page.init_kuke(poco)
    yield poco
    # 退出账号，退出app
    # 退出账号
    my_page.to_setting_page(poco)
    setting_page.logout(poco)

    # 杀死app进程
    tool.kill_app()

    # 生成报告
    simple_report(__file__, logpath=False, logfile=BASE_PATH_REPORT_LOG + 'log' + os.sep + 'log.txt', output=BASE_PATH_REPORT_LOG + 'report' + os.sep + 'login_report.html')

# -------------  测试收货地址的夹具  -------------------
@pytest.fixture(scope='session')
def logined():
    set_logdir(BASE_PATH_REPORT_LOG+"log")
    # 实例化poco对象
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/emulator-5554?cap_method=MINICAP&ori_method=ADBORI&touch_method=MINITOUCH&",])
    # 初始化打开应用
    index_page.init_kuke(poco)
    # 到‘我的’页面
    my_page.to_mypage(poco)
    # 通过手机号密码登录
    login_page.choose_tel_password(poco)
    login_page.input_tel_pw(poco, '18348443861', 'aa123456')
    login_page.checkagree_longin(poco)

    yield poco
    # 退出账号，退出app
    # 退出账号
    my_page.to_setting_page(poco)
    setting_page.logout(poco)
    # 杀死app进程
    tool.kill_app()
    # 生成报告
    simple_report(__file__, logpath=False, logfile=BASE_PATH_REPORT_LOG + 'log' + os.sep + 'log.txt', output=BASE_PATH_REPORT_LOG + 'report' + os.sep + 'login_report.html')
