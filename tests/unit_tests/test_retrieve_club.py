from app.server import retrieve_club


class TestRetrieveClub:

    def test_known_email_should_retrieve_club(self):
        """
        Test to assert if email is checked as a registered one and associated to the right club
        """
        known_email = 'admin@irontemple.com'
        club = retrieve_club(known_email)

        assert club['name'] == "Iron Temple"
        assert club['email'] == known_email
        assert int(club['points']) == 4

    def test_unknown_email_should_return_none(self):
        """
        Test to assert if email is checked as a unregistered one and associated to any club
        """
        unknown_email = 'marketing@irontemple.com'
        club = retrieve_club(unknown_email)

        assert club is None
