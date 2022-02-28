class CheckOut():
    def __init__(self,driver) :
        self.driver = driver
        self.first_name_textbox_id = "first-name"
        self.last_name_textbox_id  = "last-name"
        self.postal_code_textbox_id  = "postal-code"
        self.continue_button_id  = "continue"
        self.cancel_button_id  = "cancel"
        self.finish_button_id  = "finish"


    def enter_firstname(self, firstname):
        self.driver.find_element_by_id(self.first_name_textbox_id).clear()
        self.driver.find_element_by_id(self.first_name_textbox_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_id(self.last_name_textbox_id).clear()
        self.driver.find_element_by_id(self.last_name_textbox_id).send_keys(lastname)

    def enter_postal_code(self, postalcode):
        self.driver.find_element_by_id(self.postal_code_textbox_id).clear()
        self.driver.find_element_by_id(self.postal_code_textbox_id).send_keys(postalcode)

    def click_continue(self):
        self.driver.find_element_by_id(self.continue_button_id).click()

    def click_finish(self):
        self.driver.find_element_by_id(self.finish_button_id).click()

    def click_cancel(self):
        self.driver.find_element_by_id(self.cancel_button_id).click()
       
        