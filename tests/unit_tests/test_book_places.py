class TestBookPlaces:

    def test_when_all_booking_criteria_are_met_then_return_succeed_true(self, business):
        """
        Test to assert if club has enough points to purchase places for a specific competition
        """
        club_name = "She Lifts"
        competition_name = "Spring Festival"
        places = 8
        result = business.book_places(club_name, competition_name, places)

        assert result['succeeded'] is True

    def test_when_club_points_are_inferior_to_required_places_then_return_succeed_false(self, business):
        """
        Test to assert if club has not enough points to purchase places for a specific competition
        """
        club_name = "Iron Temple"
        competition_name = "Spring Festival"
        places = 8
        result = business.book_places(club_name, competition_name, places)

        assert result['succeeded'] is False
        assert result['error'] == 'Not enough points available'

    def test_when_club_book_more_than_the_maximum_amount_of_places_then_return_succeed_false(self, business):
        """
        Test to assert if club is trying to purchase more places than the maximum amount for a specific competition
        """
        club_name = "Simply Lift"
        competition_name = "Spring Festival"
        places = 13
        result = business.book_places(club_name, competition_name, places)

        assert result['succeeded'] is False
        assert result['error'] == 'Places total exceeds the maximum booking per competition'

    def test_when_club_book_places_for_past_competition_then_return_succeed_false(self, business):
        """
        Test to assert if club is trying to purchase places for a past competition
        """
        club_name = "Simply Lift"
        competition_name = "Fall Classic"
        places = 4
        result = business.book_places(club_name, competition_name, places)

        assert result['succeeded'] is False
        assert result['error'] == 'Places booking for this competition closed'

    def test_when_club_book_more_than_amount_of_places_available_then_return_succeed_false(self, business):
        """
        Test to assert if club is trying to purchase more places than the amount available for a specific competition
        """
        club_name = "She Lifts"
        competition_name = "Summer Jam"
        places = 10
        result = business.book_places(club_name, competition_name, places)

        assert result['succeeded'] is False
        assert result['error'] == 'Not enough places available'
