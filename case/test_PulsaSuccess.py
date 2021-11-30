import os
import random
import time
import unittest

from conf.setting import WEBPICTUREPATH
from lib.tool import Tool
from page.produk.Pulsa import Pulsa
from page.produk.checkout import Checkout


class CheckPhone(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.page = Pulsa()
        cls.page.maxwindow()
        cls.page.open()
        cls.page.clickMasuk()
        cls.page.inputAccout()
        cls.page.inputPasswd()
        time.sleep(1)
        cls.page.clickLogin()
        cls.page.clickPulsa()

    @classmethod
    def tearDown(cls):
        cls.page.quit()


    def test_01_PulsaSuccess(self):
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
        time.sleep(1)
        page.clickBeliSekarang()
        page.clickMetode()
        page.selectTransferBank()
        time.sleep(4)
        page.selectankLainnya()
        page.clickKonfirmasi()
        page.clickBayarSekarang()
        time.sleep(5)


        # self.assertTrue(self.page.check11Telepon(self.test_02_11Telepon.__name__), 'msg')



if __name__ == '__main__':
    unittest.main()