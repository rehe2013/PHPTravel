from AdminDashboardPage import AdminDashboardPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CreateCustomerPage(AdminDashboardPage):
    # customer management
    customer_management_loc = (By.XPATH, './/div[@class="panel-heading" and text()="Customers Management"]')
    add_button_loc = (By.CLASS_NAME, 'add_button')
    fname_header_loc = (By.XPATH, './/th[text()="First Name"]')
    lname_header_loc = (By.XPATH, './/th[text()="Last Name"]')
    email_header_loc = (By.XPATH, './/th[text()="Email"]')
    active_header_loc = (By.XPATH, './/th[text()="Active"]')
    last_login_header_loc = (By.XPATH, './/th[text()="Last Login"]')
    expected_email_cell_loc = (By.XPATH, './/a[@href="mailto:bdylan@gmail.com"]')

    # Create a new cusmtoer form
    firstname_loc = (By.NAME, 'fname')
    lastname_loc = (By.NAME, 'lname')
    email_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    mobile_loc = (By.NAME, 'mobile')
    country_loc = (By.XPATH, './/a[@class="select2-choice"]')
    country_arrow_loc = (By.XPATH, './/span[@class="select2-arrow"]')
    country_search_loc = (By.XPATH, './/div[@class="select2-search"]/input')
    address1_loc = (By.NAME, 'address1')
    address2_loc = (By.NAME, 'address2')
    status_loc = (By.NAME, 'status')
    newssub_loc = (By.NAME, 'newssub')
    submit_loc = (By.XPATH, './/button[contains(text(), "Submit")]')

    # alert message to verify
    alert_msg_loc = (By.XPATH, './/div[starts-with(@class, "alert")]')


    def verifyCustomerManagemtnElements(self):
        # customer management
        flag = True
        flag = flag and self.find_element(*self.customer_management_loc).is_displayed()
        flag = flag and self.find_element(*self.add_button_loc).is_displayed()
        flag = flag and self.find_element(*self.fname_header_loc).is_displayed()
        flag = flag and self.find_element(*self.lname_header_loc).is_displayed()
        flag = flag and self.find_element(*self.email_header_loc).is_displayed()
        flag = flag and self.find_element(*self.active_header_loc).is_displayed()
        flag = flag and self.find_element(*self.last_login_header_loc).is_displayed()

        return flag


    def clickToAddCustomer(self):
        self.find_element(*self.add_button_loc).click()


    def verifyCreateCustomerFormElements(self):
        #  create customer form
        flag = True
        flag = flag and self.find_element(*self.firstname_loc).is_displayed()
        flag = flag and self.find_element(*self.lastname_loc).is_displayed()
        flag = flag and self.find_element(*self.email_loc).is_displayed()
        flag = flag and self.find_element(*self.email_loc).is_displayed()
        flag = flag and self.find_element(*self.country_loc).is_displayed()
        flag = flag and self.find_element(*self.country_arrow_loc).is_displayed()
        flag = flag and self.find_element(*self.address1_loc).is_displayed()
        flag = flag and self.find_element(*self.address2_loc).is_displayed()
        flag = flag and self.find_element(*self.status_loc).is_displayed()
        flag = flag and self.find_element(*self.newssub_loc).is_displayed()
        flag = flag and self.find_element(*self.submit_loc).is_displayed()

        return flag


    def fillCustomerForm(self, firstname, lastname, email, password, mobile, country, address1, address2):
        self.find_element(*self.firstname_loc).send_keys(firstname)
        self.find_element(*self.lastname_loc).send_keys(lastname)
        self.find_element(*self.email_loc).send_keys(email)
        self.find_element(*self.password_loc).send_keys(password)
        self.find_element(*self.mobile_loc).send_keys(mobile)
        self.find_element(*self.address1_loc).send_keys(address1)
        self.find_element(*self.address2_loc).send_keys(address2)
        self.find_element(*self.country_arrow_loc).click()
        self.find_element(*self.country_search_loc).send_keys(country)
        self.find_element(*self.country_search_loc).send_keys(Keys.RETURN)
        self.find_element(*self.newsletter_loc).click()
        self.find_element(*self.submit_loc).click()


    def verifyCustomerAdded(self, email):
        flag = self.find_element(*self.expected_email_cell_loc).is_displayed()
        email_cell_text = None
        if (flag == True):
            email_cell_text = self.find_element(*self.expected_email_cell_loc).text
        return email_cell_text


    def submitBlankForm(self):
        self.find_element(*self.submit_loc).click()


    # verify alert messages after submtting a blank form
    def verifyAlert(self):
        return self.find_element(*self.alert_msg_loc).is_displayed()

