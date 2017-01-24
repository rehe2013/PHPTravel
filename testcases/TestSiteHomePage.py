import unittest
from selenium import webdriver
from page_objects import SiteHomePage
from page_objects import LoginPage


class TestSiteHomePage(unittest.TestCase):
    base_url = 'http://phptravels.net/'
    sitehome_page = None
    login_page = None

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # verify elements on homepage
    def testVerifySitePageElements(self):
        expected_title = "PHPTRAVELS | Travel Technology Partner"
        self.sitehome_page = SiteHomePage.SiteHomePage(self.driver)
        self.sitehome_page.open("")
        page_title = self.sitehome_page.get_title()
        self.assertIn(expected_title, page_title)
        result = self.sitehome_page.verifySitePageElements()
        self.assertTrue(result)


    # verify login items are available and working
    def testClickLoginItem(self):
        expected_title = "Login"
        page_url = "login"
        self.sitehome_page = SiteHomePage.SiteHomePage(self.driver)
        self.sitehome_page.open("")
        self.sitehome_page.clickLoginItem()
        self.login_page = LoginPage.LoginPage(self.driver, self.base_url)
        self.login_page.open(page_url)
        self.driver.implicitly_wait(10)
        page_title = self.login_page.get_title()
        self.assertIn(expected_title, page_title)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSiteHomePage)
    unittest.TextTestRunner(verbosity=2).run(suite)