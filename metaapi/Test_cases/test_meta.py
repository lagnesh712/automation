from Pageobject.login import Login

class Test_login:

    def test_01(self,setup):
        self.driver = setup
        self.uilogin = Login(self.driver)
        self.uilogin.login()