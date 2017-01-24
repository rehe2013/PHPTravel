from Base_Page_Object import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TourBookingPage (Page):
    # Tour listings page
    location_search_loc = (By.NAME, 'txtSearch')
    calendar_loc = (By.NAME, 'date')
    adult_num__select_loc = (By.ID, 'adults')
    tour_type_select_loc = (By.ID, 'tourtype')
    search_loc = (By.XPATH, './/button[contains(text(), "Search")]')
    first_details_loc = (By.XPATH, '(.//a/button[contains(text(), "Details")])[1]')

    # single tour page
    booking_submit_loc = (By.XPATH, './/button[@type="submit" and text()="Book Now"]')
    view_map_loc = (By.XPATH, './/a[@href="#collapseMap"]')
    booking_options_loc = (By.XPATH, './/span[text()="Booking Options"]')
    date_input_loc = (By.XPATH, './/input[@name="date" and @placeholder="Search"]')
    month_feb_loc = (By.XPATH, './/span[text()="Feb"]')
    change_date_loc = (By.XPATH, './/button[@type="submit" and text()= "Change Date"]')
    checkin_date_loc = (By.XPATH, './/div[@id="tchkin"]/div/input[@name="date"]')
    total_cost_loc = (By.CLASS_NAME, 'totalCost')

    # Booking summary page
    booking_summary_loc = (By.XPATH, './/span[text() = "Booking Summary"]')
    firstname_loc = (By.XPATH, './/input[@class="form-control" and @value="John"]')
    lastname_loc = (By.XPATH, './/input[@class="form-control" and @value="Smith"]')
    email_loc = (By.XPATH, './/input[@class="form-control" and @value="user@phptravels.com"]')
    checkin_date2_loc = (By.XPATH, './/div[@class="booking-deposit"]/following-sibling::table/tbody/tr[2]/td[2]')


    def clickDetails(self):
        self.find_element(*self.first_details_loc).click()


    def verifyTourListingsElements(self):
        expected_title = "Tour Listings"
        flag = True
        flag = flag and self.find_element(*self.location_search_loc).is_displayed()
        flag = flag and self.find_element(*self.calendar_loc).is_displayed()
        flag = flag and self.find_element(*self.adult_num__select_loc).is_displayed()
        flag = flag and self.find_element(*self.tour_type_select_loc).is_displayed()
        flag = flag and self.find_element(*self.search_loc).is_displayed()

        return flag


    def selectDate(self, desired_date):
        self.find_element(*self.date_input_loc).clear()
        self.find_element(*self.date_input_loc).send_keys(desired_date)
        self.find_element(*self.change_date_loc).click()
        self.find_element(*self.month_feb_loc).click()

    def clickBookingTour(self):
        self.find_element(*self.booking_submit_loc).click()


    def verifyTourElements(self):
        flag = True
        flag = flag and self.find_element(*self.view_map_loc).is_displayed()
        flag = flag and self.find_element(*self.booking_submit_loc).is_displayed()
        flag = flag and self.find_element(*self.total_cost_loc).is_displayed()
        flag = flag and self.find_element(*self.booking_options_loc).is_displayed()
        return flag


    def verifySummaryElements(self):
        flag = True
        flag = flag and self.find_element(*self.booking_summary_loc).is_displayed()
        flag = flag and self.find_element(*self.firstname_loc).is_displayed()
        flag = flag and self.find_element(*self.lastname_loc).is_displayed()
        flag = flag and self.find_element(*self.email_loc).is_displayed()
        return flag






