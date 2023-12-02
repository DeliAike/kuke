
class Base_file():

    # 封装点击功能  -- poco 对象   -- element 定位的元素
    def click_to(self, poco, element):
        poco(element).click()

    # 封装输入功能
    def enter_text(self, poco, element, text):
        poco(element).set_text(text)

    # 下拉列表地区选择框 --> 三级
    def pull_list(self, poco, area):
        poco(text=area).click()

    # 移动页面
    def move_page(self, poco, x_axis, y_axix):
        poco("android.view.View").swipe([x_axis, y_axix])


