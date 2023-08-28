import pytest

def test_purchase_places_valid(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '5'}, follow_redirects=True)
    assert b"Great-booking complete!" in response.data

if __name__ == '__main__':
    pytest.main()