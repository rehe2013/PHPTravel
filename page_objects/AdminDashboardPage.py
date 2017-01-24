from Base_Page_Object import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException


class AdminDashboardPage(Page):
    expected_title = 'Dashboard'

    # sidebar
    dashboard_loc = (By.CSS_SELECTOR, '.navbar-brand>span')
    side_search_loc = (By.ID, 'sidebar-query')
    accounts_loc = (By.XPATH, './/a[@href="#ACCOUNTS"]')
    customer_item_loc = (By.XPATH, './/a[@href="http://phptravels.net/admin/accounts/customers/"]')
    update_loc = (By.XPATH, './/a[@href="http://phptravels.net/admin/updates/"]')
    general_loc = (By.XPATH, './/a[@href="#menu-ui"]')
    cms_loc = (By.XPATH, './/a[@href="#CMS"]')
    blog_loc = (By.XPATH, './/a[@href="#Blog"]')
    tours_loc = (By.XPATH, './/a[@href="#Tours"]')
    tours_item_loc = (By.XPATH, './/a[@href="http://phptravels.net/admin/tours/"]')
    offer_loc = (By.XPATH, './/a[@href="#SPECIAL_OFFERS"]')
    coupons_loc = (By.XPATH, './/a[@href="http://phptravels.net/admin/coupons/"]')
    locations_loc = (By.XPATH, './/a[@href="http://phptravels.net/admin/locations"]')
    newsletter_loc = (By.XPATH, './/a[@href="http://phptravels.net/admin/newsletter/"]')

    # top buttons
    quick_booking_button_loc = (By.XPATH, './/button[@data-target="#quickbook"]')
    booking_button_loc = (By.XPATH, './/form[@action="http://phptravels.net/admin/bookings/"]')
    cms_button_loc = (By.XPATH, './/form[@action="http://phptravels.net/admin/cms/"]')
    blog_button_loc = (By.XPATH, './/form[@action="http://phptravels.net/admin/blog/"]')
    send_newsletter_button_loc = (By.XPATH, './/form[@action="http://phptravels.net/admin/newsletter/"]')
    backup_db_button_loc = (By.XPATH, './/form[@action="http://phptravels.net/admin/backup/"]')



    def verifyDashboardElements(self):
        # dashboad page
        flag = True
        # sidebar
        flag = flag and self.find_element(*self.dashboard_loc).is_displayed()
        flag = flag and self.find_element(*self.side_search_loc).is_displayed()
        flag = flag and self.find_element(*self.accounts_loc).is_displayed()
        flag = flag and self.find_element(*self.update_loc).is_displayed()
        flag = flag and self.find_element(*self.general_loc).is_displayed()
        flag = flag and self.find_element(*self.cms_loc).is_displayed()
        flag = flag and self.find_element(*self.blog_loc).is_displayed()
        flag = flag and self.find_element(*self.tours_loc).is_displayed()
        flag = flag and self.find_element(*self.offer_loc).is_displayed()
        flag = flag and self.find_element(*self.coupons_loc).is_displayed()
        flag = flag and self.find_element(*self.locations_loc).is_displayed()
        flag = flag and self.find_element(*self.newsletter_loc).is_displayed()

        # top buttons
        flag = flag and self.find_element(*self.quick_booking_button_loc).is_displayed()
        flag = flag and self.find_element(*self.booking_button_loc).is_displayed()
        flag = flag and self.find_element(*self.cms_button_loc).is_displayed()
        flag = flag and self.find_element(*self.blog_button_loc).is_displayed()
        flag = flag and self.find_element(*self.send_newsletter_button_loc).is_displayed()
        flag = flag and self.find_element(*self.backup_db_button_loc).is_displayed()

        return flag


    def clickAccountCustomer(self):
        self.find_element(*self.accounts_loc).click()
        try:
            self.explicit_wait(10).until(EC.element_to_be_clickable(self.customer_item_loc))
            self.find_element(*self.customer_item_loc).click()
        except ElementNotVisibleException:
            print "Element customer_item_loc NOT visible"


    def clickToursTours(self):
        self.find_element(*self.tours_loc).click()
        try:
            self.explicit_wait(10).until(EC.element_to_be_clickable(self.tours_item_loc))
            self.find_element(*self.tours_item_loc).click()
        except ElementNotVisibleException:
            print "Element tours_item_loc NOT visible"








