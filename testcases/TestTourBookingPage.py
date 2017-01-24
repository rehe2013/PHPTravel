import unittest
from selenium import webdriver
from page_objects import LoginPage
from page_objects import TourBookingPage
from page_objects import UserAccountPage


class TestTourBookingPage(unittest.TestCase):
    def setUp(self):
        login_url = "login"
        email = "user@phptravels.com"
        password = "demouser"

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        login_page = LoginPage.LoginPage(self.driver)
        login_page.open(login_url)
        login_page.setEmail(False, email)
        login_page.setPassword(password)
        login_page.submit()
        self.driver.implicitly_wait(20)


    def testTourBooking(self):
        base_url = 'http://phptravels.net/'
        account_url = "account"
        tours_url = "tours"
        expected_title = "Tours Listings"
        expected_email = "user@phptravels.com"

        user_account_page = UserAccountPage.UseAccountPage(self.driver)
        user_account_page.open(account_url)
        #self.driver.implicitly_wait(5)
        user_account_page.selectToBookTour()

        # verify page title and tour listing page elements
        tour_booking_page = TourBookingPage.TourBookingPage(self.driver)
        tour_booking_page.open(tours_url)
        page_title = tour_booking_page.get_title()
        flag = tour_booking_page.verifyTourListingsElements()
        self.assertTrue(flag)

        # select details button to browser a tour's detail info
        tour_booking_page.clickDetails()
        flag = tour_booking_page.verifyTourElements()
        self.assertTrue(flag)

        # enter desired date
        expected_date = "23/01/2017"
        tour_booking_page.selectDate(expected_date)

        # click submit to book a tour
        tour_booking_page.clickBookingTour()
        self.driver.implicitly_wait(10)
        tour_booking_page.verifySummaryElements()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase (TestTourBookingPage)
    unittest.TextTestRunner(verbosity=2).run(suite)