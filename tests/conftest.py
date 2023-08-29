import pytest
from flask import Flask

# Définir les données mockées
MOCKED_CLUBS_DATA = [
    {"name": "Club A", "email" : "john@simplylift.co", "points": 100},
    {"name": "Club B", "email" : "admin@irontemple.com",  "points": 200},
    # ... autres clubs mockés
]

MOCKED_COMPETITIONS_DATA = [
    {"name": "Competition X", "date" : "2020-10-22 13:30:00", "numberOfPlaces": 50},
    {"name": "Competition Y", "date" : "2020-10-22 13:30:00" , "numberOfPlaces": 30},
]

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def mocked_clubs(monkeypatch):
    monkeypatch.setattr('server.loadClubs', lambda: MOCKED_CLUBS_DATA)
    return MOCKED_CLUBS_DATA

@pytest.fixture
def mocked_competitions(monkeypatch):
    monkeypatch.setattr('server.loadCompetitions', lambda: MOCKED_COMPETITIONS_DATA)
    return MOCKED_COMPETITIONS_DATA

@pytest.fixture
def club_name():
    return "Invalid Club" 

@pytest.fixture
def competition_name():
    return "Invalid Competition" 

@pytest.fixture
def places_required():
    return "5"

@pytest.fixture
def expected_message():
    return "Invalid club or competition"
