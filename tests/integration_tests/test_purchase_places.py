class TestPurchasePlaces:

    def test_when_club_has_enough_points_to_purchase_places_then_return_http200_and_welcome_page(self, client):
        """
        Test to assert if places purchase is completed and therefore redirects to welcome/summary page
        """
        club_name = "She Lifts"
        competition_name = "Spring Festival"
        places = 8
        response = client.post('/purchasePlaces',
                               data={'club': club_name, 'competition': competition_name, 'places': places})
        data = response.data.decode()
        assert response.status_code == 200
        assert 'Booking completed' in data

    def test_when_club_has_not_enough_points_to_purchase_places_then_return_http200_and_booking_page(self, client):
        """
        Test to assert if places purchase is not completed and therefore redirects to booking/places purchase page
        """
        club_name = "Iron Temple"
        competition_name = "Spring Festival"
        places = 8
        response = client.post('/purchasePlaces',
                               data={'club': club_name, 'competition': competition_name, 'places': places})
        data = response.data.decode()
        assert response.status_code == 200
        assert 'Not enough points available' in data
