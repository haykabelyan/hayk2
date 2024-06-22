import requests
import allure
import pytest
from base_case import BaseCase

@allure.feature('TEST BOOKING DELETE- feature')
@allure.suite('TEST BOOKING DELETE - suite')
@pytest.mark.smoke
class TestBookingDelete():

    def setup_method(self):
        print('--------------------- Setup Method -----------------------')
        data = {"username": "admin", "password": "password123"}
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://restful-booker.herokuapp.com/auth', json=data, headers=headers)
        self.token = response.json().get('token')
        self.bookingid = BaseCase.my_bookingid

    @allure.title('Test delete Booking')
    @allure.description('This test case verifies that the system delete bookings successfully.')
    def test_delete_booking(self):
        headers = {'Content-Type': 'application/json', 'Cookie': f'token= {self.token}'}
        # headers = {'Content-Type': 'application/json', 'Authorization': f'Basic YWRtaW46cGFzc3dvcmQxMjM='}
        response = requests.delete(f'https://restful-booker.herokuapp.com/booking/{self.bookingid}', headers=headers)
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"