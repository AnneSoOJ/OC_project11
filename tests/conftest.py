import pytest

from app.server import create_app
from app.business import Business
from app.db_context import DbContext


@pytest.fixture
def business():
    business = Business('test')
    yield business
    reset_database()


@pytest.fixture
def app():
    app = create_app(None, 'test')
    yield app
    reset_database()


@pytest.fixture
def client():
    app = create_app({"TESTING": True}, 'test')
    with app.test_client() as client:
        yield client
    reset_database()


def reset_database():
    db_context = DbContext('test')
    db_context.clubs = [
        {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
        {"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
        {"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"}
    ]
    db_context.save_clubs()

    db_context.competitions = [
        {"name": "Spring Festival", "date": "2023-03-27 10:00:00", "numberOfPlaces": "25"},
        {"name": "Fall Classic", "date": "2020-10-22 13:30:00", "numberOfPlaces": "13"}
    ]
    db_context.save_competitions()
