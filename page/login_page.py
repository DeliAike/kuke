from airtest.core.api import sleep

from base.base_login import Base_file

base = Base_file()



# 手机号密码登录

# 点击登录

class LoginPage():
    # 选择账号密码登录
    def choose_tel_password(self, poco):
        base.click_to(poco, "com.kuke:id/textview1")
    # 输入账号密码
    def input_tel_pw(self, poco, user, password):
        base.click_to(poco, "com.kuke:id/toolbar_right")
        base.click_to(poco, "com.kuke:id/passwordLoginphoneNumber")
        base.enter_text(poco, "com.kuke:id/passwordLoginphoneNumber", user)
        base.click_to(poco, "com.kuke:id/passwordLoginpPassword")
        base.enter_text(poco, "com.kuke:id/passwordLoginpPassword", password)

    # 勾选用户协议并登录
    def checkagree_longin(self, poco):
        base.click_to(poco, "com.kuke:id/protocolCheckBox2")
        base.click_to(poco, "com.kuke:id/passwordLoginBT")



# 验证码登录
