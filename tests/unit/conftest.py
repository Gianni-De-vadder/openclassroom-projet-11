import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mocked_clubs(monkeypatch):
    mocked_clubs_data = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "3"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "0"
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

def test_load_clubs(mocked_clubs):
    from server import loadClubs
    
    clubs = loadClubs()
    
    assert len(clubs) == 3
    assert clubs[0]['name'] == 'Simply Lift'
    assert clubs[1]['email'] == 'admin@irontemple.com'
    assert clubs[2]['points'] == '12'
