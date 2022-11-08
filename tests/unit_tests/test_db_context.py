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

    def test_when_clubs_are_save_into_the_database(self, db_context):
        db_context.clubs.append({"name": "Heavy Set", "email": "admin@heavyset.co.uk", "points": "22"})
        db_context.save_clubs()
        club_list = db_context.load_clubs()

        assert club_list[3]['name'] == "Heavy Set"
        assert club_list[3]['email'] == "admin@heavyset.co.uk"
        assert club_list[3]['points'] == "22"

    def test_when_competitions_are_loaded_then_return_competitions_list(self, db_context):
        competition_list = db_context.load_competitions()

        assert competition_list[0]['name'] == "Spring Festival"
        assert competition_list[0]['date'] == "2023-03-27 10:00:00"
        assert competition_list[0]['numberOfPlaces'] == "25"

        assert competition_list[1]['name'] == "Fall Classic"
        assert competition_list[1]['date'] == "2020-10-22 13:30:00"
        assert competition_list[1]['numberOfPlaces'] == "13"

        assert competition_list[2]['name'] == "Summer Jam"
        assert competition_list[2]['date'] == "2022-12-30 15:00:00"
        assert competition_list[2]['numberOfPlaces'] == "5"

    def test_when_competitions_are_save_into_the_database(self, db_context):
        db_context.competitions.append({"name": "Winter Fest", "date": "2024-02-16 13:30:00", "numberOfPlaces": "9"})
        db_context.save_competitions()
        competition_list = db_context.load_competitions()

        assert competition_list[3]['name'] == "Winter Fest"
        assert competition_list[3]['date'] == "2024-02-16 13:30:00"
        assert competition_list[3]['numberOfPlaces'] == "9"
