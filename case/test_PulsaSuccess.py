import os
import random
import time
import unittest

from lib.tool import tool
from page.produk.checkout import Checkout


class CheckPhone(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.page = Checkout()
        cls.page.maxwindow()
        cls.page.open()
        cls.page.clickMasuk()
        cls.page.inputAccout()
        cls.page.inputPasswd()
        time.sleep(1)
        cls.page.clickLogin()
        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.page.quit()

    def test_01_PulsaSuccess(self):
        num = random.randint(10000, 99999)
        phone = '0811231' + str(num)
        self.page.inputTelepon(phone)
        self.page.selectValue(200)
        self.page.totalSelValue()
        time.sleep(0.5)
        self.page.clickBeliSekarang()
        time.sleep(3)
        self.page.clickMetode()
        self.page.selectTransferBank()
        time.sleep(1)
        self.page.selectankLainnya()
        self.page.clickKonfirmasi()
        self.page.clickBayarSekarang()
        time.sleep(3)
        self.src_big = self.page.getTargetImg()
        self.src_small = self.page.getImg()
        self.target = tool.save_picture(src=self.src_big, name='src_big.jpg')
        self.template = tool.save_picture(src=self.src_small, name='src_small.jpg')
        self.distance = tool.findpic(target=self.target, template=self.template)
        self.page.d.move_by_distance('xpath=>//aside/div/div/div/div[2]/div[2]/div[3]', self.distance)
        time.sleep(2)

        # self.assertTrue(self.page.check11Telepon(self.test_02_11Telepon.__name__), 'msg')


if __name__ == '__main__':
    unittest.main()
