from lib.pyse import Pyse


class BasePage(object):
    def __init__(self):
        self.d = Pyse('chrome')

    def open(self):   #登录地址
        self.d.open('https://uat.shopee.co.id/produk-digital/pulsa/26?dp_from_source=36')

    def quit(self):      #退出
        self.d.quit()

    def close(self):     #关闭
        self.d.close()

    def maxwindow(self):
        self.d.max_window()

    @property
    def driver(self):
        return self.d.driver

if __name__ == '__main__':          #调试
    page = BasePage()       #实例化类
    page.open()
