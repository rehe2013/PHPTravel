from Base_Page_Object import Page
from selenium.webdriver.common.by import By

class UseAccountPage(Page):
    booking_loc = (By.XPATH, './/a[@href="#bookings"]')
    myprofile_loc = (By.XPATH, './/a[@href="#profile"]')
    wishlist_loc = (By.XPATH, './/a[@href="#wishlist"]')
    newsletter_loc = (By.XPATH, './a[@href="#newsletter"]')
    greeting_loc = (By.CLASS_NAME, 'RTL')

    logo_loc = (By.CLASS_NAME, 'logo')
    flights_loc = (By.LINK_TEXT, 'Flights')
    tours_loc = (By.LINK_TEXT, 'Tours')
    cars_loc = (By.LINK_TEXT, 'Offers')
    blog_loc = (By.LINK_TEXT, 'Blog')
    hotels_loc = (By.LINK_TEXT, 'Hotels')


    def selectToBookTour(self):
        self.find_element(*self.booking_loc).click()
        self.find_element(*self.tours_loc).click()


    def verifyElements(self):
        flag = True
        flag = flag and self.find_element(*self.booking_loc).is_displayed()
        flag = flag and self.find_element(*self.myprofile_loc).is_displayed()
        flag = flag and self.find_element(*self.wishlist_loc).is_displayed()
        flag = flag and self.find_element(*self.newsletter_loc).is_displayed()
        flag = flag and self.find_element(*self.greeting_loc).is_displayed()
        return flag

