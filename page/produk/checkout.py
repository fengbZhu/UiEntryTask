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
    src_big = page.d.get_attribute('xpath=>//div[text()="Verifikasi"]/../../div[2]/div/div/img', attribute='src')
    src_small = page.d.get_attribute('xpath=>//div[text()="Verifikasi"]/../../div[2]/*/img', attribute='src')
    tool.save_picture(src=src_big, name='beijingtu.jpg')
    tool.save_picture(src=src_small, name='huakuai.jpg')
    target = WEBPICTUREPATH + os.path.sep + 'beijingtu.jpg'
    template = WEBPICTUREPATH + os.path.sep + 'huakuai.jpg'
    distance = tool.findpic(target=target, template=template)
    print(distance)
    page.d.move_by_distance('xpath=>//aside/div/div/div/div[2]/div[2]/div[3]', distance)
    time.sleep(2)
    page.d.F5()

    # page.d.quit()
