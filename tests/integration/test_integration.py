import pytest

# Tests unitaires

def test_book_invalid_club(client):
    club_name = "Invalid Club"
    competition_name = "Spring Festival"
    expected_message = "Club or competition not found"  # Utilisez une chaîne de caractères

    response = client.get(
        f"/book/{competition_name}/{club_name}",
        data={"places": 2},
        follow_redirects=True,
    )
    
    assert expected_message.encode() in response.data  # Encodez la chaîne en bytes pour la comparaison


def test_book_invalid_competition(client):
    response = client.get(
        "/book/Invalid%20Competition/Simply%20Lift",
        data={"places": "5"},
        follow_redirects=True,
    )

    # Get the raw response content as text
    response_text = response.get_data(as_text=True)
    print(response_text)  # Print the response content for inspection

    # Check if the expected message is in the response content
    assert "Club or competition not found" in response_text

def test_book_valid_booking(client):
    response = client.get(
        "/book/Spring%20Festival/Simply%20Lift",
        data={"places": "5"},
        follow_redirects=True,
    )
    assert b"Spring Festival" in response.data

def test_index(client):
    response = client.get('/')
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data


def test_logout(client):
    response = client.get('/logout', follow_redirects=True)
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

def test_points_display(client):
    response = client.get('/pointsDisplay')
    assert 'Simply Lift' in response.get_data(as_text=True)
    assert 'Points: 13' in response.get_data(as_text=True)

def test_purchase_places_insufficient_points(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '15'}, follow_redirects=True)
    assert b'Cannot use more points than available' in response.data

def test_purchase_places_invalid_club_or_competition(client, monkeypatch):
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

    def mock_load_competitions():
        return mocked_competitions

    monkeypatch.setattr('server.loadCompetitions', mock_load_competitions)

    response = client.post('/purchasePlaces', data={'competition': 'Invalid Competition', 'club': 'Invalid Club', 'places': '5'}, follow_redirects=True)
    assert b"Club or competition not found" in response.data

def test_purchase_places_valid(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '5'}, follow_redirects=True)
    assert b"Great-booking complete!" in response.data

def test_show_summary_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    assert b'Welcome, john@simplylift.co' in response.data

def test_show_summary_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'invalid@example.com'}, follow_redirects=True)
    assert b'Unknown email address' in response.data

# Test d'intégration

def test_integration(client, monkeypatch):
    # Exécution des tests unitaires dans un ordre spécifique pour simuler un scénario d'utilisation
    test_book_invalid_club(client)
    test_book_invalid_competition(client)
    test_book_valid_booking(client)
    test_index(client)
    test_logout(client)
    test_points_display(client)
    test_purchase_places_insufficient_points(client)
    test_purchase_places_invalid_club_or_competition(client, monkeypatch)
    test_purchase_places_valid(client)
    test_show_summary_valid_email(client)
    test_show_summary_invalid_email(client)

if __name__ == '__main__':
    pytest.main()
