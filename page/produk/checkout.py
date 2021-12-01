import os
import random
import time

from conf.setting import WEBPICTUREPATH
from lib.tool import Tool, tool
from page.produk.Pulsa import Pulsa


class Checkout(Pulsa):
    def clickMetode(self):
        el = 'xpath=>//span[text()="Metode Pembayaran"]'
        self.d.click(el)

    def selectTransferBank(self):
        el = 'xpath=>//div[text()="Transfer Bank"]'
        self.d.click(el)

    def selectankLainnya(self):
        el = 'xpath=>//span[text()="Menerima transfer dari SeaBank dan bank lainnya"]'
        self.d.click(el)

    def clickKonfirmasi(self):
        el = 'xpath=>//button[text()="KONFIRMASI"]'
        self.d.click(el)

    def clickBayarSekarang(self):
        el = 'xpath=>//div[text()="Bayar Sekarang"]'
        self.d.click(el)

    def verifikasi(self):
        el = 'xpath=>//button[text()="Muat Ulang"]/../div[2]/div[2]/div[3]'
        self.d.click(el)

    def getTargetImg(self):
        el = 'xpath=>//div[text()="Verifikasi"]/../../div[2]/div/div/img'
        return self.d.get_attribute(el, attribute='src')

    def getImg(self):
        el = 'xpath=>//div[text()="Verifikasi"]/../../div[2]/*/img'
        return self.d.get_attribute(el, attribute='src')


if __name__ == '__main__':
    page = Checkout()
    page.maxwindow()
    page.open()
    page.clickMasuk()
    page.inputAccout()
    page.inputPasswd()
    time.sleep(1)
    page.clickLogin()
    time.sleep(2)
    num = random.randint(10000, 99999)
    phone = '0811231' + str(num)
    page.inputTelepon(phone)
    page.selectValue(200)
    page.totalSelValue()
    time.sleep(0.5)
    page.clickBeliSekarang()
    time.sleep(3)
    page.clickMetode()
    page.selectTransferBank()
    time.sleep(1)
    page.selectankLainnya()
    page.clickKonfirmasi()
    page.clickBayarSekarang()
    time.sleep(3)
    src_big = page.getTargetImg()
    src_small = page.getImg()
    target = tool.save_picture(src=src_big, name='src_big.jpg')
    template = tool.save_picture(src=src_small, name='src_small.jpg')
    distance = tool.findpic(target=target, template=template)
    page.d.move_by_distance('xpath=>//aside/div/div/div/div[2]/div[2]/div[3]', distance,times=3)
    time.sleep(2)
    page.d.F5()

    # page.d.quit()
