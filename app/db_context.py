import json

PROD_DB_PATH = 'databases/prod_databases/'
TEST_DB_PATH = 'databases/test_databases/'


class DbContext:
    def __init__(self, running_environment):
        self.running_environment = running_environment
        self.competitions = self.load_competitions()
        self.clubs = self.load_clubs()

    def get_db_path(self, table):
        db_path = f'{PROD_DB_PATH}{table}'
        if self.running_environment == 'test':
            db_path = f'{TEST_DB_PATH}{table}'
        return db_path

    def load_clubs(self):
        with open(self.get_db_path('clubs.json')) as c:
            list_of_clubs = json.load(c)
            return list_of_clubs

    def save_clubs(self):
        with open(self.get_db_path('clubs.json'), 'w') as c:
            json.dump(self.clubs, c, indent=4)

    def load_competitions(self):
        with open(self.get_db_path('competitions.json')) as comps:
            list_of_competitions = json.load(comps)
            return list_of_competitions

    def save_competitions(self):
        with open(self.get_db_path('competitions.json'), 'w') as comps:
            json.dump(self.competitions, comps, indent=4)
