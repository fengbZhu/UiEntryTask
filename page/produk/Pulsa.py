import time

from page.common.login import Login


class Pulsa(Login):
    def clickMasuk(self):
        el = 'xpath=>//a[text()="Masuk"]'
        self.d.click(el)

    def clickPulsa(self):
        el = 'xpath=>//span[text()="Pulsa"]'
        self.d.element_wait(el, 10)
        self.d.click(el)

    def inputTelepon(self, telepon):
        el = 'xpath=>//input[@type="tel"]'
        self.d.type(el, telepon)

    def selectValue(self, value):
        el = 'xpath=>//p[text()="%s"]' % value
        self.d.click(el)

    def totalSelValue(self):
        el = 'css=>.dcRJ7yRnMm_kQcOvgAYE3'
        self.d.element_wait(el)

    def clickBeliSekarang(self):
        el = 'xpath=>//button[text()="Beli Sekarang"]'
        self.d.click(el)

    def checkNomorTeleponSalah(self,name):
        el = 'xpath=>//p[text()="Mohon masukkan nomor telepon yang sah!"]'
        return self.d.wait_and_save_exception(el, name)

    def check11Telepon(self,name):
        el = 'xpath=>//p[text()="Mohon masukkan setidaknya 11 angka11"]'
        return self.d.wait_and_save_exception(el, name)


if __name__ == '__main__':
    page = Pulsa()
    page.maxwindow()
    page.open()
    page.clickMasuk()
    page.inputAccout()
    page.inputPasswd()
    time.sleep(1)
    page.clickLogin()
    page.clickPulsa()
    page.inputTelepon('081274732481')
    page.selectValue(200)
    page.totalSelValue()
    page.clickBeliSekarang()
