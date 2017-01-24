import unittest
from selenium import webdriver
from page_objects import LoginPage
from page_objects import UserAccountPage


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # happy run test
    def testLogin(self):
        base_url = 'http://phptravels.net/'
        login_expected_title = 'Login'
        login_url = "login"
        account_url = 'account'
        account_expected_title = "My Account"
        email = "user@phptravels.com"
        password = "demouser"

        login_page = LoginPage.LoginPage(self.driver, base_url)
        login_page.open(login_url)
        page_title = login_page.get_title()
        self.assertIn(login_expected_title, page_title)

        flag = login_page.verifyPageElements()
        self.assertTrue(flag)

        login_page.setEmail(False, email)
        login_page.setPassword(password)
        login_page.submit()
        user_account_page = UserAccountPage.UseAccountPage(self.driver, base_url)
        user_account_page.open(account_url)

        page_title = user_account_page.get_title()
        self.assertIn(account_expected_title, page_title)


    # test a blank login
    def testBlankLogin(self):
        base_url = 'http://phptravels.net/'
        login_url = "login"
        login_page = LoginPage.LoginPage(self.driver, base_url)
        login_page.open(login_url)
        login_page.submit()
        flag = login_page.verifyAlert()
        self.assertTrue(flag)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase (TestLoginPage)
    unittest.TextTestRunner(verbosity=2).run(suite)