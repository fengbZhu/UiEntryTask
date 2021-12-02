import time
import unittest

from page.produk.Pulsa import Pulsa


class CheckPhone(unittest.TestCase):

    def setUp(self):
        self.page = Pulsa()
        self.page.maxwindow()
        self.page.open()
        self.page.clickMasuk()
        self.page.inputAccout()
        self.page.inputPasswd()
        time.sleep(1)
        self.page.clickLogin()
        self.page.clickPulsa()

    def tearDown(self):
        self.page.quit()

    def test_01_NomorTeleponSalah(self):
        self.page.inputTelepon('0732481')
        self.assertTrue(self.page.checkNomorTeleponSalah(self.test_01_NomorTeleponSalah.__name__), 'msg')

    def test_02_11Telepon(self):
        # self.page.inputTelepon('0732481')
        self.page.inputTelepon('0812747311')
        self.assertTrue(self.page.check11Telepon(self.test_02_11Telepon.__name__), 'msg')



if __name__ == '__main__':
    unittest.main()