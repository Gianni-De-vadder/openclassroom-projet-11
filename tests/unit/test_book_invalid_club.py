import pytest
from tests.conftest import client, club_name, competition_name, places_required, expected_message

def test_book_invalid_club(client, club_name, competition_name, places_required, expected_message):
    response = client.get(f'/book/{competition_name}/{club_name}', data={'places': places_required}, follow_redirects=True)
    assert expected_message.encode() in response.data
