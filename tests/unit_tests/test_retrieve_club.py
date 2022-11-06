class TestRetrieveClub:

    def test_when_email_is_identified_then_return_club(self, business):
        """
        Test to assert if email is checked as a registered one and associated to the right club
        """
        known_email = 'admin@irontemple.com'
        club = business.retrieve_club(known_email)

        assert club['name'] == "Iron Temple"
        assert club['email'] == known_email
        assert int(club['points']) == 4

    def test_when_email_is_unidentified_then_return_none(self, business):
        """
        Test to assert if email is checked as a unregistered one and associated to any club
        """
        unknown_email = 'marketing@irontemple.com'
        club = business.retrieve_club(unknown_email)

        assert club is None
