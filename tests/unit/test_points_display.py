def test_points_display(client, mocked_clubs):
    response = client.get('/pointsDisplay')
    assert 'Iron Temple' in response.get_data(as_text=True)
    assert 'Points: 13' in response.get_data(as_text=True)
