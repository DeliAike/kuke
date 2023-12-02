from airtest.core.api import stop_app, home
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from base.base_login import Base_file

# 滑动页面
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
base = Base_file()

class Tools():
    def movePage(self, x, y):
        base.move_page(poco, x, y)

    def kill_app(self):
        home()
        stop_app("com.kuke")