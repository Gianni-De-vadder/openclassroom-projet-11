import pytest
from server import app

# Mocked competitions data
mocked_competitions = [
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

# Monkeypatching loadCompetitions function to return mocked data
def mock_load_competitions():
    return mocked_competitions

@pytest.fixture
def client(monkeypatch):
    app.config['TESTING'] = True

    monkeypatch.setattr('server.loadCompetitions', mock_load_competitions)

    with app.test_client() as client:
        yield client

def test_integration(client):
    response = client.get('/')
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    assert b'Welcome, john@simplylift.co' in response.data

    response = client.post('/book/Spring%20Festival/Simply%20Lift', data={'places': '5'}, follow_redirects=True)
    assert b"Booking complete!" in response.data

    response = client.post('/book/Invalid%20Competition/Simply%20Lift', data={'places': '5'}, follow_redirects=True)
    assert b"Something went wrong" in response.data

    response = client.post('/book/Spring%20Festival/Invalid%20Club', data={'places': '5'}, follow_redirects=True)
    assert b"Something went wrong, you don't have enough points." in response.data

    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '5'}, follow_redirects=True)
    assert b"Great-booking complete!" in response.data

    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '15'}, follow_redirects=True)
    assert b'Cannot use more points than available' in response.data

    response = client.post('/purchasePlaces', data={'competition': 'Invalid Competition', 'club': 'Invalid Club', 'places': '5'}, follow_redirects=True)
    assert b"Club or competition not found" in response.data

    response = client.get('/pointsDisplay')
    assert 'Simply Lift' in response.get_data(as_text=True)
    assert 'Points: 13' in response.get_data(as_text=True)

    response = client.get('/logout', follow_redirects=True)
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

if __name__ == '__main__':
    pytest.main()
