from app.db_context import DbContext

from datetime import datetime


class Business:

    MAX_BOOKING_PER_COMPETITION = 12
    POINTS_PER_PLACE = 1

    def __init__(self, running_environment):
        self.db_context = DbContext(running_environment)

    def retrieve_club(self, email):
        club_list = [club for club in self.db_context.clubs if club['email'] == email]
        if len(club_list) == 0:
            return None
        return club_list[0]

    def book_places(self, club_name, competition_name, places):
        club = [c for c in self.db_context.clubs if c['name'] == club_name][0]
        competition = [c for c in self.db_context.competitions if c['name'] == competition_name][0]
        places_required = int(places)
        result = {'succeeded': False, 'club': club, 'competitions': self.db_context.competitions}
        if places_required * self.POINTS_PER_PLACE > int(club['points']):
            result['error'] = "Not enough points available"
            return result
        if places_required > self.MAX_BOOKING_PER_COMPETITION:
            result['error'] = "Places total exceeds the maximum booking per competition"
            return result
        if datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            result['error'] = "Places booking for this competition closed"
            return result
        if places_required > int(competition['numberOfPlaces']):
            result['error'] = "Not enough places available"
            return result
        result['succeeded'] = True
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-places_required
        club['points'] = int(club['points'])-places_required
        self.db_context.save_competitions()
        self.db_context.save_clubs()
        return result
