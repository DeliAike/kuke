from airtest.core.api import start_app, sleep

from base.base_login import Base_file
base = Base_file()

class IndexPage():

    # 初始化
    def init_kuke(self, poco):
        start_app("com.kuke")
        sleep(5)

    #  去首页
    def to_index(self, poco):
        base.click_to(poco, "com.kuke:id/ok")

