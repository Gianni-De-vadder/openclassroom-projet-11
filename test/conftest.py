import pytest
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mocked_competitions(monkeypatch):
    # Mocked competitions data
    mocked_competitions_data = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": 25
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": 13
        }
    ]
    
    def mock_load_competitions():
        return mocked_competitions_data

    monkeypatch.setattr('server.loadCompetitions', mock_load_competitions)
    
    return mocked_competitions_data

@pytest.fixture
def mocked_clubs(monkeypatch):
    # Mocked clubs data
    mocked_clubs_data = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
        }
    ]
    
    def mock_load_clubs():
        return mocked_clubs_data

    monkeypatch.setattr('server.loadClubs', mock_load_clubs)
    
    return mocked_clubs_data
