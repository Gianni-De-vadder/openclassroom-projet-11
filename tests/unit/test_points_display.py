import pytest

def test_points_display(client):
    response = client.get('/pointsDisplay')
    assert 'Simply Lift' in response.get_data(as_text=True)
    assert 'Points: 13' in response.get_data(as_text=True)
if __name__ == '__main__':
    pytest.main()