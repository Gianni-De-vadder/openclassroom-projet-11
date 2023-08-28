import pytest
from flask.testing import FlaskClient
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from server import app
from conftest import mocked_competitions, mocked_clubs

@pytest.mark.parametrize(
    'club_name, competition_name, places_required, expected_message',
    [
        ('Invalid Club', 'Spring Festival', 5, b"Something went wrong, you don't have enough points.")
        # Ajoutez d'autres scénarios de test ici
    ]
)
def test_book_invalid_club(client: FlaskClient, club_name, competition_name, places_required, expected_message):
    with patch('server.clubs', mocked_clubs), patch('server.competitions', mocked_competitions):
        response = client.post('/purchasePlaces', data={'club': club_name, 'competition': competition_name, 'places': str(places_required)}, follow_redirects=True)
        assert expected_message in response.data
