import requests
import pytest
import allure
from base_case import BaseCase


@allure.epic('Booking Update Cases - epic')
@allure.suite('TEST BOOKING UPDATE - suite')
@pytest.mark.regression
class TestBookingUpdate():

    exclude_param = [
       {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
       },
        {
            "firstname": "Hayk",
            "lastname": "Abelyan",
            "totalprice": 222,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    ]

    data_for_path_update = [
        {
            "firstname": "James",
            "lastname": "Brown"
        }
    ]

    def setup_method(self):
        print('--------------------- Setup Method -----------------------')
        data = {"username": "admin", "password": "password123"}
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://restful-booker.herokuapp.com/auth', json=data, headers=headers)
        self.token = response.json().get('token')

    @allure.title('Test Update Booking')
    @allure.description('This test case verifies that the system successfully updates an existing booking.')
    @pytest.mark.parametrize('condition', exclude_param)
    def test_put_booking(self, condition):
        id = BaseCase.my_bookingid
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token={self.token}'}
        response = requests.put(f'https://restful-booker.herokuapp.com/booking/{id}', json=condition, headers=headers)
        assert response.status_code == 200, 'Status Code is Incorrect'
        assert 'bookingdates' in response.json(), 'error - bookingdates'

    @allure.title('Test Negative Update Booking')
    @allure.description('This test case verifies that the system correctly handles invalid update requests for a booking.')
    @pytest.mark.parametrize('condition', exclude_param)
    def test_negative_put_booking(self, condition):
        id = BaseCase.my_bookingid
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token=1111'}
        response = requests.put(f'https://restful-booker.herokuapp.com/booking/{id}', json=condition, headers=headers )
        response.status_code ==  403, f"Expected status code 403, but got {response.status_code}"


    @allure.title('Test Patch Booking')
    @allure.description('This test case verifies that the system successfully Patch updates an existing booking.')
    @pytest.mark.parametrize('condition', data_for_path_update)
    def test_patch_booking(self, condition):
        id = BaseCase.my_bookingid
        print('test_patch_booking', self.token)
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token={self.token}'}
        response = requests.patch(f'https://restful-booker.herokuapp.com/booking/{id}', json=condition, headers=headers)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        assert condition['firstname'] == response.json()['firstname'], 'error - bookingdates'

    @allure.title('Test Negative Update Booking')
    @allure.description('This test case verifies that the system correctly handles invalid update requests for a booking.')
    @pytest.mark.parametrize('condition', data_for_path_update)
    def test_negative_patch_booking(self, condition):
        id = BaseCase.my_bookingid
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': f'token=123'}
        response = requests.patch(f'https://restful-booker.herokuapp.com/booking/{id}', json=condition, headers=headers)
        assert response.status_code == 403, f"Expected status code 200, but got {response.status_code}"

