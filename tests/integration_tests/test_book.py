class TestBook:

    def test_when_club_and_competition_are_ok_then_return_http200_and_booking_page(self, client):
        """
        Test to assert if index page is well displayed.
        """
        response = client.get('/book/Fall Classic/Iron Temple')

        assert response.status_code == 200

        data = response.data.decode()
        assert "Booking for Fall Classic || GUDLFT" in data
        assert "Places available: 13" in data

    def test_when_club_and_competition_are_not_ok_then_return_http200_and_welcome_page(self, client):
        """
        Test to assert if index page is well displayed.
        """
        response = client.get('/book/Not an existing competition/notanexistingclub@kotest.com')

        assert response.status_code == 200

        data = response.data.decode()
        assert "Something went wrong. Please try again!" in data
