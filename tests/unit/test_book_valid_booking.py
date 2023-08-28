import pytest

def test_book_valid_booking(client):
    response = client.post('/book/Spring%20Festival/Simply%20Lift', data={'places': '5'}, follow_redirects=True)
    assert b"Booking complete!" in response.data

if __name__ == '__main__':
    pytest.main()