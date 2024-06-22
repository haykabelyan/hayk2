import requests
import allure
import pytest
from base_case import BaseCase


@allure.feature('TEST BOOKING GET - feature')
@allure.suite('TEST BOOKING GET - suite')
@pytest.mark.smoke
class TestBookingGet():

    @allure.title('Test Retrieve All Bookings')
    @allure.description('This test case verifies that the system retrieves all bookings successfully.')
    def test_get_booking_all(self):
        with allure.step(f'Run get request for all booking'):
            response = requests.get('https://restful-booker.herokuapp.com/booking')
        with allure.step('Check response code is 201'):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    @allure.title('Test Retrieve Booking by ID')
    @allure.description('This test case verifies that the system retrieves a specific booking by its ID successfully.')
    def test_get_booking_by_id(self):

        id = BaseCase.my_bookingid
        with allure.step(f'Run get request for booking with id {id}'):
            response = requests.get(f'https://restful-booker.herokuapp.com/booking/{id}')
        with allure.step('Check response code is 200'):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        with allure.step('Check firstname'):
            assert 'firstname' in response.json(), "The response does not contain 'firstname'"
        with allure.step('Check lastname'):
            assert 'lastname' in response.json(), "The response does not contain 'lastname'"
        with allure.step('Check bookingdates'):
            assert 'bookingdates' in response.json(), "The response does not contain 'bookingdates'"