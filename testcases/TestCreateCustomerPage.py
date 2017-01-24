import unittest
from selenium import webdriver
from page_objects import LoginPage
from page_objects import AdminDashboardPage
from page_objects import CreateCustomerPage

class TestCreateCustomerPage(unittest.TestCase):
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


    def testCreateCustomer(self):
        admin_url = "admin"
        customer_mgmnt_url = "admin/accounts/customers"
        add_customer_url = "admin/accounts/customers/add"
        dashboard_expected_title = "Dashboard"
        customer_mngnt_expected_title = "Customers Management"
        add_customer_expected_title = "Add Customer"

        # open admin dashboard page
        dashboard_page = AdminDashboardPage.AdminDashboardPage(self.driver)
        dashboard_page.open(admin_url)
        page_title = dashboard_page.get_title()
        self.assertIn(dashboard_expected_title, page_title)

        #self.driver.implicitly_wait(10)
        flag = dashboard_page.verifyDashboardElements()
        self.assertTrue(flag)

        # open customer management page
        dashboard_page.clickAccountCustomer()
        create_customer_page = CreateCustomerPage.CreateCustomerPage(self.driver)
        create_customer_page.open(customer_mgmnt_url)
        page_title = create_customer_page.get_title()
        self.assertIn(customer_mngnt_expected_title, page_title)

        #self.driver.implicitly_wait(10)
        flag = create_customer_page.verifyCustomerManagemtnElements()

        # open add customer page
        create_customer_page.clickToAddCustomer()
        create_customer_page.open(add_customer_url)
        page_title = create_customer_page.get_title()
        self.assertIn(add_customer_expected_title, page_title)
        flag = create_customer_page.verifyCreateCustomerFormElements()
        self.assertTrue(flag)

        # fill form to add a customer
        email_addr = "bdylan@gmail.com"
        password = "password"
        create_customer_page.fillCustomerForm\
            ("Bob", "Dylan", email_addr, password, "408-777-8888", \
             "United States", "12345 Homestead Rd", "Sunnyvale, CA 94087")

        create_customer_page.open(customer_mgmnt_url)
        self.driver.implicitly_wait(10)
        result_email = create_customer_page.verifyCustomerAdded(email_addr)
        self.assertEqual(result_email, email_addr)
        print result_email

    def testSubmitBlank(self):
        admin_url = "admin"
        customer_mgmnt_url = "admin/accounts/customers"
        add_customer_url = "admin/accounts/customers/add"
        dashboard_expected_title = "Dashboard"
        customer_mngnt_expected_title = "Customers Management"
        add_customer_expected_title = "Add Customer"

        # open admin dashboard page
        dashboard_page = AdminDashboardPage.AdminDashboardPage(self.driver)
        dashboard_page.open(admin_url)
        page_title = dashboard_page.get_title()
        print page_title
        self.assertIn(dashboard_expected_title, page_title)

        self.driver.implicitly_wait(10)
        flag = dashboard_page.verifyDashboardElements()
        self.assertTrue(flag)

        # open customer management page
        dashboard_page.clickAccountCustomer()
        create_customer_page = CreateCustomerPage.CreateCustomerPage(self.driver)
        create_customer_page.open(customer_mgmnt_url)
        page_title = create_customer_page.get_title()
        self.assertIn(customer_mngnt_expected_title, page_title)

        self.driver.implicitly_wait(10)
        flag = create_customer_page.verifyCustomerManagemtnElements()

        # open add customer page
        create_customer_page.clickToAddCustomer()
        create_customer_page.open(add_customer_url)
        page_title = create_customer_page.get_title()
        self.assertIn(add_customer_expected_title, page_title)
        flag = create_customer_page.verifyCreateCustomerFormElements()
        self.assertTrue(flag)

        create_customer_page.submitBlankForm()
        flag = create_customer_page.verifyAlert()
        self.assertTrue(flag)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__=="__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase (TestCreateCustomerPage)
    unittest.TextTestRunner(verbosity=2).run(suite)
