class TestDbContext:

    def test_when_clubs_are_loaded_then_return_clubs_list(self, db_context):
        club_list = db_context.load_clubs()

        assert club_list[0]['name'] == "Simply Lift"
        assert club_list[0]['email'] == "john@simplylift.co"
        assert club_list[0]['points'] == "13"

        assert club_list[1]['name'] == "Iron Temple"
        assert club_list[1]['email'] == "admin@irontemple.com"
        assert club_list[1]['points'] == "4"

        assert club_list[2]['name'] == "She Lifts"
        assert club_list[2]['email'] == "kate@shelifts.co.uk"
        assert club_list[2]['points'] == "12"
