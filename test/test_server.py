import json
import os
import pytest
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

def test_show_summary_valid_email(client):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True)
    assert b'Welcome, john@simplylift.co' in response.data


def test_show_summary_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'invalid@example.com'}, follow_redirects=True)
    assert b'Unknown email address' in response.data


def test_book_valid_booking(client):
    response = client.post('/book/Spring%20Festival/Simply%20Lift', data={'places': '5'}, follow_redirects=True)
    assert b"Booking complete!" in response.data

def test_book_invalid_competition(client):
    response = client.post('/book/Invalid%20Competition/Simply%20Lift', data={'places': '5'}, follow_redirects=True)
    assert b"Something went wrong" in response.data

def test_book_invalid_club(client):
    response = client.post('/book/Spring%20Festival/Invalid%20Club', data={'places': '5'}, follow_redirects=True)
    assert b"Something went wrong" in response.data

def test_purchase_places_valid(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '5'}, follow_redirects=True)
    assert b"Great-booking complete!" in response.data

def test_purchase_places_insufficient_points(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '15'}, follow_redirects=True)
    assert b'Cannot use more points than available' in response.data


def test_purchase_places_invalid_club_or_competition(client):
    response = client.post('/purchasePlaces', data={'competition': 'Invalid Competition', 'club': 'Invalid Club', 'places': '5'}, follow_redirects=True)
    assert b"Club or competition not found" in response.data

def test_points_display(client):
    response = client.get('/pointsDisplay')
    assert 'Simply Lift' in response.get_data(as_text=True)
    assert 'Points: 13' in response.get_data(as_text=True)



def test_logout(client):
    response = client.get('/logout', follow_redirects=True)
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data


if __name__ == '__main__':
    pytest.main()
