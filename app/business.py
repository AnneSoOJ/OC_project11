from app.db_context import DbContext


class Business:
    def __init__(self, running_environment):
        self.db_context = DbContext(running_environment)

    def retrieve_club(self, email):
        club_list = [club for club in self.db_context.clubs if club['email'] == email]
        if len(club_list) == 0:
            return None
        return club_list[0]

    def set_club_points_balance(self, club_name, competition_name, places):
        club = [c for c in self.db_context.clubs if c['name'] == club_name][0]
        competition = [c for c in self.db_context.competitions if c['name'] == competition_name][0]
        places_required = int(places)
        result = {'succeeded': False, 'club': club, 'competitions': self.db_context.competitions}
        if places_required > int(club['points']):
            return result
        result['succeeded'] = True
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-places_required
        self.db_context.save_competitions()
        return result
