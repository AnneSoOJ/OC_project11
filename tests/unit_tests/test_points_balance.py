class TestPointsBalance:

    def test_when_club_points_are_superior_to_required_places_then_return_succeed_true(self, business):
        """
        Test to assert if club has enough points to purchase places for a specific competition
        """
        club_name = "She Lifts"
        competition_name = "Spring Festival"
        places = 8
        result = business.set_club_points_balance(club_name, competition_name, places)

        assert result['succeeded'] is True

    def test_when_club_points_are_inferior_to_required_places_then_return_succeed_false(self, business):
        """
        Test to assert if club has not enough points to purchase places for a specific competition
        """
        club_name = "Iron Temple"
        competition_name = "Spring Festival"
        places = 8
        result = business.set_club_points_balance(club_name, competition_name, places)

        assert result['succeeded'] is False
