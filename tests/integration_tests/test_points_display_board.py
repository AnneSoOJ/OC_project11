class TestPointsDisplayBoard:

    def test_when_all_is_ok_then_return_http200_and_points_display_board_page(self, client):
        """
        Test to assert if registered club is displayed on the points display page
        """
        known_club = 'Iron Temple'
        response = client.get('/showClubs')
        data = response.data.decode()
        assert response.status_code == 200
        assert known_club in data
