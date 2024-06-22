import requests
import allure
import pytest
from base_case import BaseCase


@allure.feature('Booking Post Cases - feature')
@allure.suite('TEST BOOKING POST - suite')
@pytest.mark.smoke
class TestBookingPost:

    @allure.title('Test Create Booking')
    @allure.description('This test case verifies that the system successfully creates a new booking.')
    def test_create_booking(self):
        # Arrange
        body = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post('https://restful-booker.herokuapp.com/booking', json=body, headers=headers)

        assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"

        response_data = response.json()
        assert 'bookingid' in response_data, "The response does not contain 'bookingid'"

        booking = response_data['booking']
        assert booking['firstname'] == body['firstname'], f"Expected firstname {body['firstname']}, but got {booking['firstname']}"
        assert booking['lastname'] == body['lastname'], f"Expected lastname {body['lastname']}, but got {booking['lastname']}"
        assert booking['totalprice'] == body['totalprice'], f"Expected totalprice {body['totalprice']}, but got {booking['totalprice']}"
        assert booking['depositpaid'] == body['depositpaid'], f"Expected depositpaid {body['depositpaid']}, but got {booking['depositpaid']}"
        assert booking['bookingdates']['checkin'] == body['bookingdates']['checkin'], f"Expected checkin date {body['bookingdates']['checkin']}, but got {booking['bookingdates']['checkin']}"
        assert booking['bookingdates']['checkout'] == body['bookingdates']['checkout'], f"Expected checkout date {body['bookingdates']['checkout']}, but got {booking['bookingdates']['checkout']}"
        assert booking['additionalneeds'] == body['additionalneeds'], f"Expected additionalneeds {body['additionalneeds']}, but got {booking['additionalneeds']}"

        BaseCase.my_bookingid = response_data['bookingid']