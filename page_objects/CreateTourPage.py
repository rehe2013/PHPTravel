from AdminDashboardPage import AdminDashboardPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CreateTourPage(AdminDashboardPage):
    # Tour management page
    tour_management_loc = (By.XPATH, './/div[@class="panel-heading" and text()="Tours Management"]')
    add_button_loc = (By.CLASS_NAME, 'add_button')
    image_header_loc = (By.XPATH, './/th[text()="Image"]')
    name_header_loc = (By.XPATH, './/th[text()="Name"]')
    stars_header_loc = (By.XPATH, './/th[text()="Stars"]')
    owned_by_header_loc = (By.XPATH, './/th[text()="Owned By"]')
    galley_header_loc = (By.XPATH, './/th[text()="Gallery"]')
    order_header_loc = (By.XPATH, './/th[text()="Order"]')
    status_header_loc = (By.XPATH, './/th[text()="Status"]')

    # element for verifying
    expected_tour_name_loc = \
        (By.XPATH, './/a[@href="http://phptravels.net/admin/tours/manage/Kauai-Couple-Vacation-Package"]')

    # Add tour page
    general_tab_loc = (By.XPATH, './/a[@href="#GENERAL"]')
    inclusions_tab_loc = (By.XPATH, './/a[@href="#INCLUSIONS"]')
    exclusions_tab_loc = (By.XPATH, './/a[@href="#EXCLUSIONS"]')
    meta_info_tab_loc = (By.XPATH, './/a[@href="#META_INFO"]')
    policy_tab_loc = (By.XPATH, './/a[@href="#POLICY"]')
    contact_tab_loc = (By.XPATH, './/a[@href="#CONTACT"]')
    translate_tab_loc = (By.XPATH, './/a[@href="#TRANSLATE"]')
    tour_name_loc = (By.NAME, 'tourname')
    tour_desc_loc = (By.XPATH, './/div[@id="cke_1_contents"]')
    adult_quantity_loc = (By.NAME, 'maxadult')
    adult_price_loc = (By.NAME, 'adultprice')
    adult_btn_loc = (By.ID, 'adultbtn')
    stars_selector_loc = (By.NAME, 'tourstars')
    tour_days_loc = (By.NAME, 'tourdays')
    tour_nights_loc = (By.NAME, 'tournights')
    tour_type_selector_loc = (By.XPATH, './/div[@id="s2id_autogen1"]/a[@class="select2-choice"]')
    tour_type_arrow_loc = (By.XPATH, './/*[@id="s2id_autogen1"]/a/span[2]/b')
    featured_loc = (By.ID, 'isfeatured')
    location1_selector_loc = (By.XPATH, './/div[@id="s2id_autogen3"]/a[@class="select2-choice"]')
    location1_arrow_loc = (By.XPATH, './/div[@id="s2id_autogen3"]/a/span[@class="select2-arrow"]')
    location1_selection_loc = (By.XPATH, './/*[@id="select2-drop"]/ul/li[2]/div')
    map_address_loc = (By.ID, 'mapaddress')
    first_address_loc = (By.XPATH, 'html/body/div[5]/div[1]')
    tour_submit_loc = (By.ID, 'add')

    type_search_loc = (By.XPATH, './/*[@id="select2-drop"]/div[@class="select2-search"]/input')

    # element for verifying
    alert_msg_loc = (By.XPATH, './/*[@class="output"]/div[starts-with(@class, "alert")]')


    def verifyToursManagementElements(self):
        flag = True
        flag = flag and self.find_element(*self.tour_management_loc).is_displayed()
        flag = flag and self.find_element(*self.add_button_loc).is_displayed()
        flag = flag and self.find_element(*self.image_header_loc).is_displayed()
        flag = flag and self.find_element(*self.name_header_loc).is_displayed()
        flag = flag and self.find_element(*self.stars_header_loc).is_displayed()
        flag = flag and self.find_element(*self.owned_by_header_loc).is_displayed()
        flag = flag and self.find_element(*self.galley_header_loc).is_displayed()
        flag = flag and self.find_element(*self.order_header_loc).is_displayed()
        flag = flag and self.find_element(*self.status_header_loc).is_displayed()

        return flag


    def verifyAddTourElements(self):
        flag = True
        flag = flag and self.find_element(*self.general_tab_loc).is_displayed()
        flag = flag and self.find_element(*self.inclusions_tab_loc).is_displayed()
        flag = flag and self.find_element(*self.exclusions_tab_loc).is_displayed()
        flag = flag and self.find_element(*self.meta_info_tab_loc).is_displayed()
        flag = flag and self.find_element(*self.policy_tab_loc).is_displayed()
        flag = flag and self.find_element(*self.contact_tab_loc).is_displayed()
        flag = flag and self.find_element(*self.tour_name_loc).is_displayed()
        flag = flag and self.find_element(*self.tour_desc_loc).is_displayed()
        flag = flag and self.find_element(*self.adult_price_loc).is_displayed()
        flag = flag and self.find_element(*self.adult_btn_loc).is_displayed()
        flag = flag and self.find_element(*self.stars_selector_loc).is_displayed()
        flag = flag and self.find_element(*self.tour_days_loc).is_displayed()
        flag = flag and self.find_element(*self.tour_nights_loc).is_displayed()
        flag = flag and self.find_element(*self.tour_type_selector_loc).is_displayed()
        flag = flag and self.find_element(*self.featured_loc).is_displayed()
        flag = flag and self.find_element(*self.location1_selector_loc).is_displayed()
        flag = flag and self.find_element(*self.map_address_loc).is_displayed()
        flag = flag and self.find_element(*self.tour_submit_loc).is_displayed()
        return flag


    def clickToAddTour(self):
        self.find_element(*self.add_button_loc).click()


    def fillTourCreationPage(self, tour_name, tour_type, adult_quantity, adult_price, map_address_text):
        self.find_element(*self.tour_name_loc).send_keys(tour_name)
        self.find_element(*self.adult_quantity_loc).send_keys(adult_quantity)
        self.find_element(*self.adult_price_loc).send_keys(adult_price)
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.find_element(*self.tour_type_arrow_loc).click()

        try:
            self.explicit_wait(10).until(EC.element_to_be_clickable(self.type_search_loc))
            self.find_element(*self.type_search_loc).send_keys(tour_type)
            self.find_element(*self.type_search_loc).send_keys(Keys.RETURN)
        except TimeoutException:
            print "Element type_search_loc NOT visible"
            return False

        self.find_element(*self.location1_arrow_loc).click()
        try:
            self.explicit_wait(10).until(EC.element_to_be_clickable(self.location1_selection_loc))
            self.find_element(*self.location1_selection_loc).click()
        except TimeoutException:
            print "Element location1_selection_loc NOT visible"
            return False

        self.find_element(*self.tour_submit_loc).click()
        return True


    def submitBlankForm(self):
        self.find_element(*self.tour_submit_loc).click()


    # verify alert messages after submtting a blank form
    def verifyAlert(self):
        return self.find_element(*self.alert_msg_loc).is_displayed()


    def verifyTourAdded(self, tour_name):
        flag = self.find_element(*self.expected_tour_name_loc).is_displayed()
        tour_name_cell_text = None
        if flag == True:
            tour_name_cell_text = self.find_element(*self.expected_tour_name_loc).text
        return tour_name_cell_text


