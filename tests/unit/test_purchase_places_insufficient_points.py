def test_purchase_places_insufficient_points(client):
    response = client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '15'}, follow_redirects=True)
    assert b'Cannot use more points than available' in response.data
