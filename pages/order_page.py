from selenium.webdriver.common.by import By
from pages.home_page import HomePage, HomePageLocators
import allure


class OrderPageLocators:
    FIRST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_STATION_LIST = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    RENTAL_START_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_CALENDAR_DATES = (By.XPATH, ".//div[@role='button']")
    RENTAL_PERIOD_AREA = (By.XPATH, ".//div[text()='* Срок аренды']")
    RENTAL_PERIOD_LIST = (By.XPATH, ".//div[@role='option']")
    SCOOTER_BLACK_COLOUR_CHECKBOX = (By.ID, "black")
    SCOOTER_GREY_COLOUR_CHECKBOX = (By.ID, "grey")

    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_STATUS = (By.XPATH, ".//div[text()='Заказ оформлен']")


class OrderPage(HomePage):
    @allure.step('Заполнить форму «Для кого самокат»')
    def fill_for_whom_form(self, first_name, last_name, address, metro_index, phone):
        self.find_element_located(OrderPageLocators.FIRST_NAME_FIELD).send_keys(first_name)
        self.find_element_located(OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.find_element_located(OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        self.choose_metro_station(metro_index)
        self.find_element_located(OrderPageLocators.PHONE_FIELD).send_keys(phone)

    def choose_metro_station(self, index):
        self.find_element_located(OrderPageLocators.METRO_STATION_FIELD).click()
        metro_stations = self.find_visible_elements_located(OrderPageLocators.METRO_STATION_LIST)
        return metro_stations[index].click()

    @allure.step('Кликнуть Далее')
    def click_next(self):
        return self.find_element_located(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполнить форму «Про аредну»')
    def fill_about_rent_form(self, date, rental_period, is_black=False, is_gray=False):
        self.choose_rental_start_date(date)
        self.choose_rental_period(rental_period)
        if is_black:
            self.find_element_located(OrderPageLocators.SCOOTER_BLACK_COLOUR_CHECKBOX).click()
        if is_gray:
            self.find_element_located(OrderPageLocators.SCOOTER_GREY_COLOUR_CHECKBOX).click()

    def choose_rental_start_date(self, date):
        self.find_element_located(OrderPageLocators.RENTAL_START_DATE).click()
        calendar_dates = self.find_visible_elements_located(OrderPageLocators.RENTAL_CALENDAR_DATES)

        for calendar_date in calendar_dates:
            if calendar_date.text == str(date):
                return calendar_date.click()

    def choose_rental_period(self, period):
        self.find_element_located(OrderPageLocators.RENTAL_PERIOD_AREA).click()
        rental_periods = self.find_visible_elements_located(OrderPageLocators.RENTAL_PERIOD_LIST)

        for rental_period in rental_periods:
            if rental_period.text == period:
                return rental_period.click()

    @allure.step('Кликнуть кнопку Заказать')
    def click_create_order_button(self):
        return self.find_element_located(HomePageLocators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ')
    def click_confirm_order(self):
        return self.find_element_located(OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    def get_order_status(self):
        return self.find_element_located(OrderPageLocators.ORDER_STATUS)
