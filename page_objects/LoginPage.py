from selenium.webdriver.common.by import By
from Base_Page_Object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(Page):
    email_loc = (By.NAME, 'username')
    pass_loc = (By.NAME, 'password')
    submit_loc = (By.XPATH, './/button[@type="submit"]')
    alert_msg_loc = (By.XPATH, './/div[starts-with(@class, "alert")]')

    """
    def __init__(self):
        Page.__init__(self, selenium_driver, base_url="http://phptravels.net/")
        self.url = "admin"
    """

    def openpage(self):
        self.open(self.url)

    def verifyPageElements(self):
        flag = True
        flag = flag and self.find_element(*self.email_loc).is_displayed()
        flag = flag and self.find_element(*self.pass_loc).is_displayed()
        flag = flag and self.find_element(*self.submit_loc).is_displayed()
        return flag


    def setEmail(self, admin, email):
        if (admin == True):
            self.email_loc = (By.NAME, 'email')
        self.find_element(*self.email_loc).send_keys(email)


    def setPassword(self, password):
        self.find_element(*self.pass_loc).send_keys(password)


    def submit(self):
        self.find_element(*self.submit_loc).click()

    # verify alert messages after submtting a blank form
    def verifyAlert(self):
        return self.find_element(*self.alert_msg_loc).is_displayed()