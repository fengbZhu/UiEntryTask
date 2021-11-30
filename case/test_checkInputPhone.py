import time
import unittest

from page.produk.Pulsa import Pulsa


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

        pass
    def test_01_NomorTeleponSalah(self):
        self.page.inputTelepon('0732481')
        self.assertTrue(self.page.checkNomorTeleponSalah(self.test_01_NomorTeleponSalah.__name__), 'msg')

    def test_02_11Telepon(self):
        # self.page.inputTelepon('0732481')
        self.page.inputTelepon('0812747311')
        self.assertTrue(self.page.check11Telepon(self.test_02_11Telepon.__name__), 'msg')

    def test_02_PulsaSuccess(self):
        # self.page.inputTelepon('0732481')
        self.page.inputTelepon('0812747311')
        self.assertTrue(self.page.check11Telepon(self.test_02_11Telepon.__name__), 'msg')



if __name__ == '__main__':
    unittest.main()