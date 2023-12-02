from base.base_login import Base_file

base = Base_file()

class MyPage():
    # 去我的页面
    def to_mypage(self, poco):
        base.click_to(poco,"com.kuke:id/iv_five_icon")

    # 点击我的信息 --> 登录
    def click_user(self, poco):
        base.click_to(poco, "com.kuke:id/textview1")

    # 去设置页面
    def to_setting_page(self, poco):
        base.move_page(poco, 0, -0.2)
        base.click_to(poco, "com.kuke:id/setting")


