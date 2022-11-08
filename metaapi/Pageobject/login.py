from Utilities.commonutils import Uimethod

class Login:
    login_id="email"
    password_id="pass"
    submit_id="u_0_d_fL"
    number="8962156766"

    def __init__(self,setup):
        self.driver=setup
        self.click = Uimethod()

    def login(self):
        self.click.send_key_id(self.login_id,self.number)
        self.click.send_key_id(self.password_id,"jaibarfani07")
        self.click.click_by_id(self.submit_id)



