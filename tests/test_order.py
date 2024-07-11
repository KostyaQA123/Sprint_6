import pytest
import allure

from pages.order_page import OrderPage
from utils.order_data import OrderData


@allure.epic('Test Order')
class TestOrder:
    @allure.feature('Order')
    @allure.title('Order')
    @allure.story('Making an Order')
    @pytest.mark.parametrize("is_bottom, whom_form_data, rental_data", OrderData.test_data)
    def test_make_order(self, driver, is_bottom, whom_form_data, rental_data):
        order_page = OrderPage(driver)
        order_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        order_page.confirm_cookies()
        order_page.click_make_order(is_bottom)
        order_page.fill_for_whom_form(**whom_form_data)
        order_page.click_next()
        order_page.fill_about_rent_form(**rental_data)
        order_page.click_create_order_button()
        order_page.click_confirm_order()
        order_status = order_page.get_order_status()
        assert "Заказ оформлен" in order_status.text
