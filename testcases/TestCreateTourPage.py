import unittest
from selenium import webdriver
from page_objects import LoginPage
from page_objects import AdminDashboardPage
from page_objects import CreateTourPage

class TestCreateTourPage(unittest.TestCase):
    def setUp(self):
        base_url = 'http://phptravels.net/'
        admin_url ="admin"
        email = "admin@phptravels.com"
        password = "demoadmin"
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

        login_page = LoginPage.LoginPage(self.driver)
        login_page.open(admin_url)
        login_page.setEmail(True, email)
        login_page.setPassword(password)
        login_page.submit()
        self.driver.implicitly_wait(20)


    def testCreateTour(self):
        admin_url = "admin"
        tour_mgmnt_url = "admin/tours"
        add_tour_url = "admin/tours/add"
        dashboard_expected_title = "Dashboard"
        tour_mngnt_expected_title = "Tours Management"
        add_tour_expected_title = "Add Tour"

        # open admin dashboard page
        dashboard_page = AdminDashboardPage.AdminDashboardPage(self.driver)
        dashboard_page.open(admin_url)
        page_title = dashboard_page.get_title()
        self.assertIn(dashboard_expected_title, page_title)

        #self.driver.implicitly_wait(10)
        flag = dashboard_page.verifyDashboardElements()
        self.assertTrue(flag)

        # open tour management page
        dashboard_page.clickToursTours()
        create_tour_page = CreateTourPage.CreateTourPage(self.driver)
        create_tour_page.open(tour_mgmnt_url)
        page_title = create_tour_page.get_title()
        self.assertIn(tour_mngnt_expected_title, page_title)

        #self.driver.implicitly_wait(10)
        flag = create_tour_page.verifyToursManagementElements()

        # open add tour page
        create_tour_page.clickToAddTour()
        create_tour_page.open(add_tour_url)
        page_title = create_tour_page.get_title()
        self.assertIn(add_tour_expected_title, page_title)
        flag = create_tour_page.verifyAddTourElements()
        self.assertTrue(flag)

        # fill tour creation page to add a tour
        tour_name = "Kauai Couple Vacation Package"
        tour_type = "Couples"
        adult_number = "2"
        adult_price = "$999.00"
        map_address_text = "Kauai"
        flag = create_tour_page.fillTourCreationPage(tour_name, tour_type, adult_number, adult_price, map_address_text)
        self.assertTrue(flag)
        self.driver.implicitly_wait(10)
        create_tour_page.open(tour_mgmnt_url)
        self.driver.implicitly_wait(10)
        result_name = create_tour_page.verifyTourAdded(tour_name)
        print result_name
        self.assertEqual(result_name, tour_name)

    # verify alert messages after submtting a blank form
    def testSubmitBlankForm(self):
        admin_url = "admin"
        tour_mgmnt_url = "admin/tours"
        add_tour_url = "admin/tours/add"
        dashboard_expected_title = "Dashboard"
        tour_mngnt_expected_title = "Tours Management"
        add_tour_expected_title = "Add Tour"

        # open admin dashboard page
        dashboard_page = AdminDashboardPage.AdminDashboardPage(self.driver)
        dashboard_page.open(admin_url)
        page_title = dashboard_page.get_title()
        self.assertIn(dashboard_expected_title, page_title)

        self.driver.implicitly_wait(10)
        flag = dashboard_page.verifyDashboardElements()
        self.assertTrue(flag)

        # open tour management page
        dashboard_page.clickToursTours()
        create_tour_page = CreateTourPage.CreateTourPage(self.driver)
        create_tour_page.open(tour_mgmnt_url)
        page_title = create_tour_page.get_title()
        self.assertIn(tour_mngnt_expected_title, page_title)

        self.driver.implicitly_wait(10)
        flag = create_tour_page.verifyToursManagementElements()

        # open add tour page
        create_tour_page.clickToAddTour()
        create_tour_page.open(add_tour_url)
        page_title = create_tour_page.get_title()
        self.assertIn(add_tour_expected_title, page_title)
        flag = create_tour_page.verifyAddTourElements()
        self.assertTrue(flag)

        create_tour_page.submitBlankForm()
        flag = create_tour_page.verifyAlert()
        self.assertTrue(flag)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase (TestCreateTourPage)
    unittest.TextTestRunner(verbosity=2).run(suite)