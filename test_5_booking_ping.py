import requests
import allure
import pytest


# GITHUB BRANCH TEST

@allure.feature('TEST BOOKING GET PING- feature')
@allure.suite('TEST BOOKING GET PING - suite')
@pytest.mark.xxx
class TestBookingPing():

    @allure.title('Test Retrieve All Bookings')
    @allure.description('This test case verifies that the system retrieves all bookings successfully.')
    def test_get_booking_ping(self):
        response = requests.get('https://restful-booker.herokuapp.com/booking')
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

