from page.common.Basepage import BasePage


class Login(BasePage):

    def inputAccout(self):
        el = 'xpath=>//input[@name="loginKey"]'
        self.d.type(el, '001890000123')

    def inputPasswd(self,):
        el = 'xpath=>//input[@name="password"]'
        self.d.type(el, '1qaz@WSX')

    def clickLogin(self):
        el = 'xpath=>//button[text()="Log in"]'
        self.d.double_click(el)


if __name__ == '__main__':
    page = Login()
    page.maxwindow()
    page.open()
    page.inputAccout()
    page.inputPasswd()
    page.d.wait(6)
    page.clickLogin()
