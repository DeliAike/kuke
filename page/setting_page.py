from base.base_login import Base_file

base = Base_file()

# 退出账号
class SettingPage():
    def logout(self, poco):
        base.click_to(poco, "com.kuke:id/sign_out")
        base.click_to(poco, "com.kuke:id/ok")