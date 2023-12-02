from airtest.core.api import sleep

from base.base_login import Base_file

base = Base_file()



# 手机号密码登录

# 点击登录

class AddressPage():

    # 在’我的‘页面点击收货地址
    def to_address(self, poco):
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.kuke:id/main_framelayout").offspring("com.kuke:id/nestedScrollView").offspring("com.kuke:id/h_scroll_view").child("android.widget.LinearLayout").child("android.widget.LinearLayout")[1].child("com.kuke:id/iv_icon").click()


    # 新增收货地址
    def add_address(self, poco, name, phone,area1, area2, area3, address):
        base.click_to(poco, "com.kuke:id/add_address")  # 点击’新增收货地址‘
        base.click_to(poco, "com.kuke:id/nameET")       # 点击收货人
        base.enter_text(poco, "com.kuke:id/nameET", name)      # 输入收货人
        base.click_to(poco, "com.kuke:id/phoneET")          # 点击手机号
        base.enter_text(poco, "com.kuke:id/phoneET", phone)        # 输入手机号
        base.click_to(poco, "com.kuke:id/areaTV")          # 点击所在地区
        poco.swipe([0.5, 0.9], [0.5, 0])
        base.pull_list(poco, area1)  # 选择省级地区
        base.pull_list(poco, area2)  # 选择市级地区
        base.pull_list(poco, area3)  # 选择区级地区
        base.click_to(poco, "com.kuke:id/addressET")   # 输入详细地址
        base.enter_text(poco, "com.kuke:id/addressET", address) # 输入
        base.click_to(poco, "com.kuke:id/saveBT")       # 点击保存


    # 修改收货地址
    def update_address(self, poco, name, phone,area1, area2, area3, address):
        base.click_to(poco, "com.kuke:id/edit_address")  # 点击’修改收货地址‘
        base.click_to(poco, "com.kuke:id/nameET")  # 点击收货人
        base.enter_text(poco, "com.kuke:id/nameET", name)  # 输入收货人
        base.click_to(poco, "com.kuke:id/phoneET")  # 点击手机号
        base.enter_text(poco, "com.kuke:id/phoneET", phone)  # 输入手机号
        base.click_to(poco, "com.kuke:id/areaTV")  # 点击所在地区
        poco.swipe([0.5, 0.9], [0.5, 0])
        base.pull_list(poco, area1)  # 选择省级地区
        base.pull_list(poco, area2)  # 选择市级地区
        base.pull_list(poco, area3)  # 选择区级地区
        base.click_to(poco, "com.kuke:id/addressET")  # 输入详细地址
        base.enter_text(poco, "com.kuke:id/addressET", address)  # 输入
        base.click_to(poco, "com.kuke:id/saveBT")  # 点击保存

    # 删除收货地址
    def delete_address(self, poco):
        base.click_to(poco, "com.kuke:id/del_address")  # 点击删除的图标
        base.click_to(poco, "com.kuke:id/ok")  # 点击确认删除

    # 从收货地址返回我的页面
    def address_to_my(self, poco):
        base.click_to(poco, "com.kuke:id/toolbar_back")






