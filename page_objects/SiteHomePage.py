from Base_Page_Object import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# For PHPTravels Homepage
class SiteHomePage(Page):
    url = 'http://phptravels.net/'
    carousel_loc = (By.ID, 'Carousel')
    currency_loc = (By.ID, 'currency')
    languages_loc = (By.XPATH, './/a[contains(text(), "English") and @data-toggle="dropdown"]')
    myaccout_loc = (By.XPATH, './/a[contains(text(), "My Account")]')
    login_item_loc = (By.XPATH, './/a[@href="http://phptravels.net/login"]')

    logo_loc = (By.CLASS_NAME, 'logo')
    flights_loc = (By.LINK_TEXT, 'Flights')
    tours_loc = (By.LINK_TEXT, 'Tours')
    cars_loc = (By.LINK_TEXT, 'Offers')
    blog_loc = (By.LINK_TEXT, 'Blog')
    hotels_loc = (By.LINK_TEXT, 'Hotels')


    def verifySitePageElements(self):
        flag = True
        flag = flag and self.find_element(*self.carousel_loc).is_displayed()
        flag = flag and self.find_element(*self.currency_loc).is_displayed()
        flag = flag and self.find_element(*self.languages_loc).is_displayed()
        flag = flag and self.find_element(*self.myaccout_loc).is_displayed()
        flag = flag and self.find_element(*self.logo_loc).is_displayed()
        flag = flag and self.find_element(*self.flights_loc).is_displayed()
        flag = flag and self.find_element(*self.tours_loc).is_displayed()
        flag = flag and self.find_element(*self.cars_loc).is_displayed()
        flag = flag and self.find_element(*self.blog_loc).is_displayed()
        flag = flag and self.find_element(*self.hotels_loc).is_displayed()
        return flag


    def clickLoginItem(self):
        self.find_element(*self.myaccout_loc).click()
        try:
            self.find_element(*self.login_item_loc).click()
        except NoSuchElementException:
            print "LoginPage:clickLoginItem() - Login Item not found!"

