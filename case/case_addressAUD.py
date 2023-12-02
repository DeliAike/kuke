# -*- encoding=utf8 -*-
__author__ = "Jian"

import pytest
from airtest.core.api import auto_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from base.base_login import Base_file
from page.address_page import AddressPage
from page.index import IndexPage
from page.login_page import LoginPage
from page.my_page import MyPage
from tools.read_data_login import login_data, list_login
from tools.read_logindata_xlsx import list_login_xlsx

# 实例化page包的对象
address_page = AddressPage()

class TestAddressAUD():

    # 新增修改删除 收货地址
    @pytest.mark.parametrize('name, phone, area1, area2, area3, address',
                             [('测试01', '18348443861', '河南省', '郑州市', '中牟县', 'test1111')])
    def test_add_address(self, logined, name, phone, area1, area2, area3, address):
        # 到‘收货地址’页面
        address_page.to_address(logined)
        # 新增收货地址
        address_page.add_address(logined, name, phone, area1, area2, area3, address)
        # 收货地址页面 --> 我的页面
        address_page.address_to_my(logined)

    @pytest.mark.parametrize('name, phone, area1, area2, area3, address',
                                 [('测试02', '18348443861', '河南省', '郑州市', '中牟县', 'test2222')])
    def test_update_address(self, logined, name, phone, area1, area2, area3, address):
        # 到‘收货地址’页面
        address_page.to_address(logined)
        # 修改收货地址
        address_page.update_address(logined, name, phone, area1, area2, area3, address)
        # 收货地址页面 --> 我的页面
        address_page.address_to_my(logined)

    def test_delete_address(self, logined):
        # 到‘收货地址’页面
        address_page.to_address(logined)
        # 删除收货地址
        address_page.delete_address(logined)
        # 收货地址页面 --> 我的页面
        address_page.address_to_my(logined)